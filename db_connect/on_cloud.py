from db_func import config_parser
import psycopg2

def postgresql_connect():
    db = config_parser("postgresql")
    engine = psycopg2.connect(
        dbname=db['database'],
        host=db['host'],
        user=db['user'],
        password=db['password']
    )

    return engine

def redshift_connect():
    db = config_parser("redshift")
    engine = psycopg2.connect(
        dbname=db['database'],
        host=db['host'],
        user=db['user'],
        password=db['password']
    )

    return engine

def sqlserver_connect():
    db = config_parser("sqlserver")
    engine = psycopg2.connect(
        'Driver={SQL Server}'
        ';Server=%s' % db['host'] +
        ';Database=%s' % db['database'] +
        ';UID=%s' % db['user'] +
        ';PWD=%s' % db['password'] +
        ';Trusted_Connection=no'
    )

    return engine