from langchain.document_loaders import DirectoryLoader,PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from mahabharat_rag.entity.config import dataLoaderConfig
from mahabharat_rag.entity.artifact import dataloaderArtifacts
from mahabharat_rag.logger import logging

class DocumentLoder:
    def __init__(self,data_loader_config:dataLoaderConfig):
        self.data_loader_config = data_loader_config
        self.data_loader = DirectoryLoader(self.data_loader_config.data_file_path,
                                           glob=data_loader_config.glob,
                                           loader_cls=PyPDFLoader)
        
        self.text_splitter = RecursiveCharacterTextSplitter(chunk_size=self.data_loader_config.chunk_size,
                                                            chunk_overlap=self.data_loader_config.chunk_overlap)

    def initiate_document_loader(self) -> dataloaderArtifacts:
        logging.info("Initiating document loader")
        doc = self.data_loader.load()
        data_loader_artifact: dataloaderArtifacts = dataloaderArtifacts(
            self.text_splitter.split_documents(doc)
        )

        return data_loader_artifact



