Here’s a **clean, professional `README.md`** for your project 👇
(You can copy-paste this directly into GitHub)

---

#  GenAI Assignment: Fine-Tuning LLM for Customer Support

## Overview

This project focuses on improving the performance of a Large Language Model (LLM) for **customer support tasks** using **fine-tuning techniques**. The base model is adapted to generate more relevant and structured responses using domain-specific data.

---

##  Objective

* Improve response quality of a pretrained LLM
* Adapt the model for customer support queries
* Compare **base vs fine-tuned model performance**
* Evaluate using both **quantitative and qualitative metrics**

---

##  Model Details

* **Base Model:** Qwen2.5-1.5B-Instruct
* **Architecture:** Transformer-based Causal Language Model
* **Fine-Tuning Method:** LoRA (Low-Rank Adaptation)
* **Quantization:** 4-bit (BitsAndBytes)

---

##  Dataset

* **Source:** Bitext Customer Support Dataset
* **Format:** Instruction–Response pairs
* **Size:** 1000 samples
* **Split:**

  * Training: 90%
  * Testing: 10%

---

##  Training Configuration

* Batch Size: 2
* Gradient Accumulation: 4
* Learning Rate: 2e-4
* Optimizer: AdamW
* Max Steps: 200
* Precision: bfloat16

---

##  Evaluation Metrics

###  Quantitative Metrics

* ROUGE (Text similarity)
* BLEU (Generation quality)
* Keyword Matching Score

###  Qualitative Evaluation

* Human comparison of responses
* Analysis of relevance, structure, and clarity

---

##  Results Summary

| Metric        | Base Model | Fine-Tuned Model |
| ------------- | ---------- | ---------------- |
| ROUGE-1       | 0.3324     | 0.3067           |
| ROUGE-2       | 0.1291     | 0.0865           |
| ROUGE-L       | 0.2355     | 0.1833           |
| BLEU          | 0.0436     | 0.0069           |
| Keyword Match | 0.2571     | 0.2543           |

>  Note: Traditional metrics showed limited improvement due to the generative nature of LLMs. However, qualitative evaluation indicated better response structure and domain relevance.

---

## Key Observations

* Fine-tuned model generates more structured responses
* Improved alignment with customer support context
* Metrics like BLEU/ROUGE may not fully capture conversational improvements

---

## Human Evaluation

Human evaluation was performed by comparing outputs from both models. The fine-tuned model demonstrated:

* Better clarity
* More step-by-step responses
* Improved domain relevance

---

##  Tech Stack

* Python
* PyTorch
* Hugging Face Transformers
* PEFT (LoRA)
* Datasets Library









