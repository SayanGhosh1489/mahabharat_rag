import os
import sys
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from mahabharat_rag.entity.config import modelConfig
from mahabharat_rag.entity.artifact import modelArtifact
from mahabharat_rag.logger import logging
from mahabharat_rag.exception import MahabharatXception

class ModelGeter:
    def __init__(self, model_config: modelConfig):
        self.model_config = model_config

    def _get_authorization(self):
        load_dotenv()
        return os.getenv(self.model_config.key)

    def initiate_model_geter(self):

        logging.info("Starting initiate_model_geter method of ModelGeter class")
        
        try:
            llm_model = ChatGoogleGenerativeAI(
                model=self.model_config.model_name,
                api_key= self._get_authorization(),
                **self.model_config.model_kwarg 
            )
            logging.info("Exiting initiate_model_geter method of ModelGeter class")
            return modelArtifact(model=llm_model)
        
        except Exception as e:
            raise MahabharatXception(e, sys)
