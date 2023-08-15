import os, threading


def run():
    os.system("test2.py") # starts the bot 

while True:
    threading.Thread(target=run).start()
