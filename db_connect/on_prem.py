from func import db_tools
from sqlalchemy import create_engine
import cx_Oracle
import pyodbc
import os

def mysql_connect():
    db = db_tools.config_parser("mysql")
    engine = create_engine(
        'mysql+mysqlconnector://{0}:{1}@{2}:{3}/{4}'.format(db['user'], db['password'], db['host'], db['port'], db['database'])
    )

    return engine

def postgresql_connect():
    db = db_tools.config_parser("postgresql")
    engine = create_engine(
        'postgres://{0}:{1}@{2}:{3}/{4}'.format(db['user'], db['password'], db['host'], db['port'], db['database'])
    )

    return engine

def sqlserver_connect():
    db = db_tools.config_parser("sqlserver")
    engine = create_engine(
        'mssql+pyodbc://{0}:{1}@{2}:{3}/{4}'.format(db['user'], db['password'], db['host'], db['port'], db['database'])
    )

    return engine

def oracle_connect():
    db = db_tools.config_parser("oracle")
    engine = create_engine(
        'oracle+cx_oracle://{0}:{1}@{2}:{3}/{4}'.format(db['user'], db['password'], db['host'], db['port'], db['database'])
    )

    return engine

def oracle2_connect():
    db = db_tools.config_parser("oracle")
    sid = cx_Oracle.makedsn('{0}', '{1}', service_name='{2}').format(db['host'], db['port'], db['sid'])
    engine = create_engine(
        'oracle+cx_oracle://{0}:{1}@{2}'.format(db['user'], db['password'], sid)
    )

    return engine