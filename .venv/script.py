import os

#current_directory_name = os.path.basename(os.getcwd())
#print(current_directory_name)

#files = [f for f in os.listdir('e:/hidden/.venv/') if os.path.isfile(os.path.join('e:/hidden/.venv/', f))]
#print(files)

import os

directory_path = 'e:/hidden/.venv'
file_name = 'script2.py'  # Change this to the file you want to hide
file_to_hide = os.path.join(directory_path, file_name)

# Check if the file exists
if os.path.exists(file_to_hide):
    # Hide the file using the Windows 'attrib' command
    os.system(f'attrib +h "{file_to_hide}"')
    print(f"File '{file_to_hide}' is now hidden.")
else:
    print(f"Error: The file '{file_to_hide}' does not exist.....dfgdfgdfg")
