import os

def rename_images(folder_path):
    if not os.path.exists(folder_path):
        print("The folder '{}' does not exist.".format(folder_path))
        return

    image_extensions = ['.jpg', '.webp', '.jpeg', '.png', '.gif', '.bmp']
    image_files = [file for file in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, file)) and os.path.splitext(file)[1].lower() in image_extensions]
    
    if not image_files:
        print("No image files found in the folder.")
        return

    new_name_base = "TrumpMug"
    current_number = 1

    for old_name in image_files:
        extension = os.path.splitext(old_name)[1].lower()
        new_name = "{}_{:03d}{}".format(new_name_base, current_number, extension)
        old_path = os.path.join(folder_path, old_name)
        new_path = os.path.join(folder_path, new_name)
        os.rename(old_path, new_path)
        print("Renamed: {} -> {}".format(old_name, new_name))
        current_number += 1

if __name__ == "__main__":
    folder_path = "/Users/amydominguez/Downloads/python"
    rename_images(folder_path)

