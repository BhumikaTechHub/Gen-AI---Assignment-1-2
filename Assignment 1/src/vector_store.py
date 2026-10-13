
from pathlib import Path
import shutil

from langchain_community.vectorstores import FAISS, Chroma


class VectorStoreManager:
    def __init__(
        self,
        embeddings,
        store_type="faiss",
        persist_root="vector_store",
    ):
        self.embeddings = embeddings
        self.store_type = store_type.lower()
        self.persist_root = Path(persist_root)
        self.vector_store = None

        if self.store_type not in {"faiss", "chroma"}:
            raise ValueError("store_type must be 'faiss' or 'chroma'.")

        self.store_path = self.persist_root / self.store_type

    def build(self, chunks):
        if not chunks:
            raise ValueError("Cannot index an empty list of chunks.")

        self.persist_root.mkdir(parents=True, exist_ok=True)

        if self.store_type == "faiss":
            self.vector_store = FAISS.from_documents(
                chunks,
                self.embeddings,
            )

            self.vector_store.save_local(str(self.store_path))

        else:
            # Replace the existing Chroma index on an explicit rebuild.
            if self.store_path.exists():
                shutil.rmtree(self.store_path)

            self.vector_store = Chroma.from_documents(
                documents=chunks,
                embedding=self.embeddings,
                collection_name="technical_documents",
                persist_directory=str(self.store_path),
            )

        return self.vector_store

    def load(self):
        if not self.store_path.exists():
            raise FileNotFoundError(
                f"No saved {self.store_type} index at {self.store_path}. "
                "Build the index first."
            )

        if self.store_type == "faiss":
            self.vector_store = FAISS.load_local(
                str(self.store_path),
                self.embeddings,
                allow_dangerous_deserialization=False,
            )

        else:
            self.vector_store = Chroma(
                collection_name="technical_documents",
                embedding_function=self.embeddings,
                persist_directory=str(self.store_path),
            )

        return self.vector_store

    def get_vector_store(self):
        if self.vector_store is None:
            raise RuntimeError(
                "Vector store is not initialized. Build or load it first."
            )

        return self.vector_store
