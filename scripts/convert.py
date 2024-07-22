# scripts/convert.py

import pyarrow.csv as pv
import pyarrow.json as pj
import pyarrow.parquet as pq
import pandas as pd
import logging
from utils.file_utils import create_output_dir
from utils.logging_utils import setup_logging

setup_logging()

def csv_to_parquet(csv_file, parquet_file):
    logging.info(f"Converting {csv_file} to {parquet_file}")
    table = pv.read_csv(csv_file)
    pq.write_table(table, parquet_file)
    logging.info("Conversion complete.")

def json_to_parquet(json_file, parquet_file):
    logging.info(f"Converting {json_file} to {parquet_file}")
    table = pj.read_json(json_file)
    pq.write_table(table, parquet_file)
    logging.info("Conversion complete.")

# Add more conversion functions as needed

