# Multi-PDF-RAG-Assistant---Assignment1

**Multi-PDF-RAG-Assistant---Assignment1** is a Retrieval-Augmented Generation (RAG) application developed as part of a college course assignment. It enables users to upload multiple PDF documents and interact with their contents through a conversational AI assistant.

## Project Overview

The application extracts text from multiple PDF files, divides it into manageable chunks, and converts those chunks into vector embeddings for semantic retrieval. When a user submits a question, the system retrieves relevant information from the uploaded documents and passes it as context to a Large Language Model (LLM), which generates a context-aware response grounded in the provided content.

## Features

- **Multi-PDF Upload:** Upload and process multiple PDF documents for querying.
- **Smart Text Chunking:** Splits extracted text into smaller, manageable chunks while preserving contextual relevance.
- **Vector Embeddings:** Converts text chunks into vector representations to support semantic similarity search.
- **Context-Aware Question Answering:** Generates responses based on relevant information retrieved from the uploaded documents.
- **Conversational Interface:** Allows users to ask natural-language questions about their documents.
- **Retrieval-Augmented Generation:** Combines document retrieval with LLM-based response generation to provide document-grounded answers.

## Built With

- **Python** — Core application logic and document processing.
- **LangChain** — Orchestrates document retrieval and LLM integration.
- **Streamlit** — Provides the interactive web interface.
- **ChromaDB / FAISS** — Vector storage and similarity search (specify the one actually used in your implementation).
- **Groq API** — Provides access to the language model, if configured in the application.
- **Sentence Transformers** — Generates text embeddings, if used by the configured embedding model.

## Objective

The objective of this project is to demonstrate how RAG can make information retrieval from multiple documents more efficient by combining semantic search with large language models, enabling users to ask questions and receive answers grounded in their uploaded PDFs.

## Getting Started

1. Clone the repository.
2. Install the required dependencies using `requirements.txt`.
3. Configure the necessary environment variables in a `.env` file.
4. Launch the Streamlit application.
5. Upload PDF documents and start asking questions about their content.

**Note:** Keep API keys and other credentials private. Do not upload your `.env` file to GitHub.
