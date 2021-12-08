from socket import *
from threading import *
import sys
from colorama import init
from pyfiglet import figlet_format as ff
from termcolor import cprint
init(strip=not sys.stdout.isatty())
cprint(ff('TOMASO',font='starwars'),attrs=['bold'])

class server:
    def __init__(self):
        self.serv=socket(AF_INET,SOCK_STREAM)
        address=('192.168.8.106',2234)
        self.serv.bind(address)
        self.serv.listen(5)
        self.con,addr=self.serv.accept()
        self.name=input("who am i>>> ")
        self.con.send(self.name.encode())
        self.other=self.con.recv(1024).decode()
        print("connected to: ", self.other," ip ",addr)
    def sending(self,meso):
        self.con.send(meso.encode())
    def revg(self):
        while True:
            back=self.con.recv(1024).decode()
            recvd=str(self.other)+">>>"+str(back)+"\n"
            print(recvd)
            print("======================\n")
    def main(self):
        while True:
            print("======================\n")
            mesos=input()
            self.sending(mesos)
servs=server()
getting=Thread(target=servs.revg)
getting.daemon=True
getting.start()
servs.main()
