import unittest
import utility.url.url_response as url
import urllib, ssl

class UrlResponse(unittest.TestCase):


    def test_url_exist(self):
        """ test url works retunr a succes parameter"""
        address = 'https://data.gov.ro/api/3/action/package_list'
        try:
            test_url = url.valid_url(address)
            self.assertTrue(test_url)
        except urllib.error.URLError as url_error:
            print(url_error)
        except ssl.SSLError as ssl_error:
            print(ssl_error)


    # url get a response
    def test_url_res_carry_something(self):
        """ test if url response carry any load eg. response result ['value', 'value'] """
        address = 'https://data.gov.ro/api/3/action/package_list'
        try:
            respons = url.get_avlb_package(address)
            pos = len(respons)
            self.assertTrue(pos > 0)

        except urllib.error.URLError as url_error:
            print(url_error)
        except ssl.SSLError as ssl_error:
            print(ssl_error)




if __name__ == '__main__':
    unittest.main()
