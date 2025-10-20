
import os
import re

def update_image_paths(html_file_path):
    with open(html_file_path, 'r') as f:
        content = f.read()

    # Regex to find image sources (src attributes) in <img> tags
    # This regex looks for src="image_name.ext" where image_name.ext is not starting with a dot or slash
    # and is not an external URL (http/https)
    updated_content = re.sub(r'(<img[^>]*src=")(?!\./|/|https?://)([^" >]+)(")', r'\1../\2\3', content)

    # Also consider background-image in style attributes for CSS
    updated_content = re.sub(r'(url\([\'"]?)(?!\./|/|https?://)([^\)\'" >]+)([\'"]?\))', r'\1../\2\3', updated_content)

    if updated_content != content:
        with open(html_file_path, 'w') as f:
            f.write(updated_content)
        print(f"Updated image paths in {html_file_path}")
    else:
        print(f"No changes needed for {html_file_path}")


if __name__ == "__main__":
    html_files = []
    with open('./html_files.txt', 'r') as f:
        for line in f:
            html_files.append(line.strip())

    for html_file in html_files:
        # Construct the full path to the HTML file
        full_path = html_file
        update_image_paths(full_path)

