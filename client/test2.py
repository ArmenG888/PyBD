import os

try:
    os.system("taskkill /f /im new_main.exe")
    os.remove("new_main.exe")
except:
    os.system("taskkill /f /im main.exe")
    os.remove("main.exe")