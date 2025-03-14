import sys, os
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from mahabharat_rag.entity.config import embeddingConfig
from mahabharat_rag.entity.artifact import (dataloaderArtifacts,
                                            embeddingloaderArtifacts)
from mahabharat_rag.logger import logging
from mahabharat_rag.exception import MahabharatXception

class Embedding:
    def __init__(self,
                 data_loader_artifact:dataloaderArtifacts,
                 embedding_config:embeddingConfig):
        self.data_loader_artifact = data_loader_artifact
        self.embedding_config = embedding_config
        self.embedding = HuggingFaceEmbeddings(
                model_name=self.embedding_config.embedding_model
            )
        
        self.vector_store = None

    
    def initiate_faiss_embedding(self) -> embeddingloaderArtifacts:
        logging.info("Initiating initiate_faiss_embedding module of Embedding class")
        try:
            os.makedirs(self.embedding_config.embedding_dir, exist_ok=True)
            self.vector_store = FAISS.from_documents(
                self.data_loader_artifact.data_list,
                self.embedding,
            )
            self.vector_store.save_local(self.embedding_config.embedding_output)
            embedding_artifact: embeddingloaderArtifacts = embeddingloaderArtifacts(
                embedding_file_path=self.embedding_config.embedding_output
            )

            logging.info(
                "Exited the initiate_faiss_embedding method of Embedding class"
            )
            return embedding_artifact
        except Exception as e:
            MahabharatXception(e,sys)

    def get_retriver(self,embedding_artifact:embeddingloaderArtifacts):
        logging.info("Initiating get_retriver module of Embedding class")
        try:
            self.vector_store = FAISS.load_local(embedding_artifact.embedding_file_path,
                                                 embeddings=self.embedding,
                                                 allow_dangerous_deserialization=self.embedding_config.allow_dangerous_deserialization
                                                 )
            return self.vector_store.as_retriever(
                search_type= self.embedding_config.search_term, 
                search_kwargs=self.embedding_config.search_kwargs
            )
        except Exception as e:
            MahabharatXception(e,sys)