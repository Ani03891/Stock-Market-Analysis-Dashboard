import pandas as pd
df = pd.read_csv("cleaned_stock_data.csv")
df['date'] = pd.to_datetime(df['date'])
print(df.info())
#Top 10 Green Stocks output
green = df.groupby("Ticker")["daily_return"].mean().sort_values(ascending=False).head(10)
print(green)
#Top 10 Loss Stocks.
loss = df.groupby("Ticker")["daily_return"].mean().sort_values(ascending=True).head(10)
print(loss)
#Market Summary
stock_return = df.groupby("Ticker")["daily_return"].mean()
green_count = (stock_return >0).sum()
red_count= (stock_return <0).sum()
avg_price = df["close"].mean()
avg_volume = df["volume"].mean()
print("Green Stocks:",green_count)
print("Red Stocks:",red_count)
print("Average Price:", avg_price)
print("Average Volume:", avg_volume)
# Volatility Analysis
df = df.sort_values(["Ticker","date"])
df["Prev_close"]=df.groupby("Ticker")["close"].shift(1)
df["Volatility_return"]=(df["close"]-df["Prev_close"])/df["Prev_close"]
Volatility =( df.groupby("Ticker")["Volatility_return"].std().sort_values(ascending=False).head(10))
print(Volatility)
import matplotlib.pyplot as plt
plt.title("Volatility")
plt.xlabel("Ticker")
plt.ylabel("Volatility")
Volatility.plot(kind="bar", figsize =(10,5))
plt.show()
# cumulative return 
df["cumulative_ret"] = (1+df["Volatility_return"]).groupby(df["Ticker"]).cumprod()-1
#Top 5 high cum return 
top5 = df.groupby("Ticker")["cumulative_ret"].last().sort_values(ascending=False).head(5)
top5_stocks = top5.index
top5_data= df[df["Ticker"].isin(top5_stocks)]
plt.figure(figsize=(12,6))
for stock in top5_stocks:
    stock_data = top5_data[top5_data["Ticker"]==stock]
    plt.plot(
        stock_data["date"],
        stock_data["cumulative_ret"],
        label=stock

    )
plt.xlabel("Date")
plt.ylabel("cumulative_ret")
plt.title("Top 5 Performing stock")
plt.legend()
plt.show()
# ---------------------------------------
# Sector wise performance
# ---------------------------------------

print(df["Ticker"].unique()[:10])

# Read sector file
sector = pd.read_csv("Sector_data.csv")

# Create Ticker column
sector["Ticker"] = sector["Symbol"].str.split(": ").str[1]

# Fix ticker names
sector["Ticker"] = sector["Ticker"].replace({
    "ADANIGREEN": "ADANIENT",
    "AIRTEL": "BHARTIARTL",
    "BRITANNIAIND": "BRITANNIA",
    "TATACONSUMER": "TATACONSUM"
})

# Add missing Britannia row
new_row = {
    "COMPANY": "BRITANNIA INDUSTRIES",
    "sector": "FMCG",
    "Symbol": "BRITANNIA INDUSTRIES: BRITANNIA",
    "Ticker": "BRITANNIA"
}

sector.loc[len(sector)] = new_row

# Remove old sector columns if they already exist
df = df.drop(
    columns=["COMPANY", "sector", "Symbol"],
    errors="ignore"
)

# Merge only once
merged_df = pd.merge(
    df,
    sector,
    on="Ticker",
    how="left"
)

print(merged_df[["Ticker", "sector"]].head())
print(merged_df["sector"].isna().sum())

# Save updated dataframe
merged_df.to_csv(
    "cleaned_stock_data.csv",
    index=False
)

print("Updated CSV with sector saved successfully!")

# Use merged dataframe from here onwards
df = merged_df

# Average return by sector
stock_return = (
    df.groupby(["Ticker", "sector"])["daily_return"]
      .mean()
      .reset_index()
)

sector_performance = (
    stock_return.groupby("sector")["daily_return"]
                .mean()
                .sort_values(ascending=False)
)

print(sector_performance)

sector_performance.plot(
    kind="bar",
    figsize=(10,5)
)

plt.title("Average Yearly Return by Sector")
plt.xlabel("Sector")
plt.ylabel("Average Yearly Return")
plt.xticks(rotation=45)
plt.show()
# Stock Price Correlation
price_data = df.pivot(
    index="date",
    columns="Ticker",
    values="close"
)
print(price_data.head())
correlation = price_data.corr()
print(correlation)
# Stock Price Correlation
# Create pivot table
price_data = df.pivot(
    index="date",
    columns="Ticker",
    values="close")
print(price_data.head())
# Correlation Matrix
correlation = price_data.corr()
print(correlation)
# Heatmap
plt.figure(figsize=(14,14))
plt.imshow(
    correlation,
    cmap="coolwarm",
    aspect="auto")
plt.colorbar()
plt.xticks(range(len(correlation.columns)),correlation.columns,
    rotation=90)
plt.yticks(range(len(correlation.columns)), correlation.columns)
plt.title("Stock Price Correlation Heatmap")
plt.show()
# ----------------------------------------------------
# Top 5 Gainers & Losers (Month-wise)
# ----------------------------------------------------

# Create Month column
df["Month"] = df["date"].dt.strftime("%b")
# Get first and last closing price
monthly_return = (
    df.groupby(["Month", "Ticker"])["close"]
    .agg(["first", "last"])
    .reset_index())
# Calculate monthly return
monthly_return["monthly_return"] = (
    (monthly_return["last"] - monthly_return["first"])
    / monthly_return["first"])
# Get all months
months = monthly_return["Month"].unique()
# Loop through every month
for month in months:

    print("\n", month)

    # Filter one month
    month_data = monthly_return[
        monthly_return["Month"] == month
    ]

    # Top 5 Gainers
    top5_gainers = (
        month_data
        .sort_values("monthly_return", ascending=False)
        .head(5)
    )

    print("\nTop 5 Gainers")
    print(top5_gainers[["Ticker", "monthly_return"]])

    # Top 5 Losers
    top5_losers = (
        month_data
        .sort_values("monthly_return")
        .head(5)
    )
    print("\nTop 5 Losers")
    print(top5_losers[["Ticker", "monthly_return"]])
    plt.figure(figsize=(8,4))
    plt.bar(
        top5_gainers["Ticker"],
        top5_gainers["monthly_return"])
    plt.title(f"Top 5 Gainers - {month}")
    plt.xlabel("Ticker")
    plt.ylabel("Monthly Return")
    plt.xticks(rotation=45)
    plt.show()
    plt.figure(figsize=(8,4))
    plt.bar(
        top5_losers["Ticker"],
        top5_losers["monthly_return"])
    plt.title(f"Top 5 Losers - {month}")
    plt.xlabel("Ticker")
    plt.ylabel("Monthly Return")
    plt.xticks(rotation=45)
    plt.show()








                      





