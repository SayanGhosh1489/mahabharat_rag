import os, sys
from langchain.prompts import PromptTemplate
from mahabharat_rag.entity.config import promptConfig
from mahabharat_rag.entity.artifact import promptArtifact
from mahabharat_rag.logger import logging
from mahabharat_rag.exception import MahabharatXception


class PromptCreator:
    def __init__(self,prompt_config:promptConfig):
        self.prompt_config = prompt_config

    def initiate_prompt_creator(self)->promptArtifact:
        """
        Create a prompt template using PromptTemplate
        
        Return: prompt template artifact

        """
        logging.info("Starting initiate_prompt_creator method of PromptCreator")

        try:
            prompt = PromptTemplate(
                input_variables= ["question", "context"],
                template= self.prompt_config.prompt_template
            )

            prompt_artifact: promptArtifact = promptArtifact(
                prompt=prompt
            )

            logging.info("Exiting initiate_prompt_creator method of PromptCreator")

            return prompt_artifact
        
        except Exception as e:
            raise MahabharatXception(e,sys)