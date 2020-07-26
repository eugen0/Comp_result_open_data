import unittest, urllib, ssl
import utility.get_data.get_data as get_data


class GetData(unittest.TestCase):

    def test_finding_comp_name(self):
        try:
            res = get_data.find_companies_name_dict()
        except urllib.error.URLError as url_error:
            print(url_error)
        except ssl.SSLError as ssl_error:
            print(ssl_error)
        self.assertTrue(len(res) > 0)


if __name__ == '__main__':
    unittest.main()
