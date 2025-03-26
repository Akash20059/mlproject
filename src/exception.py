import sys
import logging

# Configure logging
logging.basicConfig(
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s ",
    level=logging.INFO
)

def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()  # ✅ Correct usage of exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in the Python script [{0}] at line [{1}]: {2}".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message  # ✅ Correct return statement

class CustomException(Exception):
    def __init__(self, error, error_detail: sys):
        super().__init__(str(error))  # ✅ Pass string representation of error
        self.error_message = error_message_detail(error, error_detail=error_detail)

    def __str__(self):
        return self.error_message

