import sys
import os
from langchain_community.embeddings import HuggingFaceEmbeddings
from mahabharat_rag.entity.config import embeddingConfig
from mahabharat_rag.entity.artifact import embeddingArtifact
from mahabharat_rag.logger import logging
from mahabharat_rag.exception import MahabharatXception


class Embedding:
    def __init__(self, embedding_config: embeddingConfig):
        """
        Initialize the Embedding class with embedding configuration.
        """
        self.embedding_config = embedding_config

    def initiate_get_embedding(self) -> embeddingArtifact:
        """
        Returns the HuggingFace Embeddings object.
        """
        logging.info("Starting initiate_get_embedding method of Embedding class...")

        try:
            embedding = HuggingFaceEmbeddings(
                model_name=self.embedding_config.embedding_model
            )
            embedding_artifact: embeddingArtifact = embeddingArtifact(
                embed_model=embedding
            )
            logging.info("Exiting initiate_get_embedding of Embedding class")
            return embedding_artifact
        
        except Exception as e:
            raise MahabharatXception(e, sys)
