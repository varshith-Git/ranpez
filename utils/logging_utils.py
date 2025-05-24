# utils/logging_utils.py

import logging
import time
import os
import json as ks

def setup_logging():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
