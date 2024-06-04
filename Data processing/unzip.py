import os
import zipfile

root_path = "/Downloads/Dataset/2007"
directories = next(os.walk(root_path))[1]
print(directories)
for dir in directories:
    
    zip_folder_path = os.path.join(root_path,dir,'DESIGN')
    parent_folder_path = root_path  # will bve moved here
    zip_files = [f for f in os.listdir(zip_folder_path) if f.endswith('.ZIP')]
    for zip_file in zip_files:
        
        full_zip_file = os.path.join(zip_folder_path, zip_file)
        
        with zipfile.ZipFile(full_zip_file, 'r') as zip_ref:
            zip_ref.extractall(parent_folder_path)
        os.remove(full_zip_file)
print("All the files are Unzipped") 