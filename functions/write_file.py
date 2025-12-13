import os
def write_file(working_directory, file_path, content):

    working_dir_abs = os.path.abspath(working_directory)
    file_abs = os.path.abspath(os.path.join(working_dir_abs,file_path))

    if not file_abs.startswith(working_dir_abs):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'   
    
    if not os.path.exists(file_abs):
        try:
            os.makedirs(os.path.dirname(file_abs),exist_ok=True)
        except Exception as e:   
            return f"Error: Cannot create directory: {e}"
    if os.path.exists(file_abs) and os.path.isdir(file_abs):
        return f'Error: "{file_path}" is a directory, not a file'
    
    try:
        with open(file_abs, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written'

    except Exception as e:
        return f"Error: Cannot write to file: {e}"