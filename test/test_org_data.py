import unittest
from utility.org_data import org_data
import csv

class MyTestCase(unittest.TestCase):
    def test_build_filenames_path(self):
        path = "../utility/data/comp_names"
        list_file_names = org_data.build_filename_path(path)
        self.assertEqual(len(list_file_names), 44)
    def test_keep_only_comp_name_info(self):
        path_file = "../utility/data/comp_names/BIHOR.csv"
        org_data.only_info_comp_names_file(path_file)
        dict_keys_left = ['cod_fiscal', 'nume', 'loc', 'str', 'nr', 'fax', 'sect', 'tel', 'cp', 'detalii_adresa',
                          'bloc', 'scara', 'etaj', 'ap', 'tva']
        with open(path_file, 'r', encoding="utf8") as csv_f:
            cvs_reader = csv.DictReader(csv_f)

            for row in cvs_reader:
                self.assertTrue(len(dict_keys_left), len(row))

if __name__ == '__main__':
    unittest.main()
