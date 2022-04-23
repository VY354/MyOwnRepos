import os
import socket
import _thread
import re

from dataclasses import dataclass, asdict, astuple, fields, field

from termcolor import colored

from DBMS import *


@dataclass(init=True, repr=True)
class MyClient:
    clientSocket: socket.socket = field(init=False, default=None)
    connectionDataDict : dict = field(init=False,default=None)

    def __init__(self):
        self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connectionDataDict = {'IP':'','PORT':''}

    def connectTo(self, IP='127.0.0.1',PORT='7777'):
        try:
            self.clientSocket.connect((IP,PORT))
            self.connectionDataDict['IP']=IP
            self.connectionDataDict['PORT']=PORT
        except socket.error as e:
            return

    def close(self):
        self.clientSocket.close()

    def sendMessage(self, message: str):
        self.clientSocket.send(message.encode('utf-8'))

    def echo(self, string: str):
        print(string)

    def receiveData(self, size=1024):
        return self.clientSocket.recv(size)


@dataclass(init=True, repr=True)
class ClientManager:
    numOfClients: int = field(init=False, default=0)
    clientsList: list = field(init=False, default_factory=list)

    def selectClient(self,index):
        return self.clientsList[index]

    def addClient(self):
        newClient = MyClient()
        try:
            newClient.connectTo(serverIP, serverPORT)
            self.numOfClients+=1
        except socket.error as e:
            self.echo(f'{colored(f"{e}", "red")}')
            return 0
        self.clientsList.append(newClient)
        return  newClient

    def echo(self, string: str):
        print(string)



class ClientManagerInterface(ClientManager):

    def start(self):
        ans = None
        currClient: MyClient
        currClient = None

        while True:

            self.menu()
            print('=========================================================')
            if currClient:
                print(f'Current client ---> {self.paintAddr(currClient.clientSocket.getsockname())}')
                print('=========================================================')
            ans = int(input('select action: '))

            os.system('clear')

            if ans == 1:
                if currClient:
                    os.system('clear')
                    while 1:
                        line = input('DB MANAGER >>> write command: ')
                        currClient.sendMessage(line)
                        reply = currClient.receiveData(1024)
                        print(f'{reply.decode("utf-8")}')
                        # print(f'CLIENT MANAGER >>> {colored("server reply", "cyan")}  :::::\n {reply.decode("utf-8")}')
                        try:
                            if int(reply.decode('utf-8'))==0:
                                break
                        except Exception as e:
                            # print(f'CLIENT MANAGER >>> ERROR ::::: {colored(e,"red")}')
                            continue

            elif ans == 3:
                if len(self.clientsList):
                    ans = -1
                    while ans < 0 or ans >= len(self.clientsList):
                        os.system('clear')
                        cli: MyClient
                        for n, cli in enumerate(self.clientsList):
                            print(f'{n:>3} --- {self.paintAddr(cli.clientSocket.getsockname())}')
                        print('=======================================')
                        ans = int(input('Select client: '))
                    currClient = self.selectClient(ans)
                    os.system('clear')

            elif ans == 5:
                os.system('clear')
                newClient = self.addClient()
                print(
                    f'CLIENT MANAGER >>> Client {self.paintAddr(newClient.clientSocket.getsockname())} {colored("connected to server", "green")}')
            elif ans == 7:
                if currClient:
                    mes = f'CLIENT MANAGER >>> {colored("client disconnected", "red")}: {self.paintAddr(currClient.clientSocket.getsockname())}'
                    currClient.close()
                    self.clientsList.remove(currClient)
                    self.numOfClients -= 1
                    os.system('clear')
                    currClient = None
                    self.echo(mes)
            elif ans == 0:
                for cli in self.clientsList:
                    cli.close()
                break

    def menu(self):
        print('=========================================================')
        print('1 --- continue')
        print('------------------------------------')
        print('3 --- select another client')
        print('5 --- add new client')
        print('7 --- disconnect')
        print('------------------------------------')
        print('0 --- exit')


    def paintAddr(self, addr):
        return colored(f'{addr[0]}', "yellow") + ':' + colored(f'{addr[1]}', "yellow")




serverIP = '127.0.0.1'
serverPORT = 7777


def main():
    cliManager = ClientManagerInterface()
    cliManager.start()


if __name__ == '__main__':
    main()
