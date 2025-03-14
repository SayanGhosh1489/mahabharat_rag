import sys
from mahabharat_rag.pipeline.pipeline import pipeLine
from mahabharat_rag.logger import logging
from mahabharat_rag.exception import MahabharatXception

def start_pipeline():
    logging.info("Starting the pipeline")
    try:
        pipeline = pipeLine()
        pipeline.run_pipeline()
        logging.info("Exited the pipeline")
    except Exception as e:
        MahabharatXception(e,sys)

if __name__ == "__main__":
    start_pipeline()