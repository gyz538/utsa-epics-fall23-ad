import os
import shutil

def organize_files(folder_path, files_per_folder=10):
    if not os.path.exists(folder_path):
        print("The folder '{}' does not exist.".format(folder_path))
        return

    image_extensions = ['.webp']
    image_files = [file for file in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, file)) and os.path.splitext(file)[1].lower() in image_extensions]

    if not image_files:
        print("No image files found in the folder.")
        return

    image_files.sort()

    for i, old_name in enumerate(image_files):
        folder_number = i // files_per_folder + 1
        new_folder_name = "{:02d}".format(folder_number)
        new_folder_path = os.path.join(folder_path, new_folder_name)
        if not os.path.exists(new_folder_path):
            os.makedirs(new_folder_path)

        new_name = os.path.join(new_folder_path, old_name)
        old_path = os.path.join(folder_path, old_name)
        shutil.move(old_path, new_name)
        print("Moved: {} -> {}".format(old_name, new_name))

if __name__ == "__main__":
    folder_path = "/Users/amydominguez/Downloads/python"
    organize_files(folder_path, files_per_folder=10)
