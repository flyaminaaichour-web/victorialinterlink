
import os
import re

def replace_string_in_file(file_path, old_string, new_string):
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        updated_content = content.replace(old_string, new_string)
        
        if updated_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            print(f"Updated {file_path}")
        # else:
        #     print(f"No changes needed for {file_path}")
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

if __name__ == "__main__":
    old_string = "BRGINV"
    new_string = "Victoria Interlink"
    
    files_to_process = []
    with open('./all_files.txt', 'r') as f:
        for line in f:
            file_path = line.strip()
            # Exclude files that are likely binary or part of git metadata
            if not file_path.startswith('./.git/') and \
               not file_path.endswith(('.png', '.jpg', '.ico', '.gif', '.bin', '.pyc', '.DS_Store')) and \
               not file_path.endswith(('.pack', '.idx')):
                files_to_process.append(file_path)

    for file_path in files_to_process:
        replace_string_in_file(file_path, old_string, new_string)

