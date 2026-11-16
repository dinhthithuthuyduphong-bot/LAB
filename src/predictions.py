"""Safe reading / writing of results/predictions/<name>.csv.

Writes are atomic (write a temp file, then os.replace), so interrupting a Kaggle/Colab cell at any moment
leaves either the old or the new complete file — never a half-written one. Reading also tolerates files
damaged by older versions (cut-off UTF-8 character or unfinished quoted row at the end).
"""
import io
import os
from pathlib import Path

import pandas as pd


def _clean(df):
    if df is None or df.empty or "id" not in df.columns:
        return pd.DataFrame()
    df = df[pd.to_numeric(df["id"], errors="coerce").notna()].copy()
    df["id"] = df["id"].astype(int)
    return df.drop_duplicates("id", keep="last").reset_index(drop=True)


def load_predictions(path):
    path = Path(path)
    if not path.exists():
        return pd.DataFrame()
    try:
        return _clean(pd.read_csv(path))
    except Exception:
        pass
    # damaged file: decode leniently, then drop trailing text until the remainder parses
    text = path.read_bytes().decode("utf-8", errors="ignore")
    while text:
        try:
            df = _clean(pd.read_csv(io.StringIO(text)))
            print(f"⚠️  {path.name} was damaged (interrupted write); recovered {len(df)} complete rows")
            save_predictions(path, df)
            return df
        except Exception:
            cut = text.rstrip("\n").rfind("\n")
            text = text[:cut] if cut > 0 else ""
    return pd.DataFrame()


def save_predictions(path, df):
    path = Path(path)
    tmp = path.with_suffix(path.suffix + ".tmp")
    df.to_csv(tmp, index=False)
    os.replace(tmp, path)


def append_predictions(path, new_rows):
    old = load_predictions(path)
    df = pd.concat([old, pd.DataFrame(new_rows)], ignore_index=True) if len(old) else pd.DataFrame(new_rows)
    save_predictions(path, _clean(df))
