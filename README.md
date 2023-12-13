# Project Title:

 Multinational Retail Data Centralisation

## Table of Contents

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [License](#license)

## Description

You work for a multinational company that sells various goods across the globe. Currently, their sales data is spread across many different data sources making it not easily accessible or analysable by current members of the team. In an effort to become more data-driven, your organisation would like to make its sales data accessible from one centralised location. Your first goal will be to produce a system that stores the current company data in a database so that it's accessed from one centralised location and acts as a single source of truth for sales data. You will then query the database to get up-to-date metrics for the business.

## Files Included

1. data_all_processes.py: *This script contains the implementation of all data processing functions for the project. It likely orchestrates various steps involved in data manipulation, transformation, and analysis*.

2. data_cleaning.py: *This script focuses on cleaning and pre-processing raw data. It likely includes functions to handle missing values, outliers, and other data quality issues*.

3. data_extraction.py: In this script, you can find functions responsible for extracting data from various sources. This may include connecting to APIs, scraping websites, or reading from different file formats*.

4. data_schema.py: This script defines the schema or structure of the data used in the project. It could include class definitions, database table structures, or other specifications regarding how data is organised*.

5. data_stores.py: *This script contains functions related to storing processed data. This may involve interactions with databases, file systems, or other storage solutions to persist the cleaned and transformed data*.

6. database_utils.py: *This script provides utility functions for working with databases. It could include functions for connecting to a database, executing queries, or managing database connections efficiently*.

7. data_query.py: *This script is dedicated to handling data queries and analytics. It contains functions or methods for retrieving specific insights from the processed data.*.

## Installation

To install this project, follow these steps:

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/chiedza-ikpeh/multinational-retail-data-centralisation443.git
    ```

2. Navigate to the project directory:

    ```bash
    cd multinational-retail-data-centralisation443
    ```

3. Install the project dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up the database credentials:

    - Create a YAML file named `db_creds.yaml` in the project root.
    - Add the following content and replace with your actual database credentials:

    ```yaml
    username: your_username
    password: your_password
    host: your_host
    port: your_port
    database: your_database
    ```

5. Initialise the database:

    ```bash
    python src/main.py init_db
    ```


## Usage

To use this project, follow these steps:

1. Extract data from PDFs:

    ```bash
    python src/main.py extract_pdf_data --link (https://data-handling-public.s3.eu-west-1.amazonaws.com/card_details.pdf)
    ```

2. Clean and upload card data:

    ```bash
    python src/main.py clean_and_upload_card_data
    ```

3. Retrieve store details from the API:

    ```bash
    python src/main.py retrieve_stores_data
    ```

4. Explore the database:

    ```bash
    python src/main.py explore_database
    ```

## File Structure

- /src
  - main.py
- /data
  - input_data.csv
- /docs
  - documentation.md

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
