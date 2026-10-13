# Multi-PDF RAG Assistant

A Retrieval-Augmented Generation (RAG) application that allows users to interact with information from multiple PDF documents using natural-language questions. The project combines document processing, vector-based retrieval, and a large language model to generate context-aware answers from uploaded documents.

## Overview

Reading and searching through lengthy PDF documents manually can be time-consuming. This project aims to simplify that process by allowing users to provide PDF documents and ask questions about their content through an interactive application.

The system processes documents, divides their content into smaller chunks, generates embeddings, retrieves relevant passages, and uses a language model to generate answers based on the retrieved context.

## Features

- **Multi-PDF Support:** Work with multiple PDF documents in a single workflow.
- **Document Processing:** Extract and prepare PDF text for retrieval.
- **Text Chunking:** Split document content into manageable chunks.
- **Semantic Search:** Use embeddings to identify contextually relevant passages.
- **Vector Storage:** Support vector-based retrieval using FAISS and ChromaDB.
- **LLM-Powered Answers:** Generate responses using Groq-hosted language models.
- **Interactive Interface:** Use a Streamlit application to interact with documents.
- **Question Answering:** Ask natural-language questions about the provided document content.

## Technology Stack

| Component | Technology |
|---|---|
| Programming Language | Python |
| User Interface | Streamlit |
| LLM Integration | LangChain, LangChain-Groq |
| Language Model Provider | Groq |
| Embeddings | Hugging Face Sentence Transformers |
| Vector Search | FAISS, ChromaDB |
| Document Source | PDF files |
| Testing | pytest |

## Project Structure

```text
Multi-PDF-RAG-Assistant/
├── src/
│   ├── app.py
│   └── rag_pipeline.py
├── tests/
├── notebooks/
├── documents/
├── vector_store/
├── .streamlit/
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

*Note: Adjust this structure to match the actual files in your repository. The `vector_store/` directory may be generated at runtime and does not necessarily need to be committed.*

## How It Works

The application follows a Retrieval-Augmented Generation workflow:

1. **Document Input:** Provide the PDF documents to be processed.
2. **Text Extraction:** Extract textual content from the PDFs.
3. **Chunking:** Split the extracted text into smaller, overlapping chunks where configured.
4. **Embedding Generation:** Convert text chunks into vector representations using an embedding model.
5. **Vector Indexing:** Store or index the embeddings using the configured vector database.
6. **Question Processing:** Accept a question from the user.
7. **Context Retrieval:** Retrieve document passages relevant to the question.
8. **Answer Generation:** Pass the retrieved context and question to the language model.
9. **Response Display:** Display the generated answer through the Streamlit interface.

## Prerequisites

Before running the project, ensure you have:

- Python installed
- Git installed
- A Groq API key
- Internet access for API calls and any required model downloads

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/BhumikaTechHub/Gen-AI---Assignment-1-2.git
cd Gen-AI---Assignment-1-2
```

If you place the project inside a subdirectory, navigate into that directory before continuing.

### 2. Create a virtual environment

**Windows PowerShell**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, you can run the project using the virtual environment's Python executable directly.

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root, using `.env.example` as a reference.

Example:

```env
GROQ_API_KEY=your_groq_api_key
GROQ_MODEL=openai/gpt-oss-20b
EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2
```

Use a Groq model currently available to your account and supported by your installed integration. The model shown above is a configuration example; verify availability before using it.

**Security:** Never commit your actual `.env` file or expose your API key in source code, screenshots, or public repositories.

### 5. Run the application

From the project root, run:

```bash
python -m streamlit run src/app.py
```

Streamlit will provide a local URL, typically:

```text
http://localhost:8501
```

Open the URL in your browser to use the application.

## Usage

1. Start the Streamlit application.
2. Upload or provide PDF documents using the available interface.
3. Allow the application to process the documents and build its retrieval index.
4. Enter a question related to the document content.
5. Review the generated response.
6. Ask follow-up questions to explore other information in the documents.

The quality of answers depends on the text extracted from the PDFs, retrieval configuration, embedding model, and language model.

## Testing

If the project includes pytest tests, run them from the project root:

```bash
python -m pytest -v
```

Review any failures and ensure the required dependencies and test configuration are installed.

## Troubleshooting

### Groq model not found

If you receive a `model_not_found` error, check that the configured model identifier is currently supported and available to your Groq account.

### Missing Python packages

Ensure that the virtual environment is active and install dependencies:

```bash
python -m pip install -r requirements.txt
```

### PDF text is not retrieved correctly

Check whether the PDF contains selectable text or scanned images. Scanned documents may require OCR, depending on the application's implementation.

### Application fails to start

Verify that `src/app.py` exists, required environment variables are configured, and the dependencies in `requirements.txt` are installed.

## Future Improvements

Potential enhancements include:

- Displaying source document names and relevant passages with answers
- Supporting scanned PDFs through OCR
- Adding conversation history and follow-up question handling
- Improving retrieval through metadata filtering and reranking
- Adding document-management controls
- Deploying the application to a cloud platform

These are possible future improvements and may not be implemented in the current version.

## Learning Outcomes

This project provides practical experience with:

- Retrieval-Augmented Generation
- Document ingestion and text preprocessing
- Embeddings and semantic search
- Vector databases
- LangChain and LLM integration
- API configuration and environment-variable management
- Building interactive AI applications with Streamlit

## Author

**Bhumika Yadav**

B.Tech, Computer Science & Engineering

GitHub: [BhumikaTechHub](https://github.com/BhumikaTechHub)

---

*This project is intended for learning and experimentation with document-based question answering and retrieval-augmented generation.*
