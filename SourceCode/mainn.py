import os
import time

os.system('mode con: cols=20 lines=5')
print("Loading alles..")

alles = "alleslauncher.exe"
logo_open = "alleslogo.exe"

alles_path = "FILLER"
logo_path = "FILLER"
for root, dirs, files in os.walk("C:\\Users\\"):
    if alles in files:
        alles_path = str(os.path.join(root, alles))
    if logo_open in files:
        logo_path = str(os.path.join(root, logo_open))

os.system(logo_path)
time.sleep(1)
os.system('mode con: cols=85 lines=33')
os.system(alles_path)

