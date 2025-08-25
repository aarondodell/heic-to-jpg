from FileUtils import *
import os
import shutil

# main script
PARENT_DIR = input("Provide dir to scan: ")
RECYCLE_BIN_PATH = os.path.join(PARENT_DIR, 'HEIC_files_recycle_bin')

if not os.path.exists(PARENT_DIR):
    raise ValueError(PARENT_DIR, "not a legitimate path")

# find all files
heic_files_found = walkthrough_directory(PARENT_DIR)

# ask to create copies
should_create_copies = input(f'Found {len(heic_files_found)} .HEIC files. Create copies at each location? (y/n)')
if (should_create_copies == 'y'):
    for heic_file in heic_files_found:
        save_heic_to_jpg(heic_file)
else:
    exit()

# ask to move HEIC files to a new recycle bin
should_move_to_recycle_bin = input(f'Move the {len(heic_files_found)} .HEIC files to a new Recycle Bin folder? (y/n)')
if (should_move_to_recycle_bin == 'y'):
    if (not os.path.exists(RECYCLE_BIN_PATH)):
        os.makedirs(RECYCLE_BIN_PATH)
    for source_heic_file_path in heic_files_found:
        destination_heic_file_path = os.path.join(RECYCLE_BIN_PATH, os.path.basename(source_heic_file_path))
        shutil.move(source_heic_file_path, destination_heic_file_path)
    print(f'Moved {len(heic_files_found)} into `{RECYCLE_BIN_PATH}`')