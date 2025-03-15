import sys
import os

from mahabharat_rag.components.documnent_loader import DocumentLoder
from mahabharat_rag.components.embedding import Embedding

from mahabharat_rag.entity.config import (dataLoaderConfig,
                                            embeddingConfig)

from mahabharat_rag.entity.artifact import (dataloaderArtifacts,
                                            embeddingloaderArtifacts)

from mahabharat_rag.logger import logging
from mahabharat_rag.exception import MahabharatXception

class pipeLine:
    def __init__(self):
        self.data_loader_config = dataLoaderConfig()
        self.embedding_config = embeddingConfig()
    
    def start_data_loader(self):
        logging.info("Starting start_data_loader method of pipeline class")
        try:
            document_loader = DocumentLoder(self.data_loader_config)
            data_loader_artifact = document_loader.initiate_document_loader()
            logging.info("Exited the start_data_loader method of pipeline class")
            
            # print(data_loader_artifact.data_list[0])
            return data_loader_artifact
        except Exception as e:
            MahabharatXception(e,sys)

    def start_embedding(self,data_loader_artifact: dataloaderArtifacts):
        logging.info("Starting start_embedding method of pipeline class")
        try:
            embedding = Embedding(data_loader_artifact=data_loader_artifact, 
                                  embedding_config=self.embedding_config)
            embedding_artifact = embedding.initiate_faiss_embedding()
            logging.info("Exited the start_embedding method of pipeline class")
            return embedding_artifact
        except Exception as e:
            MahabharatXception(e,sys)

    def run_pipeline(self):
        logging.info("Entered the run_pipeline method of TrainPipeline class")

        try:
            data_loader_artifact = self.start_data_loader()
            embedding_artifact = self.start_embedding(data_loader_artifact)

        except Exception as e:
            MahabharatXception(e,sys)

