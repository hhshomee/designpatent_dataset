
import os
import shutil

root_path = "/Downloads/Dataset/2010"
directories = next(os.walk(root_path))[1]
print(directories,"dir")
for dir in directories:
        path = os.path.join(root_path, dir)
        sub_directories = next(os.walk(path))[1]
        for sub_dir in sub_directories:
                if sub_dir.endswith('SUPP'):
                        full_path = os.path.join(path,sub_dir)
                        print(full_path)
                        shutil.rmtree(full_path)
        

try:
    directories = next(os.walk(root_path))[1]
    print(directories,"dir")
    for dir in directories:
        path = os.path.join(root_path, dir)
        sub_directories = next(os.walk(path))[1]
        print(sub_directories,"sub")
        for sub_dir in sub_directories:
            sub_dir_path = os.path.join(path, sub_dir)
            sub_sub_directories=next(os.walk(sub_dir_path))[1]
            print(sub_sub_directories)
            for sub_sub_dir in sub_sub_directories:
                sub_sub_dir_path = os.path.join(sub_dir_path, sub_sub_dir)

                if sub_sub_dir.upper() != 'DESIGN':
                    shutil.rmtree(sub_sub_dir_path)
                    print(f"Deleted '{sub_sub_dir_path}'")
except Exception as e:
        print(f"An error occurred: {e}")
