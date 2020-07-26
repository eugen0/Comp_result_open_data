import unittest
#from utility.org_data import org_data
import utility.org_data.org_data_base as org_data
import csv

class MyTestCase(unittest.TestCase):
    def test_build_filenames_path(self):
        dir = ".//utility//data//comp_names"
        list_file_names = org_data.build_filename_path(dir)
        self.assertEqual(len(list_file_names), 43)

    def test_keep_only_comp_name_info(self):
        pass

if __name__ == '__main__':
    unittest.main()
