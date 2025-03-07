import os

def clear_folder(folder_patch):
    for filename in os.listdir(folder_patch):
        file_patch = os.path.join(folder_patch,filename)
        try:
            if os.path.isfile(file_patch):
                os.remove(file_patch)
        except Exception as e:
            print(f'Error deleting file {file_patch}: {e}')
