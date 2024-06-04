import os
import tarfile
path_to_folder = '/Downloads/Dataset/2021'

tar_files = [file for file in os.listdir(path_to_folder) if file.endswith('.tar')]

for tar_file in tar_files:
    tar_file_path = os.path.join(path_to_folder, tar_file)
    with tarfile.open(tar_file_path) as tar:
        extract_dir = os.path.splitext(tar_file_path)[0]
        # os.makedirs(extract_dir, exist_ok=True)  
        tar.extractall(path=extract_dir)
        
        print(f"Extracted {tar_file} into {extract_dir}")

print("Extraction o is complete.")
