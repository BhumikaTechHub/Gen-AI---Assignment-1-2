
import pytest

from langchain_core.documents import Document
from src.document_processor import DocumentProcessor


def test_split_documents_creates_chunks(tmp_path):
    processor = DocumentProcessor(
        documents_dir=str(tmp_path),
        chunk_size=100,
        chunk_overlap=20,
    )

    document = Document(
        page_content="Technical documentation. " * 30,
        metadata={
            "source": "example.pdf",
            "page": 0,
        },
    )

    chunks = processor.split_documents([document])

    assert len(chunks) > 1
    assert all(chunk.page_content.strip() for chunk in chunks)
    assert all(
        chunk.metadata["source"] == "example.pdf"
        for chunk in chunks
    )


def test_invalid_chunk_overlap_is_rejected(tmp_path):
    with pytest.raises(ValueError):
        DocumentProcessor(
            documents_dir=str(tmp_path),
            chunk_size=100,
            chunk_overlap=100,
        )


def test_empty_documents_produce_no_chunks(tmp_path):
    processor = DocumentProcessor(
        documents_dir=str(tmp_path),
        chunk_size=100,
        chunk_overlap=20,
    )

    assert processor.split_documents([]) == []
