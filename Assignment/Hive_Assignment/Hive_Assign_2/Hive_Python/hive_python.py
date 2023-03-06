import pyodbc 
import pandas as pd
import logging
import warnings

warnings.filterwarnings('ignore')

logging.basicConfig(filename="Log.txt", level=logging.DEBUG,filemode='a', format='%(asctime)s - %(message)s', datefmt= '%d-%b-%y %H:%M:%S')

def create_db(dbname):
    try:
        pyodbc.autocommit=True
        connection = pyodbc.connect('DNS=Hive_connection',autocommit=True)
        cur = connection.cursor()
        cur.execute("Create database {};".format(dbname))
        print("\n Database : {} is created successfully \n".format(dbname))
        logging.info("Database : {} is created succssfully".format(dbname))
    
    except Exception as e:
        logging.error(e)



def create_table(dbname,tablename):
    try:
        pyodbc.autocommit=True
        connection = pyodbc.connect("DSN=Hive_connection",autocommit=True)
        cur = connection.cursor()
        cur.execute('use {};'.format(dbname))
        cur.execute('create table {}(d_id int, d_name string, d_destin string, d_code int) row format delimited fields terminated by ',';'.format(tablename))
        print("\n {} is created successfully \n".format(tablename))
        logging.info('Table:- {} is created successfully'.format(tablename))

    except Exception as e:
        logging.error(e)


def load_data(dbname, tablename):
    
    try:
        pyodbc.autocommit = True
        connection = pyodbc.connect("DSN=Hive_connection", autocommit=True)
        cur = connection.cursor()
        cur.execute('use {}};'.format(dbname))
        cur.execute("load data inpath '/tmp/depart_data.csv' into table {};".format(tablename))
        print('\n data is loaded into {} \n'.format(tablename))
        logging.info('data is loaded into {}'.format(tablename))
        
    except Exception as e:
        logging.error(e)

def create_table_orc_permanent(dbname,tablename1,tablename2):
    
    try:
        pyodbc.autocommit = True
        connection = pyodbc.connect("DSN=Hive_connection", autocommit=True)
        cur = connection.cursor()
        cur.execute('use {}};'.format(dbname))
        cur.execute("create table {}(d_id int, d_name string, d_destin string, d_code int) row format delimited fields terminated by ',' stored as orc;".format(tablename2))
        cur.execute("insert overwrite into {} select * from {};".format(tablename2,tablename1))
        print('\n Table:- {} is created successfully with orc format\n'.format(tablename2))
        logging.info('\n Table:- Permanent table {} is created successfully'.format(tablename2))
        
    except Exception as e:
        logging.error(e)


def show_sorted_dataframe(dbname,tablename): 
    try:
        pyodbc.autocommit = True
        connection = pyodbc.connect("DSN=Hive_connection", autocommit=True)
        cur = connection.cursor()
        cur.execute("use {};".format(dbname))
        df = pd.read_sql("select * from {} sort by d_id Desc;".format(tablename),connection)
        print('\n sorting of table {} is under process..... \n'.format(tablename))
        print(df)
        logging.info('sorting of the table in descending order wrt d_id is done and table is displayed as dataframe')

    except Exception as e:
        logging.error(e)


def drop_temp_table(dbname,tablename):
    
    try:
        pyodbc.autocommit = True
        connection = pyodbc.connect("DSN=Hive_connection", autocommit=True)
        cur = connection.cursor()
        cur.execute('use {};'.format(dbname))
        cur.execute("drop table {};".format(tablename))
        print('\n Table:- Temprory csv table {} is deleted successfully \n'.format(tablename))        
        logging.info('Table:- Temprory csv table {} is deleted successfully'.format(tablename))
        
    except Exception as e:
        logging.error(e) 


def df_rows_details(dbname,tablename): 
    try:
        pyodbc.autocommit = True
        connection = pyodbc.connect("DSN=Hive_connection", autocommit=True)
        cur = connection.cursor()
        cur.execute("use {};".format(dbname))
        df = pd.read_sql("select * from {};".format(tablename),connection)
        
        records = df.to_records(index=False)
        result = list(records)
        print('\n converting the rows_data into python list of tuples \n') 
        print(result) 
         
    except Exception as e:
        logging.error(e)  
