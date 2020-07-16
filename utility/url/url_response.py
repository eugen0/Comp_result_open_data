from urllib.request import urlopen

import json
# valid url
def valid_url(url):
    response = urlopen(url).read()
    json_format = json.loads(response)
    return json_format['success']

# get available packages
def get_avlb_package(url):
    respose_test = urlopen(url).read()
    json_data_test = json.loads(respose_test)
    return json_data_test






