import datetime

from sqlalchemy import insert, delete, select

from dbObjects import engineObj, metaDataObj
import dbModels


# ==============================================================================

# select data from db and return cards data as list of dictionaries
def getTaskCards():
    stmt = select(dbModels.tasks_table)
    with engineObj.connect() as conn:
        res = conn.execute(stmt)
        return [{k: v for (k, v) in zip(dbModels.tasks_table.c.keys(), x)} for x in res.fetchall()]


# adding 'date' attribute and make insert query
def insertTaskCard(dataDict: dict):
    dataDict.update({'date': datetime.datetime.now().strftime('%Y-%m-%d %H:%M')})
    with engineObj.connect() as conn:
        conn.execute(
            insert(dbModels.tasks_table),
            dataDict
        )


# remove card by given id
def removeTaskCard(id: int):
    stmt = delete(dbModels.tasks_table).where(dbModels.tasks_table.c.id == id)
    with engineObj.connect() as conn:
        conn.execute(stmt)


# flushing tables if needed
def FlushTables(*args):
    with engineObj.connect() as conn:
        with conn.begin():
            # ignoring linking tables by foreign keys
            conn.execute('set foreign_key_checks = 0')
            if not args:
                tabNames = list(metaDataObj.tables.keys())
                for t in tabNames:
                    conn.execute(f'truncate table {t};')
            else:
                conn.execute(f'truncate table {args[0].name}')
            # set parameter back to value 1
            conn.execute('set foreign_key_checks = 1')


# ==========================================================================

if __name__ == '__main__':
    metaDataObj.create_all(engineObj)
    FlushTables()
