from utility.db.util_db import Db


# importing data into database
class ImportCompName(Db):
    def __init__(self, db_config_path, config_section, file_dir_path):
        super().__init__(db_config_path, config_section)
        self.file_dir_par = file_dir_path

    def read_comp_name(self):
        pass

    def read_insert_sql_file(self):
        pass





db = Db()
# connect
db.connect()

# do stuff

# close
db.disconnect()

