import os, sys
from mahabharat_rag.components.retriver import Retiver
from mahabharat_rag.entity.config import retrieverConfig
from mahabharat_rag.entity.artifact import embeddingArtifact,RetriverArtifact
from mahabharat_rag.logger import logging
from mahabharat_rag.exception import MahabharatXception

class GeneratorPipeline:
    def __init__(self):
        self.retriver_config = retrieverConfig()

    def start_initiate_retriver(self,embedding_artifact):
        """
        initiate the retriver artifact from Retriver class
        Args:
            embedding_artifact: Embedding model
        Returns:
            retriver_artifact: FAISS object loaded from local

        """
        logging.info("Initiate start initiate retriver method of GeneratorPipeline class")

        try:
            retriver = Retiver(retriver_config=self.retriver_config)

            retriver_artifact = retriver.initiate_get_retriever(embedding_artifact=embedding_artifact)

            logging.info("Exiting start initiate retricer method of GeneratorPipeline class")
            return retriver_artifact
        
        except Exception as e:
            raise MahabharatXception(e,sys)
    
    def run_pipeline(self,embedding_artifact):
        logging.info("Entered the run_pipeline method of GeneratorpipeLine class")
        
        retriver_artifact = self.start_initiate_retriver(embedding_artifact=embedding_artifact)

        logging.info("Exited run_pipeline method of LoaderpipeLine class")