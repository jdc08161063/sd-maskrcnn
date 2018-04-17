import os
import logging


def mkdir_if_missing(output_dir):
    if not os.path.exists(output_dir):
        try:
            os.makedirs(output_dir)
        except:
            logging.error("Something went wrong in mkdir_if_missing. "
                          "Probably some other process created the directory already.")