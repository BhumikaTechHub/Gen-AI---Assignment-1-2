
import os

from langchain_huggingface import HuggingFaceEmbeddings


class EmbeddingManager:
    def __init__(self, model_name=None):
        self.model_name = (
            model_name
            or os.getenv(
                "EMBEDDING_MODEL",
                "sentence-transformers/all-MiniLM-L6-v2",
            )
        )

        self.embeddings = HuggingFaceEmbeddings(
            model_name=self.model_name,
            model_kwargs={"device": "cpu"},
            encode_kwargs={"normalize_embeddings": True},
        )

    def get_embeddings(self):
        return self.embeddings
