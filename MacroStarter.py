import os
from os import listdir

os.system('mode con: cols=15 lines=5')

name = "s_finder.txt"
path = ""
for root, dirs, files in os.walk("C:\\Users\\"):
    if name in files:
        path = os.path.join(root, name)

path = path.replace("s_finder.txt", "")
list_files = listdir(path)

for file in list_files:
    if ".py" in file:
        full = "python.exe " + path + file
        os.system(full)

