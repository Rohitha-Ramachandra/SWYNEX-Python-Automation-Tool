import os
import shutil

def organize_files(folder_path):
    if not os.path.exists(folder_path):
        print("Error: Folder does not exist.")
        return

    file_types = {
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Documents": [".pdf", ".docx", ".txt", ".doc"],
        "Videos": [".mp4", ".mkv", ".mov"],
        "Audio": [".mp3", ".wav"],
        "Python_Files": [".py"],
    }

    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)

        if os.path.isfile(file_path):
            extension = os.path.splitext(file_name)[1].lower()
            destination_folder = "Others"

            for folder_name, extensions in file_types.items():
                if extension in extensions:
                    destination_folder = folder_name
                    break

            target_folder = os.path.join(
                folder_path, destination_folder
            )
            os.makedirs(target_folder, exist_ok=True)

            target_path = os.path.join(target_folder, file_name)

            if os.path.exists(target_path):
                print(f"Skipped duplicate file: {file_name}")
                continue

            shutil.move(file_path, target_path)
            print(f"Moved {file_name} to {destination_folder}")

    print("File organization completed!")


if __name__ == "__main__":
    folder_to_organize = input(
        "Enter the folder path to organize: "
    ).strip().strip('"')

    organize_files(folder_to_organize)