from FileUtils import *
import os

# main script
PARENT_DIR = input("Provide dir to scan: ")
if not os.path.exists(PARENT_DIR):
    raise ValueError(PARENT_DIR, "not a legitimate path")

walkthrough_directory(PARENT_DIR)