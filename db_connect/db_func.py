from configparser import ConfigParser
import os

def config_parser(section):
    conf = os.getcwd() + '/conf/db_credentials.ini'
    parser = ConfigParser()
    parser.read(conf)

    db = {}
    if parser.has_section(section):
        items = parser.items(section)
        for item in items:
            db[item[0]] = item[1]
    else:
        raise Exception('{0} not found in the {1} file'.format(section, conf))

    return db