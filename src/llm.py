"""LLM wrappers.  🟡 Needs a GPU (Kaggle T4/P100, Colab T4). Not executed in the CPU dev environment.

* HFChatLLM  — instruct models via transformers + chat template (Qwen2.5-*-Instruct, Llama-3.2-*-Instruct…)
* HFBaseLLM  — plain text-generation for the baseline (Qwen1.5-1.8B base), mirrors the baseline settings
Both use greedy decoding (deterministic).
"""


def _load(model_id, load_in_4bit=False):
    import torch
    from transformers import AutoModelForCausalLM, AutoTokenizer
    tok = AutoTokenizer.from_pretrained(model_id)
    kw = {"torch_dtype": torch.float16, "device_map": "auto"}
    if load_in_4bit:
        from transformers import BitsAndBytesConfig
        kw["quantization_config"] = BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_compute_dtype=torch.float16,
                                                       bnb_4bit_quant_type="nf4")
    model = AutoModelForCausalLM.from_pretrained(model_id, **kw).eval()
    if tok.pad_token is None:
        tok.pad_token = tok.eos_token
    tok.padding_side = "left"
    return tok, model


class HFChatLLM:
    def __init__(self, model_id, max_new_tokens=640, repetition_penalty=1.1, load_in_4bit=False, max_input_tokens=3500):
        self.tok, self.model = _load(model_id, load_in_4bit)
        self.max_new_tokens, self.rep, self.max_in = max_new_tokens, repetition_penalty, max_input_tokens

    def generate(self, messages_batch):
        import torch
        prompts = [self.tok.apply_chat_template(m, tokenize=False, add_generation_prompt=True) for m in messages_batch]
        enc = self.tok(prompts, return_tensors="pt", padding=True, truncation=True, max_length=self.max_in).to(self.model.device)
        with torch.no_grad():
            out = self.model.generate(**enc, max_new_tokens=self.max_new_tokens, do_sample=False,
                                      repetition_penalty=self.rep, pad_token_id=self.tok.pad_token_id)
        gen = out[:, enc["input_ids"].shape[1]:]
        return [self.tok.decode(g, skip_special_tokens=True) for g in gen], prompts


class HFBaseLLM:
    """Baseline-equivalent generation: plain prompt, greedy, max_new_tokens=256, no input truncation.

    echo_prompt=True reproduces doc/Baseline.ipynb exactly: LangChain's HuggingFacePipeline uses the
    transformers default return_full_text=True, so the *prompt (incl. retrieved context) is part of the
    evaluated answer*. echo_prompt=False returns only the generated continuation (the "fixed" baseline).
    """

    def __init__(self, model_id="Qwen/Qwen1.5-1.8B", max_new_tokens=256, echo_prompt=True):
        self.tok, self.model = _load(model_id)
        self.max_new_tokens, self.echo = max_new_tokens, echo_prompt

    def generate(self, prompts):
        import torch
        outs = []
        for p in prompts:                       # batch=1: no padding, identical to the notebook
            enc = self.tok(p, return_tensors="pt").to(self.model.device)
            with torch.no_grad():
                out = self.model.generate(**enc, max_new_tokens=self.max_new_tokens, do_sample=False,
                                          pad_token_id=self.tok.pad_token_id)
            gen = self.tok.decode(out[0, enc["input_ids"].shape[1]:], skip_special_tokens=True)
            outs.append(p + gen if self.echo else gen)
        return outs, prompts
