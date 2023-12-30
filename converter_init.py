import time
from converter_logic import *

# pandas, spark, parquet, pyarrow, csv, json, excel, mysql, impala
# sqlite, postgresql, redshift, bigquery, snowflake, oracle, Hbase
# Kudu, HDFS, GCS, s3, azure, azure_synapse, teradata, mongodb, dremio, oracledb
def get_input_fromat():
    formats = ["csv", "json", "parquet", "excel"]
    print("Enter input format:")
    for f in formats:
        print(f)
    format_choice = input("Enter format: ")
    if format_choice not in formats:
        raise ValueError("Invalid format")
    return format_choice


def get_output_format():
    formats = ["csv", "json", "parquet", "excel"]
    print("Enter output format:")
    for f in formats:
        print(f)
    format_choice = input("Enter format: ")
    if format_choice not in formats:
        raise ValueError("Invalid format")
    return format_choice


def main():
    input_file = input("Enter the path of the input file: ")
    input_format = get_input_fromat()
    output_file = input("Enter the path of the output file: ")
    output_format = get_output_format()
    start_time = time.time()


    if input_format == "csv":   
        arrow_table = read_csv_to_arrow(input_file)
    elif input_format == "json":
        arrow_table = read_json_to_arrow(input_file)
    elif input_format == "parquet":
        arrow_table = read_parquet_to_arrow(input_file)
    elif input_format == "excel":
        arrow_table = read_excel_to_arrow(input_file)
    else:
        raise ValueError("Invalid input format")
    
    table_size  = calculate_table_size(arrow_table)
    print(f"Data size: {table_size / 1024 / 1024:.2f} MB")

    if output_format == "csv":
        arrow_table.to_pandas().to_csv(output_file, index=False)
    elif output_format == "json":
        arrow_table.to_pandas().to_json(output_file, orient="records", lines=True)
    elif output_format == "parquet":
        pq.write_table(arrow_table, output_file)
    elif output_format == "excel":
        write_arrow_to_excel(arrow_table, output_file)
    else:
        raise ValueError("Invalid output format")
    
    end_time = time.time()
    duration = end_time - start_time
    print(f"Conversion completed in {duration:.2f} seconds")


if __name__ == "__main__":
    main()
    




