from urllib.parse import urlparse, urljoin

def build_url(base, path):
    ''' Buil general purpose ulr
    :param base: eg. "https://data.gov.ro/api/3/action/",
    :param path: eg. "package_list"

    :return: "https://data.gov.ro/api/3/action/package_list"
    '''

    return urljoin(base, path)


def build_url_by_id(base, package, tag):
    '''
    Building url by providing base, path, id :

    :param base: eg. "https://data.gov.ro/api/3/action/"
    :param package: eg. "package_show"
    :param tag: eg. "venit-net"

    :return: "https://data.gov.ro/api/3/action/package_show?id=venit-net"
    '''

    path = package + '?id=' + tag
    return urljoin(base, path)

def build_url_package_query(base,query):
    '''
    Getting url based of search of package:

    :param base: eg."https://data.gov.ro/api/3/action/"
    :param query: 'jandarmeria'

    :return: eg."https://data.gov.ro/api/3/action/package_search?q=jandarmeria"
    '''

    path = 'package_search?q=' + query
    return urljoin(base, path)

def build_url_resource_query(base, query):
    '''
    Building url for resource search :

    :param base: "https://data.gov.ro/api/3/action/"
    :param query: "agentia-nationala-a-functionarilor-publici"

    :return: https://data.gov.ro/api/3/action/resource_search?query=name:agentia-nationala-a-functionarilor-publici
    '''

    path ='resource_search?query=name:' + query
    return urljoin(base, path)