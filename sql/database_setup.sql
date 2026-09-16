-- ==========================================
-- SALES ANALYTICS DATABASE SETUP
-- ==========================================

-- Create the sales table

CREATE TABLE sales_data (
    Order_ID INTEGER,
    Date DATE,
    Product VARCHAR(100),
    Category VARCHAR(100),
    Quantity INTEGER,
    Unit_Price DECIMAL(10,2),
    Sales DECIMAL(12,2),
    Profit DECIMAL(12,2),
    Region VARCHAR(50)
);


-- ==========================================
-- CHECK TABLE
-- ==========================================

SELECT *
FROM sales_data;


-- ==========================================
-- CHECK NUMBER OF RECORDS
-- ==========================================

SELECT COUNT(*) AS Total_Records
FROM sales_data;


-- ==========================================
-- CHECK FOR NULL VALUES
-- ==========================================

SELECT
    COUNT(*) AS Total_Records,
    COUNT(Order_ID) AS Orders,
    COUNT(Product) AS Products,
    COUNT(Sales) AS Sales_Records,
    COUNT(Profit) AS Profit_Records
FROM sales_data;
