# DAY 68 : Exercise 7 - Clear the Clutter 

import os

def clear_clutter(folder_path):
    # Initialize counters for different file formats
    png_count = 0
    jpg_count = 0
    other_count = 0

    # Loop through all files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".png"):
            png_count += 1
            os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, f"{png_count}.png"))
        elif filename.endswith(".jpg"):
            jpg_count += 1
            os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, f"{jpg_count}.jpg"))
        else:
            other_count += 1

    print("Renamed PNG files:", png_count)
    print("Renamed JPG files:", jpg_count)
    print("Other files:", other_count)

# Provide the folder path
folder_path = "image///"

# Call the function to clear clutter inside the folder
clear_clutter(folder_path)
