# get_file_content

import os

def get_file_content(working_directory, file_path):
    absolute_path = os.path.abspath(working_directory)
    target_path = absolute_path
    if not target_path.startswith(absolute_path):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    target_path = os.path.join(absolute_path, file_path)
    if not os.path.isfile(target_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    try:
        MAX_CHARS = 10000
        with open(target_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            if len(file_content_string) == MAX_CHARS:
                file_content_string += f'[...File "{file_path}" truncated at 10000 characters]'
            return file_content_string
    except Exception as e:
        return f"Error: {e}"