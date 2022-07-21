import sqlalchemy
from sqlalchemy import MetaData

# ==============================================================================

# conntecion settings
usr = 'rayxxx'
pswd = 'password'
host = 'localhost'
db = 'taskCards'

# ==============================================================================

engineObj = sqlalchemy.create_engine(url=f'mysql+pymysql://{usr}:{pswd}@{host}/{db}')

metaDataObj = MetaData()
