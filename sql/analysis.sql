-- ==========================================
-- SALES ANALYTICS SQL PROJECT
-- ==========================================


-- 1. VIEW ALL DATA
-- ==========================================

SELECT *
FROM sales_data;


-- 2. TOTAL SALES
-- ==========================================

SELECT
    SUM(Sales) AS Total_Sales
FROM sales_data;


-- 3. TOTAL PROFIT
-- ==========================================

SELECT
    SUM(Profit) AS Total_Profit
FROM sales_data;


-- 4. TOTAL QUANTITY SOLD
-- ==========================================

SELECT
    SUM(Quantity) AS Total_Quantity
FROM sales_data;


-- 5. PROFIT MARGIN
-- ==========================================

SELECT
    (SUM(Profit) / SUM(Sales)) * 100 AS Profit_Margin
FROM sales_data;


-- 6. SALES BY PRODUCT
-- ==========================================

SELECT
    Product,
    SUM(Sales) AS Total_Sales
FROM sales_data
GROUP BY Product
ORDER BY Total_Sales DESC;


-- 7. PROFIT BY PRODUCT
-- ==========================================

SELECT
    Product,
    SUM(Profit) AS Total_Profit
FROM sales_data
GROUP BY Product
ORDER BY Total_Profit DESC;


-- 8. SALES BY REGION
-- ==========================================

SELECT
    Region,
    SUM(Sales) AS Total_Sales
FROM sales_data
GROUP BY Region
ORDER BY Total_Sales DESC;


-- 9. PROFIT BY REGION
-- ==========================================

SELECT
    Region,
    SUM(Profit) AS Total_Profit
FROM sales_data
GROUP BY Region
ORDER BY Total_Profit DESC;


-- 10. MONTHLY SALES
-- ==========================================

SELECT
    EXTRACT(MONTH FROM Date) AS Month,
    SUM(Sales) AS Total_Sales
FROM sales_data
GROUP BY EXTRACT(MONTH FROM Date)
ORDER BY Month;


-- 11. MONTHLY PROFIT
-- ==========================================

SELECT
    EXTRACT(MONTH FROM Date) AS Month,
    SUM(Profit) AS Total_Profit
FROM sales_data
GROUP BY EXTRACT(MONTH FROM Date)
ORDER BY Month;


-- 12. TOP 5 ORDERS BY SALES
-- ==========================================

SELECT
    Order_ID,
    Product,
    Sales,
    Profit,
    Region
FROM sales_data
ORDER BY Sales DESC
LIMIT 5;


-- 13. AVERAGE ORDER VALUE
-- ==========================================

SELECT
    AVG(Sales) AS Average_Order_Value
FROM sales_data;


-- 14. PRODUCT QUANTITY
-- ==========================================

SELECT
    Product,
    SUM(Quantity) AS Total_Quantity
FROM sales_data
GROUP BY Product
ORDER BY Total_Quantity DESC;


-- 15. BEST-SELLING PRODUCT
-- ==========================================

SELECT
    Product,
    SUM(Sales) AS Total_Sales
FROM sales_data
GROUP BY Product
ORDER BY Total_Sales DESC
LIMIT 1;


-- 16. MOST PROFITABLE PRODUCT
-- ==========================================

SELECT
    Product,
    SUM(Profit) AS Total_Profit
FROM sales_data
GROUP BY Product
ORDER BY Total_Profit DESC
LIMIT 1;


-- 17. BEST-PERFORMING REGION
-- ==========================================

SELECT
    Region,
    SUM(Sales) AS Total_Sales
FROM sales_data
GROUP BY Region
ORDER BY Total_Sales DESC
LIMIT 1;
