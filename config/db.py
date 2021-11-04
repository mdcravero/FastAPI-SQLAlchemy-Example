from sqlalchemy import create_engine
import pymssql
from sqlalchemy.sql.schema import MetaData


engine = create_engine(
    r"mssql+pymssql://{0}:{1}@172.16.20.50:1433/TEST?charset=utf8".format('sa', 'Municipio413$'))

meta = MetaData()

conn = engine.connect()
