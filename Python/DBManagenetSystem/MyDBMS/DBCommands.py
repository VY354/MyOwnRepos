import os
from math import *

from dataclasses import dataclass, asdict, astuple, fields, field
from abc import ABC, abstractmethod

from DBGlobals import *
from DBFilesManager import *


def commandDecorator(execFunc):
    def decorator(*args, **kwargs):
        try:
            return execFunc(*args, **kwargs)
        except Exception as e:
            print(f'>>> ERROR ::::: {e}')
            return -1
    return decorator


@dataclass
class commandAbstract(ABC,object):
    command: str = field(default='')


    @abstractmethod
    @commandDecorator
    def exec(self, *args, **kwargs):
        pass

    @abstractmethod
    def description(self):
        pass


@dataclass
class setCommand(commandAbstract):
    global currDB
    global DBs

    def __init__(self):
        super(setCommand, self).__init__()
        self.command = 'set'

    @commandDecorator
    def exec(self, *args, **kwargs):
        for i in range(0, len(args), 2):
            currDB['db'][args[i]] = args[i + 1]
        return 1

    def description(self):
        print(f'{self.command} ::: set one or multiple pair key-value | example: set a 10 ...')



@dataclass
class getCommand(commandAbstract):
    global currDB
    global DBs

    def __init__(self):
        super(getCommand, self).__init__()
        self.command = 'get'

    @commandDecorator
    def exec(self, *args, **kwargs):
        for key in args:
            print(currDB['db'][key])
        return 1

    def description(self):
        return f'{self.command} ::: get one or multiple values by keys | example: get a ...'


@dataclass
class createDBCommand(commandAbstract):
    global currDB
    global DBs

    def __init__(self):
        super(createDBCommand, self).__init__()
        self.command = 'cdb'

    @commandDecorator
    def exec(self, *args, **kwargs):
        if args[0] in DBs.keys(): raise Exception('Already have such database')
        DBs[args[0]] = {}
        return 1

    def description(self):
        print(f'{self.command} ::: create database | example: cdb db1')


@dataclass
class useDBCommand(commandAbstract):
    global currDB
    global DBs

    def __init__(self):
        super(useDBCommand, self).__init__()
        self.command = 'udb'

    @commandDecorator
    def exec(self, *args, **kwargs):
        currDB['db'] = DBs[args[0]]
        currDB['name_db'] = args[0]

        return 1

    def description(self):
        print(f'{self.command} ::: select database to work with | example: udb db1')


@dataclass
class showDBCommand(commandAbstract):
    global currDB
    global DBs

    def __init__(self):
        super(showDBCommand, self).__init__()
        self.command = 'shdb'

    @commandDecorator
    def exec(self, *args, **kwargs):
        db = DBs[args[0]]
        for (k, v) in zip(db.keys(), db.values()):
            print('{0} ::: {1}'.format(k, v))
        return 1

    def description(self):
        print(f'{self.command} ::: print all database key-value pairs | example: pdb db1')



class printDBCommand(commandAbstract):
    global currDB
    global DBs

    def __init__(self):
        super(printDBCommand, self).__init__()
        self.command = 'pdbs'

    @commandDecorator
    def exec(self, *args, **kwargs):
        for db in DBs.keys():
            print(db)
        return 1

    def description(self):
        print(f'{self.command} ::: show databases | example: shdb')


@dataclass
class printDBsFilesCommand(commandAbstract):
    global currDB
    global DBs


    def __init__(self):
        super(printDBsFilesCommand, self).__init__()
        self.command = 'pdbfs'

    @commandDecorator
    def exec(self, *args, **kwargs):
        files = getDBsFiles()
        for f in files:
            print(f)

    def description(self):
        print(f'{self.command} ::: print all saved csv files | example: pdbfs')

