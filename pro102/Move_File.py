import os
import shutil

from_dir = "C:/Users/admin/Downloads"
to_dir = "C:/Users/admin/Desktop/documented_files"
list_of_files = os.listdir(from_dir)

valid_extensions = ['.txt', '.doc', '.docx', '.pdf']

path1 = from_dir

path2 = os.path.join(to_dir, "documented_files")

if not os.path.exists(path2):
    os.makedirs(path2)

for filename in list_of_files:
    name, extension = os.path.splitext(filename)
    
    if not extension:
        continue
    
    if extension in valid_extensions:
        full_path = os.path.join(path1, filename)
        
        path3 = os.path.join(path2, filename)
        
        if not os.path.exists(path3):
            shutil.move(full_path, path3)
            print(f"Moved: {filename} to {path3}")
        else:
            print(f"Destination path {path3} already exists for file {filename}. Skipping.")
    else:
        print(f"Invalid File: {filename}")
