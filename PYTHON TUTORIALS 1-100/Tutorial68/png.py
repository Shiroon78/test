import os
import win32file
import win32con

folder_path = "C:\Users\my pc\OneDrive\Documents\exercise 7 test folder"

# Check if the folder exists, if not create it
if not os.path.exists(folder_path):
    os.mkdir(folder_path)

# Get a handle to the folder
folder_handle = win32file.CreateFile(
    folder_path,
    win32con.GENERIC_WRITE,
    0,
    None,
    win32con.CREATE_NEW,
    win32con.FILE_ATTRIBUTE_NORMAL,
    None
)

# Close the handle
win32file.CloseHandle(folder_handle)

# Loop through all the files
for index in range(1, 101):
    file_name = f'{index}.png'
    file_path = os.path.join(folder_path, file_name)
    with open(file_path, 'wb') as file:
        file.write(b' ')

print(f'Files have been created in {folder_path}')