import pandas as pd
import pyarrow as pa
import pyarrow.csv as pv
import pyarrow.json as pj
import pyarrow.parquet as pq


def read_csv_to_arrow(file_path):
    return pv.read_csv(file_path)


def read_json_to_arrow(file_path):
    return pj.read_json(file_path)


def read_parquet_to_arrow(file_path):
    return pq.read_table(file_path)


def read_excel_to_arrow(file_path):
    df = pd.read_excel(file_path)
    return pa.Table.from_pandas(df)


def read_arrow_to_excel(arrow_table, file_path):
    df = arrow_table.to_pandas()
    df.to_excel(file_path, index=False)


def calculate_table_size(arrow_table):
    total_size = 0
    for chunk in arrow_table.columns:
        for array in chunk.iterchunks():
            total_size += array.nbytes
    return total_size
