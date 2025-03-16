import os
from dataclasses import dataclass
from typing import List
from langchain.schema import Document
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

@dataclass  
class dataloaderArtifacts:
    """
    Data loader class save the splited data
    """
    data_list: List[Document]

@dataclass
class embeddingArtifact:
    """
    Data loader class accept HuggingFace embedding
    """
    embed_model: HuggingFaceEmbeddings


@dataclass
class databaseCreatorArtifacts:
    """
    Embedding loader class to load embeddings from a given path
    """
    database_file_path: str

@dataclass
class RetriverArtifact:
    """
    Embedding loader class to load embeddings from a given path
    """
    retriver: FAISS