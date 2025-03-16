import sys
from mahabharat_rag.pipeline.loader_pipeline import LoaderpipeLine
from mahabharat_rag.logger import logging
from mahabharat_rag.exception import MahabharatXception

def start_pipeline():
    logging.info("Starting the Loader pipeline")
    try:
        pipeline = LoaderpipeLine()
        pipeline.run_pipeline()
        logging.info("Exited the Loader pipeline")
    except Exception as e:
        MahabharatXception(e,sys)

if __name__ == "__main__":
    start_pipeline()