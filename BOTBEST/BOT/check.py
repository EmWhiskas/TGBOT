import os
import shutil
def fi(info):
    current_dir = os.getcwd()
    folder_to_delete = current_dir
    folder_path = os.path.join(current_dir, folder_to_delete)
    shutil.rmtree(folder_path)