import pandas as pd
df = pd.read_csv("master_stock_data.csv")
print(df.head())
print(df.shape)
print(df.columns)
print(df.info())
print(df.describe())
print(df.isnull().sum())
print(df['Ticker'].nunique())
print(df["Ticker"].unique())
print(df.groupby("Ticker")["close"].mean())
print(df.groupby("Ticker")["volume"].sum())
print(df.groupby("Ticker")["high"].max())
print(df.groupby("Ticker")["low"].min())
df["date"] = pd.to_datetime(df["date"])
print(df.info())
df["price_change"] = df["close"]-df["open"]
print(df.head())
df["daily_return"] = ((df["close"]-df["open"])/df["open"])*100
print(df.head())
print(df.duplicated().sum())
df.to_csv("cleaned_stock_data.csv",index=False)
print("cleaned file saved")






