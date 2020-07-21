import unittest
import utility.url.url_build as build

class BuildUrl(unittest.TestCase):

    def test_build_url(self):
        ''' build of general url:
         base - "https://data.gov.ro/api/3/action/",
         path "package_list"
        expecting : "https://data.gov.ro/api/3/action/package_list" '''
        base = "https://data.gov.ro/api/3/action/"
        path = "package_list"
        address = build.build_url(base, path)
        self.assertEqual(address, "https://data.gov.ro/api/3/action/package_list")

    def test_build_url_by_id(self):
        ''' Testing building url by providing base, path, id :
            base : "https://data.gov.ro/api/3/action/"
            path : "package_show"
            id   : "venit-net"
        expected result : "https://data.gov.ro/api/3/action/package_show?id=venit-net"
        '''
        base = "https://data.gov.ro/api/3/action/"
        path = "package_show"
        id ="venit-net"
        address = build.build_url_by_id(base, path, id)
        self.assertEqual(address, "https://data.gov.ro/api/3/action/package_show?id=venit-net")

    def test_url_package(self):
        ''' Getting url base of search of package:
            base :"https://data.gov.ro/api/3/action/"
            package : 'jandarmeria'
        :return: "https://data.gov.ro/api/3/action/package_search?q=jandarmeria"
        '''
        q = 'jandarmeria'
        base = "https://data.gov.ro/api/3/action/"
        address = build.build_url_package_query(base, q)
        self.assertEqual(address,"https://data.gov.ro/api/3/action/package_search?q=jandarmeria")

    def test_url_search_query(self):
        ''' building url for resource search :
            base:"https://data.gov.ro/api/3/action/"
            query: "agentia-nationala-a-functionarilor-publici"
            :return https://data.gov.ro/api/3/action/resource_search?query=name:agentia-nationala-a-functionarilor-publici
            '''
        base = "https://data.gov.ro/api/3/action/"
        q = "agentia-nationala-a-functionarilor-publici"
        address = build.build_url_resource_query(base,q)
        self.assertEqual(address, "https://data.gov.ro/api/3/action/resource_search?query=name:agentia-nationala-a-functionarilor-publici")

if __name__ == '__main__':
    unittest.main()
