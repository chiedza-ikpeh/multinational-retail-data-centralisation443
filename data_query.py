# Milestone 4

# Task 1: How many stores does the busines shave and in which countries?

SELECT
    country,
    COUNT(*) AS total_no_stores
FROM
    stores
GROUP BY
    country
ORDER BY
    total_no_stores DESC;


# Task 2: Which locations currently have the most stores?

SELECT
    locality,
    COUNT(*) AS total_no_stores
FROM
    stores
GROUP BY
    locality
ORDER BY
    total_no_stores DESC
LIMIT 7;

# Task 3: Which months produced the largest amount of sales?

SELECT
    SUM(sales_amount) AS total_sales,
    EXTRACT(MONTH FROM sale_date) AS month
FROM
    sales
GROUP BY
    month
ORDER BY
    total_sales DESC;


# Task 4: How many sales are coming from online?

SELECT
    COUNT(*) AS numbers_of_sales,
    SUM(product_quantity) AS product_quantity_count,
    CASE
        WHEN location = 'Web' THEN 'Web'
        ELSE 'Offline'
    END AS location
FROM
    sales
GROUP BY
    location;


# Task 5: What percentage of sales come through each type of store?

SELECT
    store_type,
    SUM(sales_amount) AS total_sales,
    (SUM(sales_amount) / (SELECT SUM(sales_amount) FROM sales)) * 100 AS percentage_total
FROM
    sales
GROUP BY
    store_type
ORDER BY
    total_sales DESC;

# Task 6: Which month in each yuear produced the highest cost of sales?

SELECT
    SUM(sales_amount) AS total_sales,
    EXTRACT(YEAR FROM sale_date) AS year,
    EXTRACT(MONTH FROM sale_date) AS month
FROM
    sales
GROUP BY
    year,
    month
ORDER BY
    total_sales DESC
LIMIT 10;

# Task 7: What is our staff headcount?

SELECT
    SUM(staff_count) AS total_staff_numbers,
    country_code
FROM
    locations
GROUP BY
    country_code
ORDER BY
    total_staff_numbers DESC;

# Task 8: Which German store type is selling the most?

SELECT
    SUM(sales_amount) AS total_sales,
    store_type,
    country_code
FROM
    sales
WHERE
    country_code = 'DE'
GROUP BY
    store_type, country_code
ORDER BY
    total_sales DESC;


# Task 9: How quickly is the company making sales?

SELECT
    EXTRACT(YEAR FROM sale_time) AS year,
    AVG(
        EXTRACT(EPOCH FROM LEAD(sale_time) OVER (PARTITION BY EXTRACT(YEAR FROM sale_time) ORDER BY sale_time) - sale_time) * INTERVAL '1 second'
    ) AS actual_time_taken
FROM
    sales
GROUP BY
    year
ORDER BY
    year DESC;

#Task 10: Update the latest code changes to GitHub
