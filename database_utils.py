# Task 2a: Create a new python script names database_utils.py
# Task 2b: Create a class named DatabaseConnector

import yaml 
from sqlalchemy import create_engine
import pandas as pd

class DatabaseConnector:
    def __init__(self, db_creds):
        self.db_creds = db_creds
        self.engine = None

    # Step 2: Create a method read_db_creds 
    # This will READ the credentials yaml file and return a dictionary of the credentials.

    def read_db_creds(self):
        with open("C:/Users/SamuelIkpeh/Downloads/import_local/db_creds.yaml", 'r') as file:
            return yaml.safe_load(file)

    # Step 3: Create a method init_db_engine 
    # This will READ the credentials from the return of read_db_creds and initialise and return an sqlalchemy database engine.

    def init_db_engine(self):
        creds = self.read_db_creds()
        connection_string = f"postgresql://{creds['username']}:{creds['password']}@{creds['host']}:{creds['port']}/{creds['database']}"
        self.engine = create_engine(connection_string)
        return self.engine
    
    # Step 4: Create a method list_db_table 
    # This will LIST all the tables in the database so you know which tables you can extract data from.

    def list_db_tables(self):
        engine = self.init_db_engine()
        return engine.table_names()
    
    # Step 7: Add the upload_to_db method to the DatabaseConnector class
    # This will TAKE in a Pandas DataFrame and table name to upload to as an argument.

    def upload_to_db(self, data, table_name):
        engine = self.init_db_engine()
        data.to_sql(table_name, engine, index=False, if_exists='replace')

     # Task 7.1: Extract Orders Data
    def list_orders_table(self):

        all_tables = self.db_connector.list_db_tables()  # List all tables in the database
        return all_tables


