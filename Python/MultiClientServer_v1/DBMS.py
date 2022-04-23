import os

from dataclasses import dataclass, asdict, astuple, fields, field
from abc import ABC, abstractmethod

from DBGlobals import *
from DBCommands import *

from termcolor import colored

def Parse(command: str):
    if command == '':
        return 1
    words = command.split(' ')
    if words[0] not in commandsDict.keys():
        return f'>>> {colored("No such command","red")}: {colored(words[0],"cyan")} <<<'
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
