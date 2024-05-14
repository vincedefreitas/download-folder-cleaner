import os
import shutil
import datetime

# Define mapping of file extensions to folder names
file_extensions = {
    "jpg": "Pictures",
    "jpeg": "Pictures",
    "png": "Pictures",
    "gif": "Pictures",
    "pdf": "Documents",
    "doc": "Documents",
    "docx": "Documents",
    "txt": "Documents",
    "zip": "Documents",
    "mp4": "Movies",
    # Add more file extensions and corresponding folder names as needed
}

# Define list of installer file extensions
installer_extensions = {"dmg", "pkg", "exe", "msi", "deb"}

# Get today's date
today = datetime.date.today()
date_folder_name = today.strftime("%Y-%m-%d")

# Path to downloads folder
downloads_folder = os.path.expanduser("~/Downloads")

def move_files_and_cleanup(folder):
    for root, _, files in os.walk(folder):
        for filename in files:
            file_path = os.path.join(root, filename)

            # Get file extension
            _, extension = os.path.splitext(filename)
            extension = extension[1:].lower()  # Remove the dot and make lowercase

            # Check if the file is an installer
            if extension in installer_extensions:
                # Remove installer files
                os.remove(file_path)
            else:
                # Get destination folder based on file extension
                destination_folder = file_extensions.get(extension, "Other")

                # Create destination folder if it doesn't exist
                destination_path = os.path.join(os.path.expanduser("~/"), destination_folder, date_folder_name)
                os.makedirs(destination_path, exist_ok=True)

                # Move the file out of downloads folder into the destination folder
                shutil.move(file_path, os.path.join(destination_path, filename))

# Move files from subfolders within Downloads and perform cleanup
move_files_and_cleanup(downloads_folder)