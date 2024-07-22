# main.py

from scripts.convert import csv_to_parquet, json_to_parquet
from scripts.validate import validate_file
from utils.file_utils import create_output_dir, get_file_extension

def main():
    input_file = 'data/sample_data/sample.csv'
    output_file = 'data/output/sample.parquet'

    file_type = get_file_extension(input_file)
    if not validate_file(input_file, file_type):
        print("Invalid file.")
        return

    create_output_dir('data/output')

    if file_type == '.csv':
        csv_to_parquet(input_file, output_file)
    elif file_type == '.json':
        json_to_parquet(input_file, output_file)
    else:
        print("Unsupported file type.")

if __name__ == "__main__":
    main()
