from datetime  import datetime
import os

#dataloader
RAW_DATA_PATH = r"mahabharat_rag\data"
GLOBE = '*.pdf'

TIMESTAMP = datetime.now().strftime('%Y%m%d%H%M%S')

MODEL_NAME = "gemini-2.0-flash"
EMBEDDING_MODEL = 'sentence-transformers/all-MiniLM-L6-v2'
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 100

#embedding
SEARCH_TERM = "similarity"
SEARCH_KWARG = {"k": 6}
ALLOW_DANGEROUS_DESERIALIZATION = True

# Paths for storing artifacts
ARTIFACT_PATH = "artifact"
