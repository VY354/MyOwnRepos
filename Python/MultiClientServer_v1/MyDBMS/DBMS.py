import os

from dataclasses import dataclass, asdict, astuple, fields, field
from abc import ABC, abstractmethod

from DBGlobals import *
from DBCommands import *


def Parse(command: str):
    if command == '':
        return 1
    words = command.split(' ')
    if words[0] not in commandsDict.keys():
        return print(f'>>> No such command: {words[0]} <<<')
        # return 1
    return commandsDict[words[0]].exec(*words[1:])


@dataclass()
class MyDBManagementSys:
    def start(self):
        while 1:
            line = input('---> ')
            res = Parse(line)
            if res == 0:
                break



def main():
    dbms = MyDBManagementSys()
    dbms.start()


if __name__ == '__main__':
    main()
