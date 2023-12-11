import pandas as pd

class DataCleaning:
    def __init__(self):
        # Initialization
        pass

    # Method to clean data from a CSV file
    def clean_csv_data(self, data):
        pass

    # Method to clean data from API response
    def clean_api_data(self, data):
        pass

    # Task 3.6: Add the clean_user_data method to the DataCleaning class
    def clean_user_data(self, data):
        pass

    # Task 4.3: Extracting users and cleaning card details. Create a method called clean_card_data in your DataCleaning class to clean the data
    def clean_card_data(self, data):
        # Ensure data is a pandas DataFrame
        if not isinstance(data, pd.DataFrame):
            raise ValueError("Data must be a pandas DataFrame")

        data = data.dropna()  # Removing any rows with NULL values
        data = data[data > 0]  # Removing rows where value is <= 0

        return data

    # Task 5.4: Create a method in the DataCleaning class called_clean_store_data which cleans the data retrieve from the API 
    def clean_store_data(self, data):
        # Ensure data is a pandas DataFrame
        if not isinstance(data, pd.DataFrame):
            raise ValueError("Data must be a pandas DataFrame")

        cleaned_data = data.dropna()  # Removing rows with NULL values
        cleaned_data['some_column'] = cleaned_data['some_column'].astype('desired_data_type')  # Correcting data types by converting a column to a specific data type
        cleaned_data = cleaned_data.drop_duplicates()  # Removing duplicates rows

        return cleaned_data
    
    # Task 7.3: Retrieve and Clean Orders Table
    def clean_orders_data(self, orders_data):
        cleaned_orders_data = orders_data.drop(['first_name', 'last_name', '1'], axis=1)  # Remove specified columns

