# Milestone 3: Creating a Database Schema
# Task 1: Cast columns in orders_table (assuming it is called dim_orders_table)

UPDATE dim_orders_table
SET
date_uuid = CAST(date_uuid AS UUID),
user_uuid = CAST(user_uuid AS UUID),
card_number = CAST(card_number AS INT),
store_code = CAST(store_code AS INT),
product_code = CAST(product_code AS INT),
product_quantity = CAST(product_quantity AS SMALLINT);
    
    # Task 9: Create foreign key constraints in orders_table

    # Reference dim_user_table
    ALTER TABLE orders_table
    ADD CONSTRAINT fk_orders_user
    FOREIGN KEY (user_uuid)
    REFERENCES dim_user_table (user_uuid);

    # Reference dim_store_details
    ALTER TABLE orders_table
    ADD CONSTRAINT fk_orders_store
    FOREIGN KEY (store_code)
    REFERENCES dim_store_details (store_code);

    # Reference dim_products_table
    ALTER TABLE orders_table
    ADD CONSTRAINT fk_orders_products
    FOREIGN KEY (product_code)
    REFERENCES dim_products_table (product_code);

    # Reference dim_dates_times
    ALTER TABLE orders_table
    ADD CONSTRAINT fk_orders_dates_times
    FOREIGN KEY (date_uuid)
    REFERENCES dim_dates_times (date_uuid);

    # Reference dim_card_details
    ALTER TABLE orders_table
    ADD CONSTRAINT fk_orders_card_details
    FOREIGN KEY (card_number)
    REFERENCES dim_card_details (card_number);


# Task 2: Cast columns in dim_user_table
ALTER TABLE dim_user_table
ADD PRIMARY KEY (user_uuid);

UPDATE dim_user_table
SET
    first_name = CAST(first_name AS VARCHAR(255)),
    last_name = CAST(last_name AS VARCHAR(255),
    date_of_birth = CAST(date_of_birth AS DATE),
    country_code = CAST(country_code AS VARCHAR(10)),
    join_date = CAST(join_date AS DATE);

# Task 3: Update dim_store_details
UPDATE dim_store_details
SET latitude = COALESCE(latitude1, latitude2);

# Task 4: Alter dim_store_details
ALTER TABLE dim_store_details
ADD PRIMARY KEY (store_code);

ALTER TABLE store_details_table
ALTER COLUMN longitude TYPE FLOAT,
ALTER COLUMN locality TYPE VARCHAR(255),
ALTER COLUMN store_code TYPE VARCHAR(20),
ALTER COLUMN staff_numbers TYPE SMALLINT,
ALTER COLUMN opening_date TYPE DATE,
ALTER COLUMN store_type TYPE VARCHAR(255) NULL,
ALTER COLUMN latitude TYPE FLOAT,
ALTER COLUMN country_code TYPE VARCHAR(10),
ALTER COLUMN continent TYPE VARCHAR(10);

UPDATE dim_store_details
SET location = 'N/A'
WHERE location IS NULL;

# Task 5: Update dim_products_table
UPDATE dim_products_table
SET product_price = REPLACE(product_price, '£', '');

ALTER TABLE dim_products_table
ADD COLUMN weight_class VARCHAR(255);

UPDATE dim_products_table
SET weight_class =
    CASE
        WHEN weight < 2 THEN 'Light'
        WHEN weight >= 2 AND weight < 40 THEN 'Mid_Sized'
        WHEN weight >= 40 AND weight < 140 THEN 'Heavy'
        WHEN weight >= 140 THEN 'Truck_Required'
    END;

ALTER TABLE dim_products_table
ADD PRIMARY KEY (product_code);

ALTER TABLE products_table
ALTER COLUMN product_price TYPE FLOAT,
ALTER COLUMN weight TYPE FLOAT,
ALTER COLUMN EAN TYPE VARCHAR(20),
ALTER COLUMN product_code TYPE VARCHAR(20),
ALTER COLUMN date_added TYPE DATE,
ALTER COLUMN uuid TYPE UUID,
ALTER COLUMN still_available TYPE BOOLEAN,
ALTER COLUMN weight_class TYPE VARCHAR(20);

# Task 6: Update dim_dates_times
ALTER TABLE dim_dates_times
ADD PRIMARY KEY (date_uuid);

ALTER TABLE dim_dates_times
ALTER COLUMN month TYPE VARCHAR(10),
ALTER COLUMN year TYPE VARCHAR(4),
ALTER COLUMN day TYPE VARCHAR(2),
ALTER COLUMN time_period TYPE VARCHAR(50),
ALTER COLUMN date_uuid TYPE UUID;

# Task 7: Update dim_card_details
ALTER TABLE dim_card_details
ADD PRIMARY KEY (card_number);

ALTER TABLE dim_card_details
ALTER COLUMN card_number TYPE VARCHAR(16),
ALTER COLUMN expiry_date TYPE VARCHAR(10),
ALTER COLUMN date_payment_confirmed TYPE DATE;

#Task 8: Create the 'Primary Keys' in the dim_tables