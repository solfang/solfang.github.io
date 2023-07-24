import os

def list_folder_structure(folder_path, file_output=None):
    for root, dirs, files in os.walk(folder_path):
        folder_name = os.path.relpath(root, folder_path)
        folder_indent = "  " * (folder_name.count(os.sep) - 1)
        print(f"{folder_indent}- {folder_name}", file=file_output)
        
        if folder_name.count(os.sep) < 2:
            for dir_name in dirs:
                dir_indent = "  " * folder_name.count(os.sep)
                print(f"{dir_indent}- {dir_name}", file=file_output)
            
            for file_name in files:
                file_indent = "  " * folder_name.count(os.sep)
                print(f"{file_indent}- {file_name}", file=file_output)

# Get the current directory
current_directory = os.getcwd()

# Specify the output file path
output_file_path = os.path.join(current_directory, "output.txt")

# Open the output file in write mode
with open(output_file_path, "w") as output_file:
    # Call the function to list the folder structure and pass the output file as an argument
    list_folder_structure(current_directory, file_output=output_file)
