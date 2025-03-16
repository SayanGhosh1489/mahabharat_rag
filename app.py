import os, sys
from mahabharat_rag.pipeline.generator_pipeline import GeneratorPipeline
from mahabharat_rag.components.embedding import Embedding
from mahabharat_rag.entity.config import embeddingConfig
from mahabharat_rag.logger import logging
from mahabharat_rag.exception import MahabharatXception

embedding_config = embeddingConfig()

embedding = Embedding(embedding_config=embedding_config)
embedding_artifact = embedding.initiate_get_embedding()

def start_generator_pipeline():
    logging.info("Starting the start_generator_pipeline pipeline")
    try:
        pipeline = GeneratorPipeline()
        pipeline.run_pipeline(embedding_artifact=embedding_artifact)
        logging.info("Exited the Loader pipeline")
    except Exception as e:
        MahabharatXception(e,sys)

if __name__ == "__main__":
    start_generator_pipeline()
