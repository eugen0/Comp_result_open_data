import unittest, psycopg2
#from utility.db import db_controller
import utility.db.db_controller as db_controller

class TestCreateTable(unittest.TestCase):
    def test_create_tb_comp_name_cmd(self):
        #conn to bd
        # db check if tables is present in db, at teh moment not sure what db is and what it will return 
        cmd = db_controller.build_inset_tbl_comp_name()
        self.assertIsNotNone(cmd)

    def test_insert_command(self):
       pass


if __name__ == '__main__':
    unittest.main()
