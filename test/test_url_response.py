import unittest
import utility.url.url_response as url


class UrlResponse(unittest.TestCase):

    def test_url_exist(self):
        ''' test url works retunr a succes parameter'''
        address = 'https://data.gov.ro/api/3/action/package_list'
        test_url = url.valid_url(address)
        self.assertTrue(test_url)

    # url get a response
    def test_url_res_carry_something(self):
        ''' test if url response carry any load eg. response result ['value', 'value'] '''
        address = 'https://data.gov.ro/api/3/action/package_list'
        respons = url.get_avlb_package(address)
        ret = respons['result']
        pos = len(ret)
        self.assertTrue(pos > 0)


if __name__ == '__main__':
    unittest.main()