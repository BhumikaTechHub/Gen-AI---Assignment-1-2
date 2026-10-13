
from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


class DocumentProcessor:
    def __init__(
        self,
        documents_dir="documents",
        chunk_size=1000,
        chunk_overlap=150,
    ):
        self.documents_dir = Path(documents_dir)
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

        if chunk_size <= 0:
            raise ValueError("chunk_size must be positive.")

        if chunk_overlap < 0 or chunk_overlap >= chunk_size:
            raise ValueError(
                "chunk_overlap must be >= 0 and smaller than chunk_size."
            )

        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            add_start_index=True,
        )

    def load_documents(self):
        if not self.documents_dir.exists():
            raise FileNotFoundError(
                f"Documents directory not found: {self.documents_dir}"
            )

        pdf_files = sorted(self.documents_dir.glob("*.pdf"))

        if not pdf_files:
            raise FileNotFoundError(
                f"No PDF files found in {self.documents_dir.resolve()}"
            )

        documents = []
        errors = []

        for pdf_path in pdf_files:
            try:
                pages = PyPDFLoader(str(pdf_path)).load()

                # Preserve the original filename and page metadata.
                for page in pages:
                    page.metadata["source"] = pdf_path.name

                extracted_text = "".join(
                    page.page_content.strip() for page in pages
                )

                if not extracted_text:
                    errors.append(
                        f"{pdf_path.name}: no extractable text"
                    )
                    continue

                documents.extend(pages)

            except Exception as exc:
                errors.append(f"{pdf_path.name}: {exc}")

        if not documents:
            raise ValueError(
                "No readable PDF text was found. Check the PDFs "
                "or use OCR for scanned documents. "
                + "; ".join(errors)
            )

        return documents, errors


    def split_documents(self, documents):
        if not documents:
            return []

        chunks = self.splitter.split_documents(documents)

    # Remove empty chunks and preserve document metadata.
        chunks = [
            chunk
            for chunk in chunks
            if chunk.page_content.strip()
       ] 

        return chunks


    def process(self):
        documents, errors = self.load_documents()
        chunks = self.split_documents(documents)

        return documents, chunks, errors
