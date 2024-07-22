# utils/file_utils.py

import os

def create_output_dir(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

def get_file_extension(file_path):
    return os.path.splitext(file_path)[-1].lower()
