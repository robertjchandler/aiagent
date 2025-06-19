# run_python.py

import os, subprocess

def run_python_file(working_directory, file_path):
    absolute_dir = os.path.abspath(working_directory)
    absolute_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not absolute_path.startswith(absolute_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(absolute_path):
        return f'Error: File "{file_path}" not found.'
    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    try:
        result = subprocess.run(absolute_path, capture_output=True, timeout=30)
        print(f"STDOUT:", result.stdout)
        print(f"STDERR:", result.stderr)
        if result.returncode != 0:
            print(f"Process exited with code {result.returncode}")
        if result == None:
            print("No output produced")
    except Exception as e:
        return f"Error: executing Python file: {e}"
