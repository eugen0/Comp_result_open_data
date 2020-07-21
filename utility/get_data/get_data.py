from utility.url import url_response, url_build
from urllib.request import urlopen
import os

# get dict of comp names
def find_companies_name_dict():
    """
    Finds companies names and addresses
    :return: a dict with resource name eg.area of companies and url of available data

    """
    base = "https://data.gov.ro/api/3/action/"
    query = "Date-de-identificare-platitori"
    address = url_build.build_url_package_query(base, query)

    # dictionary with available files and download url
    data_platitori = {}

    # check for valid url
    packages_exists = url_response.valid_url(address)
    if packages_exists:
        # find available  packages
        avlb_package = url_response.get_avlb_package(address)

        # resources are at ['results'][0]['resources']
        resources = avlb_package['results'][0]['resources']

        # num avl resource
        num_resources = avlb_package['results'][0]['num_resources']

        # sanity check
        count = 0

        # loop over list and build a dict with name of resource and url
        for x in resources:
            package_name = x['name']
            package_url = x['url']
            temp_dict = {package_name: package_url}
            data_platitori.update(temp_dict)
            count += 1

        # sanity check
        if count == num_resources:
            print("all resources founded!")

        return data_platitori

    raise Exception("Invalid query to find companies names")


# download names and address of companies and save in data
def download_files_from_dict(dict, path):
    """
    Downloads files from given dict into path provided

    :param dict: dict with resource name and url address
    :param path: path where to save the files

    :return: none
    """
    if not os.path.exists(path):
        os.makedirs(path)

    # loop over dict and create files
    for x in dict:
        filename = "{}".format(x)
        print("Importing file: ", filename)
        response = urlopen(dict[x]).read()

        with open(os.path.join(path, filename), "wb") as f:
            f.write(response)
        f.close()

        print("Finished to import file: ", filename)


# get dic of comp data based of url
def get_comp_data_dic(address):
    """
    build a dict from data at address

    :param address: url address to download data
    :return: dic with comp activity areas and download url

    """
    ret_dict = {}

    # test address
    url_exists = url_response.valid_url(address)

    if url_exists:
        avl_packages = url_response.get_avlb_package(address)

        # resourse are at ['result']['resources']
        resources = avl_packages['resources']

        num_resources = avl_packages['num_resources']
        count = 0

        # loop over resources
        for x in resources:
            package_name = x['name']
            package_url = x['url']
            temp_dict = {package_name: package_url}
            ret_dict.update(temp_dict)
            count += 1

        # sanity check
        if count == num_resources:
            print("All resources founded!")

        return ret_dict

    raise Exception("Invalid query to find companies data")
