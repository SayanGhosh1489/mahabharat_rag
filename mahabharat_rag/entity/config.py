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