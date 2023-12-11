# Step 1: Create a new python script names data_cleaning.py
# Step 2: Create a class named DataCleaning

import pandas as pd

class DataCleaning:
    def __init__(self):
        # Initialisation
        pass

    # Method to clean data from a CSV file
    def clean_csv_data(self, data):
        pass

    # Method to clean data from API response
    def clean_api_data(self, data):
        pass

    # Method to clean data from S3 bucket
    def convert_product_weights(self, products_df):
        """
        Converts various weight units in the DataFrame to kilograms.

        :param products_df: pandas DataFrame with a 'weight' column.
        :return: pandas DataFrame with weights converted to kg.
        """
        def convert_to_kg(weight):
            # Remove non-numeric and non-decimal characters
            numeric_weight = ''.join(filter(str.isdigit, weight))

            # Convert based on unit
            if 'ml' in weight or 'g' in weight:
                # Convert grams or milliliters to kilograms (assuming 1ml = 1g)
                return float(numeric_weight) / 1000
            elif 'kg' in weight:
                # Already in kilograms
                return float(numeric_weight)
            else:
                # Default case, if unit is unknown or missing
                return None

        # Apply conversion to each row in the 'weight' column
        products_df['weight'] = products_df['weight'].apply(convert_to_kg)

        return products_df
    
    def clean_products_data(self, products_df):
        """
        Cleans the products DataFrame to remove additional erroneous values.

        :param products_df: pandas DataFrame containing product data
        :return: Cleaned pandas DataFrame
        """
        # Remove duplicates if any
        cleaned_df = products_df.drop_duplicates()

        # Handle missing values
        # For example, you can fill missing values with a default value or drop them
        cleaned_df = cleaned_df.fillna('Unknown')  # Replace 'Unknown' with an appropriate value

        # Further cleaning steps can be added here based on the specific requirements of your dataset

        return cleaned_df
    
    # Task 3.6: # Add the clean_user_data method to the DataCleaning class
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

        cleaned_data = data.dropna() # Removing rows with NULL values
        cleaned_data['some_column'] = cleaned_data['some_column'].astype('desired_data_type') # Correcting data types by converting a column to a specific data type
        cleaned_data = cleaned_data.drop_duplicates()  # Removing duplicates rows

        return cleaned_data
    
    # Task 7.3: Retrieve and Clean Orders Table
    def clean_orders_data(self, orders_data):
        
        cleaned_orders_data = orders_data.drop(['first_name', 'last_name', '1'], axis=1) # Remove specified columns

        return cleaned_orders_data
