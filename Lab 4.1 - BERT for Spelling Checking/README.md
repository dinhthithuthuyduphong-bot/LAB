# Lab 4: Vietnamese Spell-checking using PhoBERT

## 1 Lab Overview

This lab demonstrates how to leverage PhoBERT (Vietnamese BERT) for intelligent spell-checking by using masked language modeling. Instead of relying on simple dictionary lookups, we use the contextual understanding capabilities of BERT to identify potential spelling errors by measuring how well each word fits within its surrounding context.
---

## 2 Lab Structure

### **Step 1: Study the Knowledge Base**
**File**: `spelling-detect-coreidea.ipynb`

This notebook contains the **complete working implementation** that you should study carefully:

#### **Study Guide Questions**:
While reviewing the knowledge notebook, consider:
- How does masking individual words help detect spelling errors?
- Why do we use probability thresholds for error detection?
- How do Vietnamese accents affect similarity comparison?
- What makes PhoBERT better than multilingual BERT for Vietnamese text?

### **Step 2: Implement Your Solution**
**File**: `spelling-detect-TODO-key.ipynb`

This is your **implementation workspace** where you'll build the complete pipeline from scratch:

---

## 🚀 Getting Started

### **Prerequisites**
- Python 3.7+ with Jupyter Notebook support (Suggest best is 3.10)
- Basic understanding of BERT and transformer models
- Familiarity with Vietnamese text (helpful but not required)

### **Installation**
```bash
pip install transformers torch torchvision torchaudio
```
---
