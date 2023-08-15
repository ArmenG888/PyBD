import time
import requests



while True:
    r = requests.get("http://127.0.0.1:8000/computer/1")
    print(r.json()['ping'])