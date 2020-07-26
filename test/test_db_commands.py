import unittest
import utility.db.db_controller as db_controller


class TestCreateTable(unittest.TestCase):
    def test_create_tb_comp_name_cmd(self):
        #conn to bd
        # db check if tables is present in db, at teh moment not sure what db is
        # build paths
        dir_path = "./utility/db"
        file = "db_create_tab_comp_name.sql"
        cmd = db_controller.build_inset_tbl_comp_name(dir_path, file)
        self.assertIsNotNone(cmd)

    def test_insert_command(self):
        row = {'cod_fiscal':'4563023', 'nume':'SCOALA AJUTORARE BLAJ', 'stare':'RADIERE',\
        'tva':'NU', 'loc':'Blaj', 'sect': '', 'str': '1848', 'nr': '     11', 'fax': '         0',\
        'tel': '    710566', 'cp':'', 'detalii_adresa': '', 'bloc': '', 'scara': '', 'etaj': '', 'ap': ''}
        in_cmd = db_controller.build_insert_cmd_comp_name(row)
        res = "INSERT INTO Company (cod_fiscal,nume,stare,tva,loc,str,nr,fax,tel) VALUES ('4563023','SCOALA AJUTORARE BLAJ','RADIERE','NU','Blaj','1848','     11','         0','    710566');"
        false_res ="INSERT INTO Alocard (cod_fiscal,nume,stare,tva,loc,str,nr,fax,tel) VALUES ('4563023','SCOALA AJUTORARE BLAJ','RADIERE','NU','Blaj','1848','     11','         0','    710566');"
        self.assertIsNotNone(in_cmd)
        self.assertEqual(res, in_cmd)
        self.assertNotEqual(false_res, in_cmd)
if __name__ == '__main__':
    unittest.main()
