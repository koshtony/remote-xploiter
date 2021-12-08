from threading import *
from socket import *

class server:
    def __init__(self):
        self.serv=socket(AF_INET,SOCK_STREAM)
        address=('192.168.1.18',2234)
        self.serv.bind(address)
        self.serv.listen(5)
        self.con,addr=self.serv.accept()
        self.os = self.con.recv(1024).decode()
        print("connected to: ",self.os," ip ",addr)
    def sending(self,meso):
        self.con.send(meso.encode())
    def revg(self):
        while True:
            back=self.con.recv(1024).decode()
            recvd=str(back)+"\n"
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