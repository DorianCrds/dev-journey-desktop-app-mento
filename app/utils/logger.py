# app/utils/logger.py
import logging


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(filename)s - %(message)s')
logger = logging.getLogger()