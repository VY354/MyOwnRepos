from sqlalchemy import Table, Column
from sqlalchemy import Integer, String

# contain engine and metadata objects
import dbObjects

tasks_table = Table(
    'tasks',
    dbObjects.metaDataObj,
    Column('id', Integer, primary_key=True, nullable=False, autoincrement=True),
    Column('date', String(20), nullable=False),
    Column('title', String(40), nullable=False),
    Column('text', String(300), nullable=False)
)
