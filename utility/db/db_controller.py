from utility.db.util_db import Db


# importing data into database
def import_com_name(db_config_path, config_section, file_dir_path):
    datab= Db(db_config_path, config_section)


def read_insert_sql_file(insert_sql_file):
    with open(insert_sql_file, 'r') as sql_f:
        cmd = sql_f.read()
        cmd.format()





db = Db()
# connect
db.connect()

# do stuff

# close
db.disconnect()

