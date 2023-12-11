import boto3
import pandas as pd
import tabula
import requests
from io import StringIO

class DataExtractor:
    def __init__(self):
        # Initialization
        pass

    def extract_from_csv(self, file_path):
        pass

    def extract_from_api(self, api_url):
        pass

    def read_rds_table(self, db_connector, table_name):
        engine = db_connector.initialize_database_engine()
        return pd.read_sql_table(table_name, engine)

    def retrieve_pdf_data(self, link):
        try:
            dfs = tabula.read_pdf("https://data-handling-public.s3.eu-west-1.amazonaws.com/card_details.pdf", pages='all')
            combined_df = pd.concat(dfs, ignore_index=True)
            return combined_df
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def get_number_of_stores(self, endpoint, headers):
        response = requests.get(endpoint, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            return f"Error: {response.status_code}"

    def retrieve_stores_data(self, base_endpoint, headers):
        number_of_stores = self.get_number_of_stores(base_endpoint + "/number_stores", headers)
        store_data = []

        for store_number in range(1, number_of_stores + 1):
            store_endpoint = f"{base_endpoint}/store_details/{store_number}"
            response = requests.get(store_endpoint, headers=headers)
            if response.status_code == 200:
                store_data.append(response.json())
            else:
                print(f"Error retrieving store {store_number}: {response.status_code}")

        return pd.DataFrame(store_data)

    def extract_from_s3_bucket(self, s3_path):
        bucket_name = s3_path.split('/')[2]
        file_path = '/'.join(s3_path.split('/')[3:])
        s3 = boto3.client('s3')
        object_key = s3.get_object(Bucket=bucket_name, Key=file_path)
        data = object_key['Body'].read().decode('utf-8')
        df = pd.read_csv(StringIO(data))
        return df

    def retrieve_orders_data(self, db_connector, orders_table_name):
        db_connector.initialise_database_engine()
        orders_data = db_connector.read_rds_table(orders_table_name)
