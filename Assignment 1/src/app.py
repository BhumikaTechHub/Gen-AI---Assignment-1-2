
from pathlib import Path
import sys

import streamlit as st
from dotenv import load_dotenv

# Ensure imports work when running: streamlit run src/app.py
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

load_dotenv(ROOT / ".env")

from src.document_processor import DocumentProcessor
from src.embeddings import EmbeddingManager
from src.vector_store import VectorStoreManager
from src.rag_pipeline import RAGPipeline


st.set_page_config(
    page_title="Multi-PDF RAG Assistant",
    page_icon="📚",
    layout="wide",
)

st.title("📚 Multi-PDF RAG Assistant")
st.caption(
    "Ask questions about your technical PDFs and inspect the sources."
)

DOCUMENTS_DIR = ROOT / "documents"
INDEX_DIR = ROOT / "vector_store"

if "rag" not in st.session_state:
    st.session_state.rag = None

if "messages" not in st.session_state:
    st.session_state.messages = []

with st.sidebar:
    st.header("Configuration")

    store_type = st.selectbox(
        "Vector store",
        ["faiss", "chroma"],
    )

    chunk_size = st.number_input(
        "Chunk size",
        min_value=200,
        max_value=3000,
        value=1000,
        step=100,
    )

    chunk_overlap = st.number_input(
        "Chunk overlap",
        min_value=0,
        max_value=1000,
        value=150,
        step=50,
    )

    top_k = st.slider(
        "Retrieved chunks",
        min_value=1,
        max_value=10,
        value=4,
    )

    st.divider()

    st.subheader("Documents")

    pdf_files = sorted(DOCUMENTS_DIR.glob("*.pdf"))

    if pdf_files:
        st.write(f"Found **{len(pdf_files)} PDF files**.")
        for pdf in pdf_files:
            st.caption(f"📄 {pdf.name}")
    else:
        st.warning("Add PDF files to the documents/ folder.")

    st.divider()

    build_clicked = st.button(
        "Build / Rebuild Index",
        use_container_width=True,
    )

    load_clicked = st.button(
        "Load Existing Index",
        use_container_width=True,
    )

    if chunk_overlap >= chunk_size:
        st.error("Chunk overlap must be smaller than chunk size.")

    elif build_clicked:
        try:
            with st.spinner("Processing PDFs and building index..."):
                processor = DocumentProcessor(
                    documents_dir=str(DOCUMENTS_DIR),
                    chunk_size=int(chunk_size),
                    chunk_overlap=int(chunk_overlap),
                )

                pages, chunks, errors = processor.process()

                embedding_manager = EmbeddingManager()
                manager = VectorStoreManager(
                    embeddings=embedding_manager.get_embeddings(),
                    store_type=store_type,
                    persist_root=str(INDEX_DIR),
                )

                vector_store = manager.build(chunks)

                st.session_state.rag = RAGPipeline(
                    vector_store=vector_store,
                    k=int(top_k),
                )

                st.session_state.messages = []

                st.success(
                    f"Indexed {len(pages)} pages into {len(chunks)} chunks."
                )

                if errors:
                    st.warning("Some PDFs could not be processed:")
                    for error in errors:
                        st.write(f"- {error}")

        except Exception as exc:
            st.error(f"Indexing failed: {exc}")

    elif load_clicked:
        try:
            with st.spinner("Loading saved index..."):
                embedding_manager = EmbeddingManager()

                manager = VectorStoreManager(
                    embeddings=embedding_manager.get_embeddings(),
                    store_type=store_type,
                    persist_root=str(INDEX_DIR),
                )

                vector_store = manager.load()

                st.session_state.rag = RAGPipeline(
                    vector_store=vector_store,
                    k=int(top_k),
                )

                st.session_state.messages = []
                st.success(f"Loaded the {store_type} index.")

        except Exception as exc:
            st.error(f"Could not load the index: {exc}")

# Display previous messages.
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

        if message["role"] == "assistant":
            for source in message.get("sources", []):
                page = source.get("page")
                page_text = f", page {page}" if page else ""

                with st.expander(
                    f"{source['source']}{page_text}"
                ):
                    st.write(source["excerpt"])

question = st.chat_input("Ask a question about your PDFs...")

if question:
    if st.session_state.rag is None:
        st.warning(
            "Build or load an index from the sidebar before asking questions."
        )
    else:
        st.session_state.messages.append(
            {"role": "user", "content": question}
        )

        with st.chat_message("user"):
            st.markdown(question)

        with st.chat_message("assistant"):
            with st.spinner("Searching documents and generating an answer..."):
                try:
                    # Update retrieval count without rebuilding the index.
                    st.session_state.rag.k = int(top_k)
                    result = st.session_state.rag.ask(question)

                    st.markdown(result["answer"])

                    for source in result["sources"]:
                        page = source.get("page")
                        page_text = f", page {page}" if page else ""

                        with st.expander(
                            f"{source['source']}{page_text}"
                        ):
                            st.write(source["excerpt"])

                    st.session_state.messages.append(
                        {
                            "role": "assistant",
                            "content": result["answer"],
                            "sources": result["sources"],
                        }
                    )

                except Exception as exc:
                    st.error(f"Question answering failed: {exc}")
