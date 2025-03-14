import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format= '[%(asctime)s]: %(message)s:')

list_of_files = [
    "mahabharat_rag/constants/__init__.py",
    "mahabharat_rag/components/__init__.py",
    "mahabharat_rag/components/documnent_loader.py",
    "mahabharat_rag/components/retriver.py",
    "mahabharat_rag/components/embedding.py",
    "mahabharat_rag/components/prompt.py",
    "mahabharat_rag/components/generator.py",
    "mahabharat_rag/entity/__init__.py",
    "mahabharat_rag/entity/config.py",
    "mahabharat_rag/entity/artifact.py",
    "mahabharat_rag/pipeline/__init__.py",
    "mahabharat_rag/pipeline/pipeline.py",
    "mahabharat_rag/data/raw/text.txt",
    "mahabharat_rag/data/embedded/text.txt",
    "mahabharat_rag/Notebooks/experiment.ipynb",
    "mahabharat_rag/logger.py"
]

def file_creator(list_of_files):
    for file in list_of_files:
        filepath = Path(file)
        filedir, filename = os.path.split(filepath)

        if filedir:
            os.makedirs(filedir, exist_ok=True)
            logging.info(f"Creating directory; {filedir} for the file {filename}")

        if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
            with open(filepath, 'w') as f:
                pass
                logging.info(f"Creating empty file: {filepath}")

        else:
            logging.info(f"{filename} is already created")

    logging.info("All files are created successfully")

if __name__ == "__main__":
    file_creator(list_of_files)
