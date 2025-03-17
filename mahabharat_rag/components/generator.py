import sys
from langchain.chains import RetrievalQA
from mahabharat_rag.entity.config import RetrievalQAConfig
from mahabharat_rag.entity.artifact import (RetrievalQAAritfact,
                                            RetriverArtifact,
                                            modelArtifact,
                                            promptArtifact)

from mahabharat_rag.logger import logging
from mahabharat_rag.exception import MahabharatXception

class Generator:
    """
    Create retrievalQA object:

    Args:
        Retrievalqa Config
        Model Artifact
        Retrival database artifact
        Prompt Artifact

    """
    def __init__(self,retrievalqa_config: RetrievalQAConfig,
                 retrival_artifact: RetriverArtifact,
                 model_artifact: modelArtifact,
                 prompt_artifact:promptArtifact):
        
        self.retrieval_config = retrievalqa_config
        self.retrival_artifact = retrival_artifact
        self.model_artifact = model_artifact
        self.prompt_artifact = prompt_artifact

    def initiate_retrievalqa(self):
        """
        create retrievalQA object

        Retrun:
            RetrivalQA Artifact
        """

        logging.info("Starting initiate retrievalqa method from Generator class")

        try:
            qa = RetrievalQA.from_chain_type(
                llm=self.model_artifact.model,
                retriever = self.retrival_artifact.retriver,
                chain_type=self.retrieval_config.chian_type,
                verbose = self.retrieval_config.verbose,
                return_source_documents = self.retrieval_config.return_source_document,
                chain_type_kwargs={"prompt": self.prompt_artifact.prompt})
            
            logging.info("Starting initiate retrievalqa method from Generator class")
            return RetrievalQAAritfact(retrivel=qa)
        
        except Exception as e:
            raise MahabharatXception(e,sys)