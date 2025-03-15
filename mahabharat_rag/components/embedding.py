import sys
import os
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from mahabharat_rag.entity.config import embeddingConfig
from mahabharat_rag.entity.artifact import dataloaderArtifacts, embeddingloaderArtifacts
from mahabharat_rag.logger import logging
from mahabharat_rag.exception import MahabharatXception


class Embedding:
    def __init__(self, data_loader_artifact: dataloaderArtifacts, embedding_config: embeddingConfig):
        """
        Initialize the Embedding class with data artifacts and embedding configuration.

        Args:
            data_loader_artifact (dataloaderArtifacts): The data artifacts containing document list.
            embedding_config (embeddingConfig): The embedding configuration.
        """
        self.data_loader_artifact = data_loader_artifact
        self.embedding_config = embedding_config
        self.vector_store = None  # Placeholder for the FAISS vector store

    def get_embedding(self):
        """
        Returns the HuggingFace Embeddings object.
        
        Returns:
            HuggingFaceEmbeddings: The HuggingFace Embeddings object.
        """
        logging.info("Initializing HuggingFace Embeddings...")

        try:
            embedding = HuggingFaceEmbeddings(
                model_name=self.embedding_config.embedding_model
            )

            return embedding
        
        except Exception as e:
            raise MahabharatXception(e, sys)

    def initiate_faiss_embedding(self) -> embeddingloaderArtifacts:
        """
        Creates a FAISS vector store from documents and saves it.

        Returns:
            embeddingloaderArtifacts: Artifact containing the path to the stored FAISS index.
        """
        logging.info("Initiating FAISS embedding process...")
        
        embedding = self.get_embedding()

        try:
            # Ensure the artifact directory exists
            os.makedirs(self.embedding_config.embedding_output, exist_ok=True)

            logging.info(f"Creating FAISS vector store at: {self.embedding_config.embedding_output}")

            # Create FAISS index
            self.vector_store = FAISS.from_documents(
                self.data_loader_artifact.data_list,
                embedding,
            )

            # Save FAISS index
            self.vector_store.save_local(self.embedding_config.embedding_output)

            embedding_artifact = embeddingloaderArtifacts(
                embedding_file_path=self.embedding_config.embedding_output
            )

            logging.info("Successfully created and stored FAISS embeddings.")
            return embedding_artifact

        except Exception as e:
            logging.error(f"Error in initiate_faiss_embedding: {str(e)}", exc_info=True)
            raise MahabharatXception(e, sys)

    