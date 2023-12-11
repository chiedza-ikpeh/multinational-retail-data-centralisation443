# Step 8: Once extracted and cleaned use the upload_to_db method 
# This will STORE the data in your sales_data database in a table named dim_users.

import pandas as pd
from database_utils import DatabaseConnector
from data_extraction import DataExtractor
from data_cleaning import DataCleaning

def extract_clean_data():
   # Task 3: Extracting and cleaning the user data
   # Initialise all classes
   
    db_connector = DatabaseConnector('C:/Users/SamuelIkpeh/Downloads/import_local/db_creds.yaml')
    extractor = DataExtractor()
    cleaner = DataCleaning()
    tables = db_connector.list_db_tables()  # List tables and read data sets
    print("Available tables:", tables) # Print available tables
    
    user_data_df = extractor.read_rds_table(db_connector, 'your_user_data_table_name')
    clean_user_data_df = cleaner.clean_user_data(user_data_df) # Clean data set
    
    db_connector.upload_to_db(clean_user_data_df, 'dim_users') # Upload cleaned data to the database

def extract_clean_users():
    # Task 4: Extracting users and cleaning card details
    # Initialise the DataCleaning class
    
    data_cleaner = DataCleaning() # Clean data
    data = pd.read_csv('s3://data-handling-public/products.csv') # Load data
    cleaned_data = data_cleaner.clean_card_data(data) # Extract clean data
    db_connector = DatabaseConnector('C:/Users/SamuelIkpeh/Downloads/import_local/db_creds.yaml') #Initialise database
    
    db_connector.upload_to_db(cleaned_data, 'dim_card_details') # Upload data

def extract_clean_store_data():
    # Task 5: Extracting clean details of each store
    # Initialise all classes
    
    db_connector = DatabaseConnector(db_creds)  # Initialise with database credentials
    db_creds = "C:/Users/SamuelIkpeh/Downloads/import_local/db_creds.yaml"
    data_extractor = DataExtractor() # Extract data
    stores_data = data_extractor.retrieve_stores_data("https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/store_details", {"x-api-key": "your_api_key"})
    data_cleaner = DataCleaning() # Clean data
    cleaned_data = data_cleaner._clean_store_data(stores_data)

    db_connector.upload_to_db(cleaned_data, 'dim_store_details')  # Upload the cleaned data to the database

def extract_clean_products():
    # Task 6: Extracting clean data to database
    # Initialising all classes

    data_extractor = DataExtractor()  # Initialise DataExtractor
    data_cleaner = DataCleaning() # Initialise DataCleaning
    db_connector = DatabaseConnector(db_creds)  # Initialise DatabaseConnector with db credentials
    db_creds = "C:/Users/SamuelIkpeh/Downloads/import_local/db_creds.yaml"
    products_df = data_extractor.extract_from_s3('s3://data-handling-public/products.csv')  # Step 1: Extract data from S3
    products_df = data_cleaner.convert_product_weights(products_df) # Step 2: Convert product weights
    cleaned_products_df = data_cleaner.clean_products_data(products_df) # Step 3: Clean product data
    db_connector.upload_to_db(cleaned_products_df, 'dim_products') # Step 4: Upload the cleaned data to the database

def extract_clean_orders():
    # Task 7.4:Upload Cleaned Orders Data to Database
    # Initialising all classes
    
    data_cleaner = DataCleaning() # Initialise your DataCleaning
    db_connector = DatabaseConnector(db_creds)  # Initialise DatabaseConnector with your db credentials
    db_creds = "C:/Users/SamuelIkpeh/Downloads/import_local/db_creds.yaml"
    cleaned_orders_data = data_cleaner.clean_orders_data(orders_data) # Clean orders data
    orders_table_name = "name_of_orders_table"  # Replace with the actual name of the orders table
    orders_data = db_connector.read_rds_table(orders_table_name)   
    db_connector.upload_to_db(cleaned_orders_data, 'orders_table') # Upload the cleaned orders data to the database
