import os
from dataclasses import dataclass


class dataloaderArtifacts:
    """
    Data loader class save the splited data
    """
    data_list: list

@dataclass
class embeddingloaderArtifacts:
    """
    Embedding loader class to load embeddings from a given path
    """
    embedding_file_path: str