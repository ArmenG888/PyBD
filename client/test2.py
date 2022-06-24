import requests

sample_file = open("test.png", "rb")
upload_file = {"file": sample_file}
r = requests.post("http://127.0.0.1:8000/screenshot/", files = upload_file)