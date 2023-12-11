import pandas as pd
from database_utils import DatabaseConnector
from data_extraction import DataExtractor
from data_cleaning import DataCleaning

class DataProcessing:
    def __init__(self):
        self.db_connector = DatabaseConnector('C:/Users/SamuelIkpeh/Downloads/import_local/db_creds.yaml')
        self.extractor = DataExtractor()
        self.cleaner = DataCleaning()

    def extract_clean_data(self):
        # Task 3: Extracting and cleaning the user data
        # Initialise all classes
        tables = self.db_connector.list_db_tables()  # List tables and read data sets
        print("Available tables:", tables)  # Print available tables

        user_data_df = self.extractor.read_rds_table(self.db_connector, 'your_user_data_table_name')
        clean_user_data_df = self.cleaner.clean_user_data(user_data_df)  # Clean data set

        self.db_connector.upload_to_db(clean_user_data_df, 'dim_users')  # Upload cleaned data to the database

    def extract_clean_users(self):
        # Task 4: Extracting users and cleaning card details
        # Initialise the DataCleaning class
        data = pd.read_csv('s3://data-handling-public/products.csv')  # Load data
        cleaned_data = self.cleaner.clean_card_data(data)  # Extract clean data

        self.db_connector.upload_to_db(cleaned_data, 'dim_card_details')  # Upload data

    def extract_clean_store_data(self):
        # Task 5: Extracting clean details of each store
        # Initialise all classes
        stores_data = self.extractor.retrieve_stores_data("https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/store_details", {"x-api-key": "your_api_key"})
        cleaned_data = self.cleaner._clean_store_data(stores_data)

        self.db_connector.upload_to_db(cleaned_data, 'dim_store_details')  # Upload the cleaned data to the database

    def extract_clean_products(self):
        # Task 6: Extracting clean data to database
        # Initialising all classes
        products_df = self.extractor.extract_from_s3('s3://data-handling-public/products.csv')  # Step 1: Extract data from S3
        products_df = self.cleaner.convert_product_weights(products_df)  # Step 2: Convert product weights
        cleaned_products_df = self.cleaner.clean_products_data(products_df)  # Step 3: Clean product data

        self.db_connector.upload_to_db(cleaned_products_df, 'dim_products')  # Step 4: Upload the cleaned data to the database

    def extract_clean_orders(self):
        # Task 7.4: Upload Cleaned Orders Data to Database
        # Initialising all classes
        cleaned_orders_data = self.cleaner.clean_orders_data(orders_data)  # Clean orders data
        orders_table_name = "name_of_orders_table"  # Replace with the actual name of the orders table
        orders_data = self.db_connector.read_rds_table(orders_table_name)

        self.db_connector.upload_to_db(cleaned_orders_data, 'orders_table')  # Upload the cleaned orders data to the database
