from utility.org_data import org_data
import os


def get_list_path_files(dir_path):
    """
        get a list of paths to available files in given folder
    :param dir_path: folder to look for files
    :return: list of paths to files
    """
    return org_data.build_filename_path(dir_path)


def reading_comp_name_files(dir_path, file):
    """
    reads comp name file as dict with file data
    :param dir_path: dir where file is located
    :param file: file name
    :return: calling read_com_names_file()
    """
    file_path = os.path.join(dir_path, file)
    return org_data.only_info_comp_names_file(file_path)


def reading_comp_data_files(dir_path, file):
    pass