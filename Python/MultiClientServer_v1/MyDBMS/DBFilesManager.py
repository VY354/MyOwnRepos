import os
from dataclasses import dataclass, asdict, astuple, fields, field
from abc import ABC, abstractmethod
import csv


DBFilesDirName = 'DBFiles'

def saveDBtoCSV(DB : dict):
    fullFileName = f'{DBFilesDirName}/{DB["name_db"]}.csv'
    if not os.path.exists(fullFileName):
        os.system(f'touch {fullFileName}')
    with open(fullFileName,'w') as out:
        csvWriter = csv.writer(out)
        csvWriter.writerow(['key','value'])
        csvWriter.writerows([[key,value] for (key,value) in zip(DB['db'].keys(),DB['db'].values())])


def loadDBfromCSV(DBName : str):
    fullFileName = f'{DBFilesDirName}/{DBName}.csv'
    if not os.path.exists(fullFileName):
        raise Exception(f'There is no such file: {fullFileName}')
    with open(fullFileName,'r') as out:
        csvReader = csv.reader(out)
        csvReaderList = list(csvReader)[1:]
        return {x[0]:int(x[1]) for x in csvReaderList}


def removeDB(DBName : dict):
    fullFileName = f'{DBFilesDirName}/{DBName}.csv'
    if not os.path.exists(fullFileName):
        raise Exception(f'There is no such file: {fullFileName}')
    os.system(f'rm {fullFileName}')


def getDBsFiles():
    files = os.listdir(DBFilesDirName)
    return [f for f in files if os.path.isfile(f'{DBFilesDirName}/{f}')]



def main():
    data = {}
    db ={'name_db':'testfile','db':data}

    for i in range(10):
        db['db'][str(i)]=i**2

    print(db['db'])

    saveDBtoCSV(db)
    loaddata = loadDBfromCSV(db['name_db'])
    print(loaddata)
    removeDB(db['name_db'])


if __name__ =='__main__':
    main()


