import os

files = os.listdir("D:\Python couraw\Data2\Tutorial75\ClutterFolder")
i = 1
for file in files:
  print(file)
  if file.endswith(".png"):
    print(files)
    os.rename(f"D:\Python couraw\Data2\Tutorial75\ClutterFolder/{file}",f"D:\Python couraw\Data2\Tutorial75\ClutterFolder/{i}.png")
    i = i + 1
