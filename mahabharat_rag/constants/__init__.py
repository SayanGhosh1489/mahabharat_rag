from datetime  import datetime
import os

#commmon
TIMESTAMP = datetime.now().strftime('%Y%m%d%H%M%S')
ARTIFACT_PATH = "artifact"
DATABASE_FOLDER_NAME = "DataBase"

#dataloader and spliter
RAW_DATA_PATH = r"mahabharat_rag\data"
GLOBE = '*.pdf'
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 100

#embedding
EMBEDDING_MODEL = 'sentence-transformers/all-MiniLM-L6-v2'


#retriver
SEARCH_TERM = "similarity"
SEARCH_KWARG = {"k": 6}
ALLOW_DANGEROUS_DESERIALIZATION = True

#generator
MODEL_NAME = "gemini-2.0-flash"
