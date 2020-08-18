import unittest
import utility.db.util_db as util
from utility.db.db_controller import ImportCompName


class DbTest(unittest.TestCase):

    def test_connection(self):
        config_file = '../utility/db/database.ini'
        db = util.Db(config_file, 'postgresql')
        db.connect()
        self.assertIsNotNone(db.connection)

        db.disconnect()
        self.assertIsNone(db.connection)

    def test_cmd(self):
        config_file = '../utility/db/database.ini'
        db = util.Db(config_file, 'postgresql')
        db.connect()
        print(db.print_conn())
        self.assertIsNotNone(db.connection)

        # execute query
        query = "CREATE DATABASE Demon;"
        db.execute_query(query)
        ret = db.select_query("SELECT datname FROM pg_database;")
        print(ret)
        for x in ret:
            if 'demon' in x:
                self.assertTrue('demon' in x)

        # exct sql_file
        sql_file = '../utility/db/tables_sql'
        db.execute_sql_file(sql_file)
        query1 = "DROP DATABASE Demon;"
        db.execute_query(query1)
        ret = db.select_query("SELECT datname FROM pg_database;")
        for x in ret:
            if 'demon' not in x:
                self.assertFalse('demon' in x)

        # dic
        db.disconnect()


class InsertIntoDb(unittest.TestCase):
    def test_file_read(self):
        config_file = '../utility/db/database.ini'
        file_dir_path = '../utility/data/comp_names'
        db_insert = ImportCompName(config_file, config_section='postgresql', file_dir_path=file_dir_path)

        # check connection
        self.assertIsNotNone(db_insert.connection)
        print(db_insert.print_conn())

        db_insert.read_comp_names()

        self.assertTrue(db_insert.read_file)

        db_insert.import_comp_names()

        self.assertEqual(True, False)



if __name__ == '__main__':
    unittest.main()
