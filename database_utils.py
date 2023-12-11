import yaml
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import pandas as pd

class DatabaseConnector:
    def __init__(self, db_creds):
        self.db_creds = db_creds
        self.engine = None

    def _initialise_engine(self):
        creds = self.load_database_credentials()
        connection_string = f"postgresql://{creds['username']}:{creds['password']}@{creds['host']}:{creds['port']}/{creds['database']}"
        self.engine = create_engine(connection_string)

    def load_database_credentials(self) -> dict:
        """Load the database credentials from a YAML file."""
        with open("C:/Users/SamuelIkpeh/Downloads/import_local/db_creds.yaml", 'r') as file:
            return yaml.safe_load(file)

    def initialise_database_engine(self):
        """Initialize the database engine."""
        self._initialize_engine()
        return self.engine

    def list_database_tables(self):
        """List all tables in the database."""
        self._initialize_engine()
        return self.engine.table_names()

    def upload_dataframe_to_table(self, data: pd.DataFrame, table_name: str):
        """Upload a Pandas DataFrame to a specified table."""
        self._initialize_engine()
        data.to_sql(table_name, self.engine, index=False, if_exists='replace')

    def _initialise_engine_and_get_session(self) -> Session:
        """Initialize the engine and get a session."""
        self._initialize_engine()
        return Session(bind=self.engine)

    # Task 7.1: Extract Orders Data
    def get_orders_tables(self):
        """Get all tables related to orders."""
        return self.list_database_tables()

if __name__ == "__main__":
    pass



