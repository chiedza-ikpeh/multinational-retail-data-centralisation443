import requests

class StoreAPI:
    def __init__(self):
        self.base_url = "https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod"
        self.headers = {
            "x-api-key": "yFBQbwXe9J3sd6zWVAMrK6lcxxr0q1lr2PT6DDMX"
        }

    def get_store_details(self, store_number):
        """Retrieve details of a specific store"""
        response = requests.get(f"{self.base_url}/store_details/{store_number}", headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            return f"Error: {response.status_code}"

    def get_number_of_stores(self):
        """Retrieve the total number of stores"""
        response = requests.get(f"{self.base_url}/number_stores", headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            return f"Error: {response.status_code}"
        
    