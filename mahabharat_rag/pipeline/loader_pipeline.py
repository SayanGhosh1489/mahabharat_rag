import sys
import os

from mahabharat_rag.components.documnent_loader import DocumentLoder
from mahabharat_rag.components.embedding import Embedding
from mahabharat_rag.components.database_creator import DatabaseCreator

from mahabharat_rag.entity.config import (dataLoaderConfig,
                                          embeddingConfig,
                                          databaseCreatorConfig)

from mahabharat_rag.entity.artifact import (dataloaderArtifacts,
                                            databaseCreatorArtifacts,
                                            embeddingArtifact)

from mahabharat_rag.logger import logging
from mahabharat_rag.exception import MahabharatXception

class LoaderpipeLine:
    def __init__(self):
        self.data_loader_config = dataLoaderConfig()
        self.embedding_config = embeddingConfig()
        self.database_creator_config = databaseCreatorConfig()
    
    def start_data_loader(self):
        logging.info("Starting start_data_loader method of LoaderpipeLine class")
        try:
            document_loader = DocumentLoder(self.data_loader_config)
            data_loader_artifact = document_loader.initiate_document_loader()
            logging.info("Exited the start_data_loader method of LoaderpipeLine class")
            
            # print(data_loader_artifact.data_list[0])
            return data_loader_artifact
        except Exception as e:
            MahabharatXception(e,sys)
    
    def start_get_embedding(self):
        logging.info("Starting start_get_embedding method of LoaderpipeLine")

        try:
            embedding = Embedding(self.embedding_config)
            embedding_artifact = embedding.initiate_get_embedding()

            return embedding_artifact
        except Exception as e:
            MahabharatXception(e,sys)

    def start_database_creator(self,data_loader_artifact: dataloaderArtifacts,
                               embedding_artifact: embeddingArtifact)->databaseCreatorArtifacts:
        logging.info("Starting start_database_creator method of LoaderpipeLine class")
        try:
            db = DatabaseCreator(data_loader_artifact= data_loader_artifact,
                                 embedding_artifact=embedding_artifact,
                                 database_creator_config=self.database_creator_config)
            
            database_creator_artifact:databaseCreatorArtifacts = db.initiate_database_creator()

            logging.info("Exited the start_embedding method of LoaderpipeLine class")
            return database_creator_artifact
        
        except Exception as e:
            MahabharatXception(e,sys)

    def run_pipeline(self):
        logging.info("Entered the run_pipeline method of LoaderpipeLine class")

        try:
            data_loader_artifact = self.start_data_loader()
            embedding_artifact = self.start_get_embedding()
            database_creator_artifact = self.start_database_creator(data_loader_artifact=data_loader_artifact,
                                                                    embedding_artifact=embedding_artifact)
            
            logging.info("Exited run_pipeline method of LoaderpipeLine class")

        except Exception as e:
            MahabharatXception(e,sys)

