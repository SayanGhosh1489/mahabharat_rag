import os
from dataclasses import dataclass
from mahabharat_rag.constants import *

@dataclass
class dataLoaderConfig:
    """
    Data loader class to load data from a given path
    """
    def __init__(self):
        self.data_file_path: str = os.path.join(RAW_DATA_PATH, "raw")
        self.chunk_size: int = CHUNK_SIZE
        self.chunk_overlap: int = CHUNK_OVERLAP
        self.glob: str = GLOBE

@dataclass
class embeddingConfig:
    """
    Embedding config class to prepare the embedding
    """
    def __init__(self):
        self.embedding_model: str = EMBEDDING_MODEL
        self.embedding_dir: str = os.path.join(ARTIFACT_PATH,TIMESTAMP)
        self.embedding_output: str =os.path.join(self.embedding_dir, f"embedding")
        self.search_term: str = SEARCH_TERM
        self.allow_dangerous_deserialization: bool = ALLOW_DANGEROUS_DESERIALIZATION
        self.search_kwargs: dict = SEARCH_KWARG