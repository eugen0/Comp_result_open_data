from utility.org_data import org_data_base
import os


def get_list_path_files(dir_path):
    """
        get a list of paths to available files in given folder
    :param dir_path: folder to look for files
    :return: list of paths to files
    """
    return org_data_base.build_filename_path(dir_path)


def reading_comp_name_files(dir_path, list_file):
    """
    calls function to save only comp ident information from files provided and dir
    :param dir_path: dir where files are located
    :param list_file: file list
    :return: none
    """
    org_data_base.only_info_comp_names_files(dir_path, list_file)


def reading_comp_data_files(dir_path, file):
    pass