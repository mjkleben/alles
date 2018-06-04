import os
import inspect
import shutil

path = os.path.dirname(os.getcwd())
path = path + r"\alles" + "\setup\\"
install = path + "get-pip.py"
chrome = path + "GoogleChrome_Installer.exe"
os.system("python.exe " + install)

list = ['requests', 'bs4','selenium','pytube' ,'pip','lxml']

path2 = os.path.dirname(os.getcwd())
path2 = path2 + r"\alles" + "\my_startup_scripts\\" + "MacroStarter.exe"

s_path = str(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))).split("\\")
string1 = r"C:\Users"
string2 = r"\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
start_path = string1 + "\\" + str(s_path[2]) + string2 + "\\"

shutil.move(path2, start_path)

for package in list:
    os.system("python -m pip install " + package)

os.system(chrome)