@dataclass
class currdbCommand(commandAbstract):
    global currDB
    global DBs

    def __init__(self):
        super(currdbCommand, self).__init__()
        self.command = 'crdb'

    @commandDecorator
    def exec(self, *args, **kwargs):
        print (currDB['name_db'])


    def description(self):
        print(f'{self.command} ::: print current database name | example: crdb')


@dataclass
class showCmdListCommand(commandAbstract):
    global currDB
    global DBs

    def __init__(self):
        super(showCmdListCommand, self).__init__()
        self.command = 'shcmdl'

    @commandDecorator
    def exec(self, *args, **kwargs):
        print('------------------------')
        for cmd in commandsDict.values():
            cmd.description()
        print('------------------------')

    def description(self):
        print(f'{self.command} ::: show list of available commands | example: shcmdl')


@dataclass
class concatDBsCommand(commandAbstract):
    global currDB
    global DBs

    def __init__(self):
        super(concatDBsCommand, self).__init__()
        self.command = 'cnct'

    @commandDecorator
    def exec(self, *args, **kwargs):
        firstDB = DBs[args[0]]
        for arg in args[1:]:
            secondDB = DBs[args[1]]
            for k in secondDB.keys():
                firstDB[k]=secondDB[k]

    def description(self):
        print(f'{self.command} ::: concatenates 2 or more databases; data added to first defined database | example: cnct db1 db2 db3 ...')


@dataclass
class saveDBCommand(commandAbstract):
    global currDB
    global DBs

    def __init__(self):
        super(saveDBCommand, self).__init__()
        self.command = 'savedb'

    @commandDecorator
    def exec(self, *args, **kwargs):
        for arg in args:
            saveDBtoCSV({'name_db':arg,'db':DBs[arg]})

    def description(self):
        print(f'{self.command} ::: save one or several databases to csv format | example: fave db1 db2 ...')


@dataclass
class removeDBCommand(commandAbstract):
    global currDB
    global DBs


    def __init__(self):
        super(removeDBCommand, self).__init__()
        self.command = 'rmdb'

    @commandDecorator
    def exec(self, *args, **kwargs):
        for arg in args:
            DBs.pop(arg)
            currDB.clear()

    def description(self):
        print(f'{self.command} ::: remove one or several databases | example: rmdb db1 db2 ...')


@dataclass
class removeDBFileCommand(commandAbstract):
    global currDB
    global DBs


    def __init__(self):
        super(removeDBFileCommand, self).__init__()
        self.command = 'rmdbf'

    @commandDecorator
    def exec(self, *args, **kwargs):
        for arg in args:
            removeDB(arg)

    def description(self):
        print(f'{self.command} ::: remove one or several databases csv file | example: rmdbf db1 db2 ...')


@dataclass
class loadDBCommand(commandAbstract):
    global currDB
    global DBs

    def __init__(self):
        super(loadDBCommand, self).__init__()
        self.command = 'loaddb'

    @commandDecorator
    def exec(self, *args, **kwargs):
        for arg in args:
            DBs[args[0]] = loadDBfromCSV(arg)

    def description(self):
        print(f'{self.command} ::: load one or several databases from csv | example: loaddb db1 db2 ...')



@dataclass
class exitCommand(commandAbstract):
    global currDB
    global DBs

    def __init__(self):
        super(exitCommand, self).__init__()
        self.command = 'exit'

    @commandDecorator
    def exec(self, *args, **kwargs):
        return 0

    def description(self):
        print(f'{self.command} ::: exit from database management system | example: exit')



commandsObjectsList = [
    setCommand(),
    getCommand(),
    createDBCommand(),
    useDBCommand(),
    exitCommand(),
    showDBCommand(),
    currdbCommand(),
    printDBCommand(),
    showCmdListCommand(),
    concatDBsCommand(),
    saveDBCommand(),
    removeDBCommand(),
    removeDBFileCommand(),
    loadDBCommand(),
    printDBsFilesCommand()
]


commandsDict = {}

for cmd in commandsObjectsList:
    commandsDict[cmd.command]=cmd