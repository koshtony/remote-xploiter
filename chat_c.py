from socket import *
from threading import *
from sqlite3 import *
import sys
from colorama import init
from pyfiglet import figlet_format as ff
from termcolor import cprint
from tqdm import tqdm
import time
init(strip=not sys.stdout.isatty())
cprint(ff('TOMASO',font='starwars'),attrs=['bold'])
class client:
    def __init__(self):
        self.cli=socket(AF_INET,SOCK_STREAM)
        address=('192.168.1.13',2234)
        for i in tqdm (range (101), desc="connecting to the server…", ascii=False, ncols=75):
            time.sleep(0.1)
        print("==========================\n")
        self.cli.connect(address)
        self.name=input("who am i>>>: ")
        self.cli.send(self.name.encode())
    
        self.other=self.cli.recv(1024).decode()
    def sender(self,messg):
        self.cli.send(messg.encode())
    def store_messg(self,name,mess):
        self.dab=connect("messg.db")
        self.cus=self.dab.cursor()
        self.cus.execute('''create table if not exists message(name text,message text)''')
        self.cus.execute('''insert into message(name,message) values(?,?)''',(name,mess))
        self.dab.commit()
        self.dab.close()
    def retrieve_messg(self):
        self.con=connect("messg.db")
        self.cs=self.con.cursor()
        self.cs.execute('''select *from message''')
        rows=self.cs.fetchall()
        for row in rows:
            print(row)
        self.con.close()
    def reci(self):
        while True:
            self.data=self.cli.recv(1024).decode()
            recvd=str(self.other)+">>>"+str(self.data)+"\n"
            print(recvd)
            print("===================\n")
            self.store_messg(self.other,self.data)
    def main(self):
        while True:
            print("===================\n")
            messg=input()
            self.sender(messg)

cl=client()
rp=Thread(target=cl.reci)
rp.daemon=True
rp.start()
cl.main()
