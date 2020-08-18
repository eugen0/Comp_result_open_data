
""" assuming bd postgresql , other wise change the database.init file to something you like"""
from configparser import ConfigParser
import psycopg2
from os import path


class Db:
    @staticmethod
    def read_db_config_file(filename='database.ini', section='postgresql'):
        """
            Reads bd file configuration and returns configuration parameters
            :param filename: file where parameters ara saved
            :param section: postgresql section
            :return: config parameters
            """
        # parser
        parser = ConfigParser()

        # read db config file or return
        if path.exists(filename):
            parser.read(filename)
        else:
            raise Exception(f"file'{filename}' do not exist")

        db_config = {}
        if parser.has_section(section):
            param = parser.items(section)
            for par in param:
                db_config[par[0]] = par[1]
        else:
            raise Exception(f"Section '{section} not found in file '{filename}'")
        return db_config

    def __init__(self, config_filepath='database.ini', section='postgresql'):
        self.config_dict = self.read_db_config_file(config_filepath, section)
        self.connection = None

    def print_conn(self):
        print(self.connection, "from print_conn")

    def connect(self):
        db_config = self.config_dict
        try:
            self.connection = psycopg2.connect(**db_config)
            print(f"Connection to database successful")
        except psycopg2.OperationalError as e:
            print(f"Error '{e}' occurred! ")
            return self.connection

    def disconnect(self):
        cursor = self.connection.cursor()
        cursor.close()
        self.connection = None

    def execute_query(self, query):
        try:
            self.connection.autocommit = True
            cursor = self.connection.cursor()
            cursor.execute(query)
            print("execute_query run successfully")
        except psycopg2.OperationalError as e:
            print(f"Error '{e}' occurred")

    def execute_sql_file(self, filepath='tables_sql'):
        with open(filepath, 'r') as sql_f:
            self.execute_query(sql_f.read())

    def select_query(self, query):
        self.connection.autocommit = True
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






















