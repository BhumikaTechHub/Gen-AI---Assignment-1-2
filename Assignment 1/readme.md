
#  Multi-PDF RAG System using LangChain, FAISS & Groq


This project implements a **Technical Documentation Assistant** using a **Retrieval-Augmented Generation (RAG)** approach. It is designed to help users query and understand **technical documents (PDFs)** efficiently.

Unlike traditional LLM responses, this system ensures:
-  Answers are grounded in uploaded documents
- Relevant context is retrieved using vector search
- Responses are generated using a powerful LLM (LLaMA via Groq)

---

##  Features

- Acts as a **Technical Documentation Assistant**
- Supports **multiple PDFs (10 or more)**
- Intelligent **text chunking** for better retrieval
- Dual vector database support:
- FAISS (fast similarity search)
- Chroma (persistent storage)
- Uses **HuggingFace embeddings**
- Accurate **context-based answering**
- Source tracking (which PDF the answer came from)
- Modular **class-based architecture**
- Interactive CLI chat system



## Installation

Run in Google Colab or locally:

```bash
pip install langchain langchain-community langchain-huggingface faiss-cpu chromadb pypdf groq
```


