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

#prompt
PROMPT_TEMPLATE = """
You are an expert in Mahabharat, the ancient Indian epic. 
Answer the user's question using the provided context. 
If the context does not contain relevant information, respond with "The provided context does not contain an answer.
Context:{context}
Question:{question}
Answer:
"""

#model
MODEL_NAME = "gemini-1.5-flash"
TEMPERATURE = 0.4
KEY = "GEMINI_API_KEY"

#RetrievalQA
CHAIN_TYPE = "stuff"
RETURN_SOURCE_DOCUMENT=True
VERBOSE = False
