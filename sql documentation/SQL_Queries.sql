-- Total Records
SELECT COUNT(*) AS total_records
FROM stocks;

-- Total Stocks
SELECT COUNT(DISTINCT Ticker) AS total_stocks
FROM stocks;

-- Average Close Price
SELECT ROUND(AVG(close),2)
FROM stocks;

-- Average Volume
SELECT ROUND(AVG(volume),2)
FROM stocks;

-- Top 10 Gainers
SELECT Ticker,
ROUND(AVG(daily_return),4) AS Avg_Return
FROM stocks
GROUP BY Ticker
ORDER BY Avg_Return DESC
LIMIT 10;

-- Top 10 Losers
SELECT Ticker,
ROUND(AVG(daily_return),4) AS Avg_Return
FROM stocks
GROUP BY Ticker
ORDER BY Avg_Return
LIMIT 10;

-- Volatility
SELECT Ticker,
ROUND(STD(Volatility_return),4) AS Volatility
FROM stocks
GROUP BY Ticker
ORDER BY Volatility DESC
LIMIT 10;

-- Sector Performance
SELECT sector,
ROUND(AVG(daily_return),4) AS Avg_Return
FROM stocks
GROUP BY sector
ORDER BY Avg_Return DESC;