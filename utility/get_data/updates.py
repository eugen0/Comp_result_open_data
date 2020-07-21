from utility.url import url_response, url_build


def check_package_updates():
    """
    checks for available package updates 
    :return: avilable package update
    """
    address = "https://data.gov.ro/api/3/action/recently_changed_packages_activity_list"
    return url_response.get_avlb_package(address)
