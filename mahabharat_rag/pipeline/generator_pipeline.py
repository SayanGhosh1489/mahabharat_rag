import os, sys
from mahabharat_rag.components.retriver import Retiver
from mahabharat_rag.components.prompt import PromptCreator
from mahabharat_rag.components.model import ModelGeter
from mahabharat_rag.components.generator import Generator

from mahabharat_rag.entity.config import (retrieverConfig,
                                          promptConfig,
                                          modelConfig,
                                          RetrievalQAConfig)

from mahabharat_rag.entity.artifact import (RetriverArtifact,
                                            promptArtifact,
                                            modelArtifact,
                                            RetrievalQAAritfact)
from mahabharat_rag.logger import logging
from mahabharat_rag.exception import MahabharatXception

class GeneratorPipeline:
    def __init__(self):
        self.retriver_config = retrieverConfig()
        self.prompt_config = promptConfig()
        self.model_config = modelConfig()
        self.retrievalqa_config = RetrievalQAConfig()

    def start_initiate_retriver(self,embedding_artifact)->RetriverArtifact:
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

            retriver_artifact = retriver.initiate_get_retriever(embedding_artifact = embedding_artifact)

            logging.info("Exiting start initiate retricer method of GeneratorPipeline class")
            return retriver_artifact
        
        except Exception as e:
            raise MahabharatXception(e,sys)
    
    def start_initiate_prompt_creator(self)->promptArtifact:
        """
        initiate the PromptCreator class from Retriver

        Args: 
            None

        Return:
            Prompt Templapte artifact
        """
        logging.info("Initiate start initiate prompt creator method of GeneratorPipeline class ")

        try:
            prompt = PromptCreator(self.prompt_config)

            prompt_artifact = prompt.initiate_prompt_creator()

            logging.info("Exiting start initiate prompt creator method of GeneratorPipeline class ")

            return prompt_artifact
        except Exception as e:
            raise MahabharatXception(e,sys)
        
    def start_inititate_model_geter(self)->modelArtifact:
        """
        initiate the ModelGeter class from Model

        Args: 
            None

        Return:
            model artifact
        """

        logging.info("Initiate start initiate model geter method of GeneratorPipeline class ")

        try:
            model = ModelGeter(self.model_config)
            model_artifact = model.initiate_model_geter()
            logging.info("Exiting start initiate model geter method of GeneratorPipeline class ")

            return model_artifact

        except Exception as e:
            raise MahabharatXception(e,sys)
        
    def start_initiate_retrievalqa(self,prompt_artifact: promptArtifact,
                          model_artifact: modelArtifact,
                          retriver_artifact: RetriverArtifact)->RetrievalQAAritfact:
        """
        initiate the initiate_retrievalqa Method from class Generator

        Args: 
            prompt artifact
            model artifact
            retriver db artifact

        Return:
            retrieval qa artifact
        """

        logging.info("Initiate start_initiate_retrievalqa method of GeneratorPipeline class ")

        try:
            qa = Generator(model_artifact=model_artifact,
                           prompt_artifact=prompt_artifact,
                           retrievalqa_config = self.retrievalqa_config,
                           retrival_artifact= retriver_artifact)
            
            retrievalqa_artifact = qa.initiate_retrievalqa()

            
            logging.info("Exiting Initiate start_initiate_retrievalqa method of GeneratorPipeline class ")

            return retrievalqa_artifact

        except Exception as e:
            raise MahabharatXception(e,sys)

    
    def run_pipeline(self,embedding_artifact):
        logging.info("Entered the run_pipeline method of GeneratorpipeLine class")
        
        retriver_artifact = self.start_initiate_retriver(embedding_artifact=embedding_artifact)
        prompt_artifact = self.start_initiate_prompt_creator()
        model_artifact = self.start_inititate_model_geter()

        retrievalqa_artifact = self.start_initiate_retrievalqa(model_artifact=model_artifact,
                                                               prompt_artifact=prompt_artifact,
                                                               retriver_artifact=retriver_artifact)
        
       

        logging.info("Exited run_pipeline method of GeneratorpipeLine class")

        return retrievalqa_artifact