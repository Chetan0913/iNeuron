import hive_python

# To create database
hive_python.create_database('hive_challange_1')

# To create a csv temp table
hive_python.create_table_csv_temp('hive_challange_1','department_data_temp_table_1')

# load data to csv table 
hive_python.load_data('hive_challange_1','department_data_temp_table_1')

# create table orc permanent
hive_python.create_table_orc_permanent('hive_challange_1','department_data_temp_table_1','department_data_perm_table_1')

# sort the table and show in dataframe (table_name, database_name)
hive_python.show_sorted_dataframe('hive_challange_1','department_data_perm_table')

# drop the csv table
hive_python.drop_temp_table('hive_challange_1','department_data_temp_table')

# to store the rows_data into list of tuples
hive_python.df_rows_details('hive_challange_1','department_data_perm_table')