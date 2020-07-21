import unittest
from utility.get_data.get_data import *


class GetData(unittest.TestCase):

    def test_finding_comp_name(self):
        res = find_companies_name_dict()
        self.assertTrue(len(res) > 0)


if __name__ == '__main__':
    unittest.main()
