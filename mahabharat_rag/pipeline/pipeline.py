import sys
import os

from mahabharat_rag.components.documnent_loader import DocumentLoder
from mahabharat_rag.entity.config import dataLoaderConfig
from mahabharat_rag.entity.artifact import dataloaderArtifacts

from mahabharat_rag.logger import logging
from mahabharat_rag.exception import MahabharatXception

class pipeLine:
    def __init__(self):
        self.data_loader_config = dataLoaderConfig()
    
    def start_data_loader(self):
        logging.info("Starting start_data_loader method of pipeline class")
        try:
            document_loader = DocumentLoder(self.data_loader_config)
            data_loader_artifact = document_loader.initiate_document_loader()
            logging.info("Exited the start_data_loader method of pipeline class")
            return dataloaderArtifacts(data_list = data_loader_artifact)
        except Exception as e:
            MahabharatXception(e,sys)


    def run_pipeline(self):
        logging.info("Entered the run_pipeline method of TrainPipeline class")

        try:
            data_loader_artifact = self.start_data_loader()

        except Exception as e:
            MahabharatXception(e,sys)

