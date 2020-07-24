import os,csv


def build_filename_path(dir_path):
    """
    create a list of paths to filename in given dir
    :param dir_path: dir to look into
    :return: list of paths
    """
    list_of_files = os.listdir(dir_path)
    return list_of_files


def only_info_comp_names_files(dir_path, file_list):
    """
    Reads list of files, build paths to that files, read content of the file
    and save in another file in the same dir only identification of that company  and delete old file
    :param dir_path: dir where files are located
    :param file_list: file list
    :return: none
    """

    dict_keys = ['cod_fiscal', 'nume', 'stare', 'tva', 'loc', 'sect', 'str', 'nr', 'fax', 'tel', 'cp',
                      'detalii_adresa', 'bloc', 'scara', 'etaj', 'ap']

    # creating file_path from list given and accessing file
    for file in file_list:
        # delete explicatii.csv, do not need this one
        if file == "explicatii.csv":
            os.remove(os.path.join(dir_path, file))
            continue

        file_path = os.path.join(dir_path, file)

            # reading date from file
        with open(file_path, 'r', encoding='utf-8') as csv_out:
            csv_reader = csv.DictReader(csv_out)
            next(csv_reader)                            # skip fist row
            print("trimming {}".format(file))

            # creating new file and write good values:
            new_file = "New_" + file
            new_file_path = os.path.join(dir_path, new_file)

            with open(new_file_path, 'w', encoding='utf-8') as csv_in:
                csv_writer = csv.DictWriter(csv_in, fieldnames=dict_keys, delimiter=',')
                csv_writer.writeheader()
                for row in csv_reader:
                    csv_writer.writerow({'cod_fiscal': row['cod_fiscal'], 'nume': row['nume'], 'stare': row['stare'],
                                         'tva': row['tva'], 'loc': row['loc'], 'sect': row['sect'], 'str': row['str'],
                                         'nr': row['nr'], 'fax': row['fax'], 'tel': row['tel'], 'cp': row['detalii_adresa'],
                                         'bloc': row['bloc'], 'scara': row['scara'], 'etaj': row['etaj'], 'ap': row['ap']})
            csv_in.close()
        csv_out.close()
        print('finished with trimming {}'.format(file_path))

        # deleting old file
        os.remove(file_path)






def read_comp_data_file(file_path):
    pass