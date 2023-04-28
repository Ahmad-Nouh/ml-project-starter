import sys
import logging


def error_message_details(error, error_details: sys):
    _, _, exc_tb = error_details.exc_info()
    
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno

    error_message = """
        Error occured in python script name [{0}].
        line number [{1}].
        error message [{2}].
    """.format(
        file_name,
        line_number,
        str(error)
    )

    return error_message


class CustomException(Exception):
    def __init__(self, message, details: sys):
        super().__init__(message)
        self.message = error_message_details(message, error_details=details)

    def __str__(self) -> str:
        return self.message
