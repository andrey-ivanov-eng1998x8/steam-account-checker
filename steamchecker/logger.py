import sys

def get_logger(name):
    import logging
    logger = logging.getLogger(name)
    if not logger.handlers:
        h = logging.StreamHandler(sys.stdout)
        h.setFormatter(logging.Formatter('%(asctime)s [%(levelname)s] %(message)s'))
        logger.addHandler(h)
        logger.setLevel(logging.INFO)
    return logger
