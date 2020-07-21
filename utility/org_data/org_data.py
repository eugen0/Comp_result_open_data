import os, csv


def build_filename_path(dir_path):
    """
    create a list of paths to filename in given dir
    :param dir_path: dir to look into
    :return: list of paths
    """
    list_of_files = os.listdir(dir_path)
    return list_of_files


def only_info_comp_names_file(file_path):
    """
    reads comp name file and keeps only identification information
    :param file_path: file_path
    :return: none
    """
    dict_keys_left = ['cod_fiscal', 'nume', 'loc', 'str', 'nr', 'fax', 'sect', 'tel', 'cp', 'detalii_adresa',
                 'bloc', 'stare','scara', 'etaj', 'ap', 'tva']

    with open(file_path, 'r+', encoding="utf8") as csv_f:
        csv_reader = csv.DictReader(csv_f)
        print("trimming {}".format(file_path))
        # here is the bug
        for row in csv_reader:
            for key in dict_keys_left:
                if key not in row:
                    del row[key]

        csv_f.close()
        print('finished with triming {}'.format(file_path))






def read_comp_data_file(file_path):
    pass