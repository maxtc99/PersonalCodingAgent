import os
from config import CONTENT_LIMIT
from google.genai import types

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description=f"Reads and returns the first {CONTENT_LIMIT} characters of the content from a specified file within the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file whose content should be read, relative to the working directory.",
            ),
        },
        required=["file_path"],
    ),
)


def get_file_content(working_directory, file_path):   
    working_dir_abs = os.path.abspath(working_directory)
    abs_file = os.path.abspath(os.path.join(working_dir_abs,file_path))
    if not abs_file.startswith(working_dir_abs):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'   
    if not os.path.isfile(abs_file):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    try:
        with open(abs_file, "r") as file:
            content = file.read(CONTENT_LIMIT) 
            limit_msg = f'[...File "{abs_file}" truncated at 10000 characters]'         
            if len(content) >= CONTENT_LIMIT:
                content += limit_msg                  
        return content
    except Exception as e:
        return f"Error: Cannot read file: {e}"