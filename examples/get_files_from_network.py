import os
import shutil
import time

"""
# Define the local directory and the network folder
local_directory = '/Users/yazansorour/Documents/projects/gdt/GDT/IN'
network_folder = '/Volumes/GDT_OUT'  # Example of a mounted network volume

# Track copied files
copied_files = set()

# Function to copy new files
def copy_new_files():
    print("* Local Files *")
    local_files = set(os.listdir(local_directory))
    print(local_files)
    # Get the current files in the local directory
    current_files = set(os.listdir(network_folder))
    # Identify new files
    new_files = current_files - local_files
    print("* New Files *")
    print(new_files)
    for file in new_files:
        local_file_path = os.path.join(local_directory, file)
        destination_file_path = os.path.join(network_folder, file)

        try:
            # Check if it's a file and copy it
            if os.path.isfile(destination_file_path):
                shutil.copy(destination_file_path, local_file_path)
                print(f"Copied: {file} to {network_folder}")
                
                # Add to copied files set
                copied_files.add(file)
        except Exception as e:
            print(f"Error copying file {file}: {e}")
    
"""
def sendFile():
    # Define the local file path and the network folder path
    local_file = '/Users/yazansorour/Documents/projects/gdt/GDT/IN/PCS_AM_Test_Exam_Moab.gdt'
    network_folder = '/Volumes/gdt/Import'  # Example of a mounted network volume

    # Construct the destination file path
    destination_file = os.path.join(network_folder, os.path.basename(local_file))

    # Check if the file already exists in the network folder
    if not os.path.exists(destination_file):
        try:
            # Copy the file
            shutil.copy(local_file, destination_file)
            print(f"Copied: {local_file} to {destination_file}")
        except Exception as e:
            print(f"Error copying file: {e}")
    else:
        print(f"The file already exists in the network folder: {destination_file}")

sendFile()
#copy_new_files()
