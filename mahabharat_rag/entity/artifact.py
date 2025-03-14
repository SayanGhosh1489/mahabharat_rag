import os
from dataclasses import dataclass
from typing import List
from langchain.schema import Document

@dataclass  
class dataloaderArtifacts:
    """
    Data loader class save the splited data
    """
    data_list: List[Document]

@dataclass
class embeddingloaderArtifacts:
    """
    Embedding loader class to load embeddings from a given path
    """
    embedding_file_path: str