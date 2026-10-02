-- Vehicle Sales Business Analytics
-- SQL Analysis

-- 1. Total vehicles
SELECT COUNT(*) AS total_vehicles
FROM Cleaned_CarPrices;


-- 2. Total revenue
SELECT SUM(sellingprice) AS total_revenue
FROM Cleaned_CarPrices;


-- 3. Average selling price
SELECT AVG(sellingprice) AS average_selling_price
FROM Cleaned_CarPrices;


-- 4. Sales by vehicle brand
SELECT
    make,
    COUNT(*) AS vehicles_sold,
    AVG(sellingprice) AS average_selling_price
FROM Cleaned_CarPrices
GROUP BY make
ORDER BY vehicles_sold DESC;


-- 5. Top 10 vehicle models
SELECT TOP 10
    make,
    model,
    COUNT(*) AS vehicles_sold,
    AVG(sellingprice) AS average_selling_price
FROM Cleaned_CarPrices
GROUP BY make, model
ORDER BY vehicles_sold DESC;


-- 6. Sales by state
SELECT
    state,
    COUNT(*) AS vehicles_sold,
    AVG(sellingprice) AS average_selling_price
FROM Cleaned_CarPrices
GROUP BY state
ORDER BY vehicles_sold DESC;


-- 7. Mileage analysis
SELECT
    CASE
        WHEN odometer < 30000 THEN 'Low Mileage'
        WHEN odometer < 70000 THEN 'Medium Mileage'
        WHEN odometer < 100000 THEN 'High Mileage'
        ELSE 'Very High Mileage'
    END AS mileage_category,
    COUNT(*) AS vehicles_sold,
    AVG(sellingprice) AS average_selling_price
FROM Cleaned_CarPrices
GROUP BY
    CASE
        WHEN odometer < 30000 THEN 'Low Mileage'
        WHEN odometer < 70000 THEN 'Medium Mileage'
        WHEN odometer < 100000 THEN 'High Mileage'
        ELSE 'Very High Mileage'
    END
ORDER BY average_selling_price DESC;


-- 8. Price difference from market value
SELECT
    make,
    COUNT(*) AS vehicles_sold,
    AVG(sellingprice - mmr) AS average_price_difference
FROM Cleaned_CarPrices
GROUP BY make
ORDER BY average_price_difference DESC;


-- 9. Transmission analysis
SELECT
    transmission,
    COUNT(*) AS vehicles_sold,
    AVG(sellingprice) AS average_selling_price
FROM Cleaned_CarPrices
GROUP BY transmission
ORDER BY vehicles_sold DESC;


-- 10. Condition analysis
SELECT
    condition,
    COUNT(*) AS vehicles_sold,
    AVG(sellingprice) AS average_selling_price
FROM Cleaned_CarPrices
GROUP BY condition
ORDER BY average_selling_price DESC;
