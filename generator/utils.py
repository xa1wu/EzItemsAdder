# generator/utils.py

import os

def get_image_files(folder_path, extensions=(".png", ".jpg", ".jpeg", ".webp")):
    return [
        os.path.splitext(f)[0]
        for f in os.listdir(folder_path)
        if os.path.isfile(os.path.join(folder_path, f)) and f.lower().endswith(extensions)
    ]
