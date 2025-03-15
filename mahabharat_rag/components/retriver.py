import sys
import os
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from mahabharat_rag.entity.config import retrieverConfig
from mahabharat_rag

def get_retriever(self, embedding_artifact: embeddingloaderArtifacts):
        """
        Loads the FAISS index and returns it as a retriever.

        Args:
            embedding_artifact (embeddingloaderArtifacts): Artifact containing FAISS index path.

        Returns:
            FAISS retriever object.
        """
        logging.info("Loading FAISS retriever...")

        try:
            self.vector_store = FAISS.load_local(
                embedding_artifact.embedding_file_path,
                embeddings=self.embedding,
                allow_dangerous_deserialization=self.embedding_config.allow_dangerous_deserialization
            )

            retriever = self.vector_store.as_retriever(
                search_type=self.embedding_config.search_term,
                search_kwargs=self.embedding_config.search_kwargs
            )

            logging.info("Successfully loaded FAISS retriever.")
            return retriever

        except Exception as e:
            logging.error(f"Error in get_retriever: {str(e)}", exc_info=True)
            raise MahabharatXception(e, sys)
