import os

folder_path = 'C:\Users\my pc\OneDrive\Documents\exercise 7 test folder'

# Get a list of all the files in the folder
files = os.listdir(folder_path)

# Filter the list to only include PNG files
png_files = [file for file in files if file.endswith('.png')]

# Sort the list in ascending order
png_files.sort()

# Get the last PNG file in the list
last_png_file = png_files[-1]

# Get the index of the last PNG file
last_png_index = int(last_png_file.split('.')[0])

# Loop through all the PNG files and remove them
for index in range(1, last_png_index + 1):
    file_name = f'{index}.png'
    file_path = os.path.join(folder_path, file_name)
    os.remove(file_path)

# Print a message to indicate that the clutter has been cleared
print(f'Clutter has been cleared from {folder_path}')