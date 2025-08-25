import os
from pillow_heif import register_heif_opener
from PIL import Image

register_heif_opener()

RECYCLE_BIN_DIRNAME = 'HEIC_files_recycle_bin'


def save_heic_to_jpg(heic_file_path):
    image = Image.open(heic_file_path)
    file_root, ext = os.path.splitext(heic_file_path)
    jpg_file_path = file_root + '.JPG'
    image.save(jpg_file_path, "jpeg")
    print (f'.JPG file created: {jpg_file_path}')

    return jpg_file_path

def walkthrough_directory(dir_path, heic_files_found = []):
    # TODO: skip recycle_bin paths in here somewhere
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if file.upper().endswith(".HEIC"):
                full_file_path = os.path.join(root, file)
                heic_files_found.append(full_file_path)
                print (f'.HEIC file found: {full_file_path}')
        for dir in dirs:
            if os.path.basename(dir) != (RECYCLE_BIN_DIRNAME):
                walkthrough_directory(dir)

    return heic_files_found
