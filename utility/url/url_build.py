from urllib.parse import urlparse, urljoin

def build_url(base, path):
    return urljoin(base, path)


def build_url_by_id( base, package, tag):
    path = package + '?id=' + tag
    return urljoin(base,path)

def build_url_package_query(base,query):
    path = 'package_search?q=' + query
    return urljoin(base, path)

def build_url_resource_query( base, query):
    path ='resource_search?query=name:' + query
    return urljoin(base, path)