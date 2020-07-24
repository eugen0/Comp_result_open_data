import unittest
#from utility.get_data.get_data import find_companies_name_dict
import utility.get_data.get_data as get_data


class GetData(unittest.TestCase):

    def test_finding_comp_name(self):
        res = get_data.find_companies_name_dict()
        self.assertTrue(len(res) > 0)


if __name__ == '__main__':
    unittest.main()
