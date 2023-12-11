import requests

class StoreAPI:
    def __init__(self, base_url, api_key):
        self.base_url = base_url
        self.headers = {"x-api-key": api_key}

    def _make_request(self, endpoint):
        """Make a request to the API endpoint"""
        response = requests.get(f"{self.base_url}/{endpoint}", headers=self.headers)
        return response

    def get_store_details(self, store_number):
        """Retrieve details of a specific store"""
        response = self._make_request(f"store_details/{store_number}")
        if response.status_code == 200:
            return response.json()
        else:
            return f"Error: {response.status_code}"

    def get_number_of_stores(self):
        """Retrieve the total number of stores"""
        response = self._make_request("number_stores")
        if response.status_code == 200:
            return response.json()
        else:
            return f"Error: {response.status_code}"
