import logging
import os
import sys
from mahabharat_rag.logger import LOG_FILE_PATH  # Ensure this import is correct

# Configure logger for exception handling
logger = logging.getLogger(__name__)

def error_message_detail(error: Exception, error_detail: sys) -> str:
    _, _, exc_tb = error_detail.exc_info()
    file_name: str = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]

    error_message: str = (
        f"Error occurred in script [{file_name}] at line [{exc_tb.tb_lineno}] - {str(error)}"
    )
    
    return error_message


class MahabharatXception(Exception):
    def __init__(self, error_message, error_detail):
        """
        Custom Exception class for Mahabharat RAG errors.
        Logs the error message when an exception occurs.
        """
        super().__init__(error_message)
        self.error_message: str = error_message_detail(
            error_message, error_detail=error_detail
        )

        # Log the error message
        logger.error(self.error_message)  # Logs error to file

    def __str__(self):
        return self.error_message
