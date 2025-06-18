# write_file

import os

def write_file(working_directory, file_path, content):
    absolute_dir = os.path.abspath(working_directory)
    absolute_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not absolute_path.startswith(absolute_dir):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(absolute_path):
        try:
            os.makedirs(os.path.dirname(absolute_path), exist_ok=True)
        except Exception as e:
            return f"Error: creating directory: {e}"
    if os.path.exists(absolute_path) and os.path.isdir(absolute_path):
        return f'Error: "{file_path}" is a directory, not a file'
    try:
        with open(absolute_path, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error writing to file: {e}"
    