from utility.get_data import get_data
from utility.url import url_build


# check for companies name and import the available files
def import_comp_names_files(path):
    """
    Imports comp names files to the path spec

    :param path: path where to save files
    :return: none
    """
    comp_dict = get_data.find_companies_name_dict()
    get_data.download_files_from_dict(comp_dict, path)

# check for companies data and import files
def import_comp_data(path, year):
    """
    Importing financial data of specified year

    :param path: path where to save data
    :param year: fiancial year interested
    :return: none
    """
    # build url
    base = "https://data.gov.ro/api/3/action/"
    p = "package_show"
    q = "situatii_financiare_" + str(year)
    address = url_build.build_url_by_id(base, p, q)


    # getting dict of resources and url
    data_dict = get_data.get_comp_data_dic(address)

    # download files from dict
    get_data.download_files_from_dict(data_dict, path)