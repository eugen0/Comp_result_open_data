import unittest
import utility.db.util_db as util


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

if __name__ == '__main__':
    unittest.main()
