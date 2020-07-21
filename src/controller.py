from utility.get_data import get_data_controller
from utility.org_data import   org_data_controller


############ importing data ##################
#import companies name files

#dir_path = "../utility/data/comp_names"
#get_data_controller.import_comp_names_files(dir_path)

# import companies data based on years 
#path = "../utility/data/comp_data"
#years =["2008", "2009", "2010", "2011", etc]
#get_data_controller.import_comp_data(path, 2008)


####### organising  data ##################

# get a list of paths of file_manes from given dir
dir_path = "../utility/data/comp_names"
filepaths_list = org_data_controller.get_list_path_files(dir_path)

# remove explicatii.csv
filepaths_list.remove('explicatii.csv')

# reading data from comp_names and keeps only identification information
for x in filepaths_list:
    org_data_controller.reading_comp_name_files(dir_path, x)

