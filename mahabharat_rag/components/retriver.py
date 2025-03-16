import sys
import os
from pathlib import Path
from langchain_community.vectorstores import FAISS
from mahabharat_rag.entity.config import retrieverConfig
from mahabharat_rag.entity.artifact import embeddingArtifact,RetriverArtifact
from mahabharat_rag.logger import logging
from mahabharat_rag.exception import MahabharatXception

class Retiver:
    def __init__(self,retriver_config: retrieverConfig):
        
        self.retriver_config = retriver_config
    
    def _get_latest_database(self):
        """
        Finds the latest timestamped folder from database folder and returns its path.

        Args:
            base_path (str): The base directory where timestamped folders are stored.

        Returns:
            str: The path of the latest timestamped folder, or None if no valid folder is found.
        """
        logging.info("Initiating _get_latest_database method from retriver class")
        try:
            db_dir_path = Path(self.retriver_config.database_dir)
            if not db_dir_path.exists() or not db_dir_path.is_dir():
                return None
            folders = [f for f in db_dir_path.iterdir() if f.is_dir() and f.name.isdigit()]

            if not folders:
                return None
            
            latest_folder = max(folders,key=lambda f: f.name)

            logging.info("Exiting _get_latest_database method from retriver class")
            logging.info(f"Latest dabase location: {(latest_folder.resolve())}")
            return str(latest_folder.resolve())
        
        except Exception as e:
            raise MahabharatXception(e,sys)

    
    def initiate_get_retriever(self,embedding_artifact: embeddingArtifact)->RetriverArtifact:
        """
        Loads the FAISS index and returns it as a retriever.

        Args:
            embedding_artifact (embeddingloaderArtifacts): Artifact containing embedding model
    

        Returns:
            FAISS retriever object.
        """
        logging.info("Initiating initiate_get_retriever method from Retriver class")

        db_path = self._get_latest_database()

        try:
            self.vector_store = FAISS.load_local(
                db_path,
                embeddings= embedding_artifact.embed_model, 
                allow_dangerous_deserialization=self.retriver_config.allow_dangerous_deserialization
            )

            retriever = self.vector_store.as_retriever(
                search_type=self.retriver_config.search_term,
                search_kwargs=self.retriver_config.search_kwargs
            )

            retriver_artifact: RetriverArtifact = RetriverArtifact(
                retriver=retriever
            )

            logging.info("Exiting initiate_get_retriever method from Retriver class")
            return retriver_artifact

        except Exception as e:
            raise MahabharatXception(e, sys)
