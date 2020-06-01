from db_func import config_parser
import cx_Oracle

# MySQL
def mysql_connect():
    db = config_parser("mysql")
    engine = create_engine(
        'mysql+mysqlconnector://{0}:{1}@{2}:{3}/{4}'.format(db['user'], db['password'], db['host'], db['port'], db['database'])
    )

    return engine

# PostgreSQL
def postgresql_connect():
    db = config_parser("postgresql")
    engine = create_engine(
        'postgres://{0}:{1}@{2}:{3}/{4}'.format(db['user'], db['password'], db['host'], db['port'], db['database'])
    )

    return engine

# SQL Server
def sqlserver_connect():
    db = config_parser("sqlserver")
    engine = create_engine(
        'mssql+pyodbc://{0}:{1}@{2}:{3}/{4}'.format(db['user'], db['password'], db['host'], db['port'], db['database'])
    )

    return engine

# Oracle
def oracle_connect():
    db = config_parser("oracle")
    engine = create_engine(
        'oracle+cx_oracle://{0}:{1}@{2}:{3}/{4}'.format(db['user'], db['password'], db['host'], db['port'], db['database'])
    )

    return engine

# Oracle with SID / Service Name
def oracle2_connect():
    db = config_parser("oracle")
    sid = cx_Oracle.makedsn('{0}', '{1}', service_name='{2}').format(db['host'], db['port'], db['sid'])
    engine = create_engine(
        'oracle+cx_oracle://{0}:{1}@{2}'.format(db['user'], db['password'], sid)
    )

    return engine