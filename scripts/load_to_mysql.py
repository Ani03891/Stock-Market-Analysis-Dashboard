import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv("cleaned_stock_data.csv")

engine = create_engine(
    "mysql+pymysql://root:12345678@localhost/stock_analysis"
)

print("Connected Successfully")

df.to_sql(
    "stocks",
    con=engine,
    if_exists="replace",
    index=False
)

print("Loaded Successfully")