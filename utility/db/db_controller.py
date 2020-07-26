import psycopg2, os, csv
from utility.org_data.org_data_base import build_filename_path


def build_inset_tbl_comp_name(dir_path, file):
    """
    imports CREATE TABLE Command from Company tables located in db_create_tab_comp_names.sql
    :return: string of create table cmd
    """
    # build paths
    file_list = os.listdir(dir_path)
    index = file_list.index(file)
    file_path = os.path.join(dir_path, file_list[index])

    # open sql text
    with open(file_path, 'r') as sql_f:
        tbl_command = sql_f.readlines()
        cmd = ""
        for line in tbl_command:
            cmd += line

    return cmd


def build_insert_cmd_comp_name(file_row):
    """
    builds insert statement based on values found in row provided
    :param file_row: row from files
    :return: insert statement
    """
    fst_part_cmd = "INSERT INTO Company ("
    sec_part_cmd = "VALUES ("
    for x in file_row:
        # if missing values no need for column
        if not file_row[x]:
            continue
        else:
            # add column
            fst_part_cmd += x + ','

            # add values
            sec_part_cmd += "'" + file_row[x] + "'" + ','


    # remove last (,), # add closing bracket and ;
    fst_part_cmd = fst_part_cmd[:len(fst_part_cmd)-1] + ') '
    sec_part_cmd = sec_part_cmd[:len(sec_part_cmd)-1] + ');'

    insert_cmd = fst_part_cmd+sec_part_cmd
    return insert_cmd


def export_comp_names(dir_path, db_name_, user_, password_, host_ ):
    """
    creates table in db with names of companies from dir
    :param files_list: list of files to extract data from
    :return: none
    """
    #### create a table in db ######
    # connect to db
    db = psycopg2.connect(database=db_name_, user=user_, password=password_, host=host_)

    # get the cursor
    cursor = db.cursor()

    # build paths
    db_path = "../utility/db"
    file = "db_create_tab_comp_name.sql"

    # inset table cmd
    cmd = build_inset_tbl_comp_name(db_path, file)

    # execute create table
    cursor.execute(cmd)

    # commit command
    db.commit()

    # create file list from dir
    files_list = build_filename_path(dir_path)

    # delete explicatii.csv, do not need this one
    #files_list.remove("explicatii.csv")

    # main loop
    for file in files_list:
        # delete explicatii.csv, do not need this one
        if file == "explicatii.csv":
            os.remove(os.path.join(dir_path, file))
            continue

        file_path = os.path.join(dir_path, file)

        # read file and export to db
        with open(file_path, 'r', encoding='utf-8') as cvs_in:
            csv_reader = csv.DictReader(cvs_in)
            next(csv_reader)        # skip first row

            print("inserting {}".format(file))
            for row in csv_reader:
                insert_command = build_insert_cmd_comp_name(row)

                # insert into db
                cursor.execute(insert_command)
            print("finished inserting {}".format(file))

    # close db conn
    db.commit()
    db.close()






