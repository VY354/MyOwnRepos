import os

import socket
from _thread import *
import threading

import time

import termcolor
from termcolor import colored

from dataclasses import dataclass,asdict,astuple,fields,field

from DBMS import *

@dataclass(init=True,repr=True)
class MyServer:

    IP : str = field(default='127.0.0.1')
    PORT : int = field(default=7777)
    serverSocket : socket.socket = field(init=False,default=None)

    def create(self):
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.serverSocket.bind((self.IP, self.PORT))
        except socket.error as e:
            print(str(e))
            self.releasePort()

    def start(self):
        os.system('clear')
        self.serverSocket.listen(10)
        self.echo(f'SERVER >>> {colored("Sever is listening","green")} ...')

        while True:
            try:
                # self.serverSocket.settimeout(60)
                conn, addr = self.serverSocket.accept()
                newThread = threading.Thread(target=self.ClientThread, args=(conn, addr,))
                newThread.start()
                self.echo(f'SERVER >>> {colored("NEW connection","green")}: {painrAddr(addr)}')
            except socket.error as e:
                self.echo(f'{colored(f"{e}","red")}')
                self.stop()
                return

    def stop(self):
        self.serverSocket.close()
        os.system('fuser -vn tcp ' + str(self.PORT))

    def releasePort(self):
        os.system('fuser -vn tcp ' + str(self.PORT))
        waitt = 5
        start = time.time()
        dt = time.time() - start
        while dt < waitt:
            if dt % 1 == 0:
                os.system('clear')
                print('o ' * int(dt))
            dt = time.time() - start

    def ClientThread(self, conn: socket.socket, addr):
        while True:
            reply = conn.recv(1024)

            if not reply:
                self.echo(f'SERVER >>> {colored("client disconnected", "red")}: {painrAddr(addr)}')
                break

            commandResult = Parse(reply.decode('utf-8'))
            self.sendToClient(conn,str(commandResult))

            # self.sendToClient(conn,str(f'receive message from you ({addr})'))
            self.echo(f'SERVER >>> {colored("message from client","cyan")} {painrAddr(addr)} ::::: {reply.decode("utf-8")}')
        conn.close()

    def echo(self,string:str):
        print(string)

    def sendToClient(self,client:socket.socket,data:str):
        client.send(data.encode('utf-8'))


def painrAddr(addr):
    return colored(f'{addr[0]}',"yellow")+':'+colored(f'{addr[1]}',"yellow")



def main():
    ip = '127.0.0.1'
    port = 7777
    server = MyServer(ip,port)
    server.create()
    server.start()


if __name__ == '__main__':
    main()
