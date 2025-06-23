# call_function

from google.genai import types

from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.run_python import run_python_file
from functions.write_file import write_file

def call_function(function_call_part, verbose=False):
    function_name = function_call_part.name
    function_arguments = function_call_part.args

    if verbose:
        print(f"Calling function: {function_name}({function_arguments})")
    else:
        print(f" - Calling function: {function_name}")

    function_call_part.args["working_directory"] = "./calculator"
    
    functions = {
        "get_files_info": get_files_info,
        "get_file_content": get_file_content,
        "run_python": run_python_file,
        "write_file": write_file
    }

    if function_name not in functions:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}"},
                )
            ],
        )
    
    function_result = functions[function_name](**function_arguments)

    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_name,
                response={"result": function_result},
            )
        ],
    )
