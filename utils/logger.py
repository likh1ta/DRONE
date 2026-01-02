import logging

def setup_logger(log_file, level):
    logging.basicConfig(filename=log_file, level=getattr(logging, level),
                        format='%(asctime)s - %(levelname)s - %(message)s')
    return logging.getLogger()
