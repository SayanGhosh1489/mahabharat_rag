import os
import sys
from mahabharat_rag.pipeline.generator_pipeline import GeneratorPipeline
from mahabharat_rag.components.embedding import Embedding
from mahabharat_rag.entity.config import embeddingConfig
from mahabharat_rag.logger import logging
from mahabharat_rag.exception import MahabharatXception
from langchain.chains import RetrievalQA

# Initialize embedding at the start to reduce runtime delay
###########################################
embedding_config = embeddingConfig()
embedding = Embedding(embedding_config=embedding_config)
embedding_artifact = embedding.initiate_get_embedding()
############################################

# Pipeline will run each time RetrievalQA is requested.
def start_generator_pipeline():
    logging.info("Starting the start_generator_pipeline pipeline")
    try:
        pipeline = GeneratorPipeline()
        qa = pipeline.run_pipeline(embedding_artifact=embedding_artifact)
        logging.info("Exited the Loader pipeline")
        return qa
    except Exception as e:
        raise MahabharatXception(e, sys)  # Fixed missing 'raise'

if __name__ == "__main__":
    qa_artifact = start_generator_pipeline()
    qa_staff = qa_artifact.retrivel

    question = "what is 2+2"

    response = qa_staff.invoke({'query': question})

    print(response['result'])
