import sys, os
from langchain_community.vectorstores import FAISS
from mahabharat_rag.entity.config import databaseCreatorConfig
from mahabharat_rag.entity.artifact import dataloaderArtifacts,embeddingArtifact, databaseCreatorArtifacts
from mahabharat_rag.logger import logging
from mahabharat_rag.exception import MahabharatXception


class DatabaseCreator:
    def __init__(self, database_creator_config: databaseCreatorConfig,
                 data_loader_artifact: dataloaderArtifacts,
                 embedding_artifact: embeddingArtifact):

        self.database_creator_config = database_creator_config
        self.data_loader_artifact = data_loader_artifact
        self.embedding_artifact = embedding_artifact
        self.vector_store = None  # Placeholder for the FAISS vector store

    def initiate_database_creator(self) -> databaseCreatorArtifacts:
        """
        Creates a FAISS vector store from documents and saves it.
        """
        try:
            # Ensure the database output directory exists (FIXED)
            os.makedirs(self.database_creator_config.database_output, exist_ok=True)

            logging.info(f"Creating FAISS vector store at: {self.database_creator_config.database_output}")

            # Create FAISS index
            self.vector_store = FAISS.from_documents(
                self.data_loader_artifact.data_list,
                self.embedding_artifact.embed_model,
            )

            # Save FAISS index
            self.vector_store.save_local(self.database_creator_config.database_output)

            database_artifact = databaseCreatorArtifacts(
                database_file_path=self.database_creator_config.database_output
            )

            logging.info("Successfully created and stored FAISS embeddings.")
            return database_artifact

        except Exception as e:
            logging.error(f"Error in initiate_database_creator: {str(e)}", exc_info=True)
            raise MahabharatXception(e, sys)

