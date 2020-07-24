from utility.org_data import org_data_controller
from utility.db import db_controller


########          importing data           ##################
#import companies name files
#dir_path = "../utility/data/comp_names"
#get_data_controller.import_comp_names_files(dir_path)

# import companies data based on years 
#path = "../utility/data/comp_data"
#years =["2008", "2009", "2010", "2011", etc] unfinished
#get_data_controller.import_comp_data(path, 2008)


#######          organising  data            ##################
## comp names
# get a list of paths of file_manes from given dir
#dir_path = "../utility/data/comp_names"
#filepaths_list = org_data_controller.get_list_path_files(dir_path)

# reading data from comp_names and keeps only identification information
#org_data_controller.reading_comp_name_files(dir_path, filepaths_list)


# not finished
# comp_data
#get list of files of comp_data
#dir_comp_data = "../utility/data/comp_data"
#comp_data_files = org_data_controller.get_list_path_files(dir_comp_data)





####### exporting into db ########

# exporting to db comp names
dir_path = "../utility/data/comp_names"
db_name = "postgres"
user = "postgres"
db_password = ""
host = "localhost"
db_controller.export_comp_names(dir_path, db_name, user, db_password, host)
