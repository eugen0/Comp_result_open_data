
"""
class DbControl:
    def __init__(self, db_config_dict):
        self.connection = None
        self.db_config = db_config_dict

    def connect(self):
        try:
            db_config = self.db_config
            self.connection = psycopg2.connect(**db_config)
            self.connection.autocommit = True
            print(f"Connection to database successful")
        except psycopg2.OperationalError as e:
            print(f"Error '{e}' occurred! ")

    def stop_connection(self):
        self.connection.close()

    def execute_query(self, query):
        # execute a query as Insert or Create command
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            print("query run successfully")
        except psycopg2.OperationalError as e:
            print(f"Error '{e}' occurred")

    def select_query(self, query):
        cursor = self.connection.cursor()
        ret = None
        try:
            cursor.execute(query)
            ret = cursor.fetchall()
            cursor.close()
            print("select query run successfully")
        except psycopg2.OperationalError or psycopg2.ProgrammingError as e:
            print(f"Error '{e}' occurred")
        if ret:
            return ret

def create_connection(db_config):

    connection = None
    try:
        connection = psycopg2.connect(**db_config)
        print(f"Connection to database successful")
    except psycopg2.OperationalError as e:
        print(f"Error '{e}' occurred! ")
    return connection


def stop_connection(connection):
    connection.close()


def execute_query(connection, query):

    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("query run successfully")
    except psycopg2.OperationalError as e:
        print(f"Error '{e}' occurred")


def select_query(connection, query):

    connection.autocommit = True
    cursor = connection.cursor()
    ret = None
    try:
        cursor.execute(query)
        ret = cursor.fetchall()
        cursor.close()
        print("select query run successfully")
    except psycopg2.OperationalError or psycopg2.ProgrammingError as e:
        print(f"Error '{e}' occurred")
    if ret is not None:
        return ret

def read_sql_file(filepath='tables_sql'):
    with open(filepath, 'r') as sql_f:
        return sql_f.read()

"""


from configparser import ConfigParser
import psycopg2
from os import path

from utility.db import util_db

""""
def build_inset_tbl_cmd(dir_path, file):
    #imports CREATE TABLE Command from Company tables located in given file
    #:return: string of create table cmd

    # build paths
    file_list = os.listdir(dir_path)
    index = file_list.index(file)
    file_path = os.path.join(dir_path, file_list[index])

    # open sql text
    with open(file_path, 'r') as sql_f:
        tbl_command = sql_f.readlines()
        cmd = ""
        for line in tbl_command:
            cmd += line

    return cmd


def build_insert_cmd(file_row, table_name):
   # builds insert statement based on values found in row provided into table name provided
    #:param file_row: file row of data
    #:param table_name: table name
    #:return: cmd
    fst_part_cmd = "INSERT INTO " + table_name + " ("
    sec_part_cmd = "VALUES ("
    for x in file_row:
        # if missing values no need for column
        if not file_row[x]:
            continue
        else:
            # add column
            fst_part_cmd += x + ','

            # add values
            sec_part_cmd += "'" + file_row[x] + "'" + ','


    # remove last (,), # add closing bracket and ;
    fst_part_cmd = fst_part_cmd[:len(fst_part_cmd)-1] + ') '
    sec_part_cmd = sec_part_cmd[:len(sec_part_cmd)-1] + ');'

    insert_cmd = fst_part_cmd+sec_part_cmd
    return insert_cmd


def export_comp_names(dir_path, db_name_, user_, password_, host_ ):
    """"""
     creates table in db with names of companies from dir
    :param dir_path: dir where comp+name data is located
    :param db_name_: db name
    :param user_: db_user
    :param password_: db_password
    :param host_: bd_hos
    :return: none
    """"""
    #### create a table in db ######
    # connect to db
    db = psycopg2.connect(database=db_name_, user=user_, password=password_, host=host_)

    # get the cursor
    cursor = db.cursor()

    # cmd dir paths
    db_path = "../utility/db"
    file = "db_create_tab_comp_name.sql"

    # inset table cmd
    cmd = build_inset_tbl_cmd(db_path, file)

    # execute create table
    cursor.execute(cmd)

    # commit command
    db.commit()

    # create file list from dir
    files_list = build_filename_path(dir_path)

    # main loop
    for file in files_list:
        # delete explicatii.csv, do not need this one
        if file == "explicatii.csv":
            os.remove(os.path.join(dir_path, file))
            continue

        file_path = os.path.join(dir_path, file)

        # read file and export to db
        with open(file_path, 'r', encoding='utf-8') as cvs_in:
            csv_reader = csv.DictReader(cvs_in)
            next(csv_reader)                     # skip first row
            table_name = "Company"
            print("inserting {}".format(file))
            for row in csv_reader:
                insert_command = build_insert_cmd(row, table_name)

                # insert into db
                cursor.execute(insert_command)

            print("finished inserting {}".format(file))
            cvs_in.close()

    # close db conn
    db.commit()
    db.close()
"""


