from urllib.request import urlopen
import json


def valid_url(url):
    """
     check if url return success

    :param url: eg.'https://data.gov.ro/api/3/action/package_list'

    :return: returns bool from success status of url
    """

    response = urlopen(url).read()
    json_format = json.loads(response)
    return json_format['success']

# get available packages
def get_avlb_package(url):
    """
    Checks if url returns a payload

    :param url: eg. 'https://data.gov.ro/api/3/action/package_list'

    :return: expected a list of available payload if 0
    """

    response = urlopen(url).read()
    json_data = json.loads(response)
    return json_data['result']






