# Step 1a: Create a new python script names data_extraction.py
# Step 1b: Create a class named DataExtractor

import boto3
import pandas as pd
import tabula
import requests
from io import StringIO

class DataExtractor:
    def __init__(self):
        # Initialisation
        pass

    # Method to extract data from a CSV file
    def from_csv(self, file_path):
        pass

    # Method to extract data from an API
    def from_api(self, api_url):
        pass

    # Task 3.5: Add the read_rds_table method to the DataExtractor class
    def read_rds_table(self, db_connector, table_name):
        engine = db_connector.init_db_engine()
        return pd.read_sql_table(table_name, engine)
    
    # Task 4.2: Create a method in your DataExtractor class called retrieve_pdf_data
    def retrieve_pdf_data(self, link):
        try:
            # Extract tables from all pages of the PDF
            dfs = tabula.read_pdf("https://data-handling-public.s3.eu-west-1.amazonaws.com/card_details.pdf", pages='all')

            # Combine all tables into a single DataFrame
            combined_df = pd.concat(dfs, ignore_index=True)
            return combined_df
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    # Task 5.1: Create a method in your DataExtractor class called list_number_of_stores      
    def list_number_of_stores(self, endpoint, headers):
        response = requests.get(endpoint, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            return f"Error: {response.status_code}"

    # Task 5.3: Create another method retrieve_stores_data which will take the retrieve a store endpoint as an argument     
    def retrieve_stores_data(self, base_endpoint, headers):
        number_of_stores = self.list_number_of_stores(base_endpoint + "/number_stores", headers)
        store_data = []

        for store_number in range(1, number_of_stores + 1):
            store_endpoint = f"{base_endpoint}/store_details/{store_number}"
            response = requests.get(store_endpoint, headers=headers)
            if response.status_code == 200:
                store_data.append(response.json())
            else:
                print(f"Error retrieving store {store_number}: {response.status_code}")

        return pd.DataFrame(store_data)
    
    # Task 6.1: Extract and clean product details from an S3 bucket
    def from_s3_bucket(self, bucket_name, object_key):
        bucket_name = ('s3://data-handling-public/products.csv').split('/')[2] # Parse bucket name and file path from s3_path
        file_path = '/'.join('s3://data-handling-public/products.csv'.split('/')[3:])
        s3 = boto3.client('s3') # Initialise S3 client
        object_key = s3.get_object(Bucket=bucket_name, Key=file_path) # Get object from S3
        data = object_key['Body'].read().decode('utf-8')
        df = pd.read_csv(StringIO(data)) # Read data into pandas DataFrame
        
        return df
    
    #Task 7.2:
    def retrieve_orders_data(self, db_connector, orders_table_name):
        
        db_connector = DatabaseConnector(db_creds)  # Initialise with your database credentials
        db_creds = "C:/Users/SamuelIkpeh/Downloads/import_local/db_creds.yaml"
        orders_table_name = "name_of_orders_table"  # Replace with the actual name of the orders table
        orders_data = db_connector.read_rds_table(orders_table_name)
