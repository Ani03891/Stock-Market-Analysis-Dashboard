import streamlit as st
import pandas as pd
import pymysql
import matplotlib.pyplot as plt

# -----------------------------
# Title
# -----------------------------
st.title("📈 Stock Market Analysis Dashboard")

# -----------------------------
# MySQL Connection
# -----------------------------
conn = pymysql.connect(
    host="localhost",
    user="root",
    password="12345678",
    database="stock_analysis"
)

st.success("✅ MySQL Connected Successfully")

# -----------------------------
# Sidebar
# -----------------------------
page = st.sidebar.selectbox(
    "Select Page",
    [
        "Dashboard",
        "Stock Analysis",
        "Volatility Analysis",
        "Sector Analysis",
        "Correlation",
        "Monthly Analysis"
    ]
)

# -----------------------------
# Dashboard Page
# -----------------------------
if page == "Dashboard":

    st.header("Dashboard")

    # Total Records
    total_records = pd.read_sql(
        """
        SELECT COUNT(*) AS total_records
        FROM stocks
        """,
        conn
    ).iloc[0]["total_records"]

    # Total Stocks
    total_stocks = pd.read_sql(
        """
        SELECT COUNT(DISTINCT Ticker) AS total_stocks
        FROM stocks
        """,
        conn
    ).iloc[0]["total_stocks"]

    # Average Close Price
    avg_close = pd.read_sql(
        """
        SELECT ROUND(AVG(close), 2) AS avg_close
        FROM stocks
        """,
        conn
    ).iloc[0]["avg_close"]

    # Average Volume
    avg_volume = pd.read_sql(
        """
        SELECT ROUND(AVG(volume), 2) AS avg_volume
        FROM stocks
        """,
        conn
    ).iloc[0]["avg_volume"]

    # -----------------------------
    # KPI Columns
    # -----------------------------
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            label="Total Records",
            value=total_records
        )

    with col2:
        st.metric(
            label="Total Stocks",
            value=total_stocks
        )

    with col3:
        st.metric(
            label="Average Close Price",
            value=avg_close
        )

    with col4:
        st.metric(
            label="Average Volume",
            value=avg_volume
        )
if page == "Stock Analysis":
    st.header("Stock Analysis")
    col1, col2 = st.columns(2)

    with col1:

        st.subheader("📈 Top 10 Gainers")

        top_gainers = pd.read_sql(
            """
            SELECT Ticker, daily_return
            FROM stocks
            ORDER BY daily_return DESC
            LIMIT 10
            """,
            conn
        )

        st.dataframe(top_gainers)

        st.bar_chart(
            data=top_gainers,
            x="Ticker",
            y="daily_return"
        )
    with col2:

        st.subheader("📉 Top 10 Losers")

        top_losers = pd.read_sql(
            """
            SELECT Ticker, daily_return
            FROM stocks
            ORDER BY daily_return ASC
            LIMIT 10
            """,
            conn
        )

        st.dataframe(top_losers)

        st.bar_chart(
            data=top_losers,
            x="Ticker",
            y="daily_return"
        )
if page == "Volatility Analysis" :
    st.header("Volatility Analysis")
    volatility_analysis = pd.read_sql(
        """
        Select Ticker, Round(STD(Volatility_return),4) as Volatility from Stocks group by Ticker order by Volatility desc limit 10
        """,conn)
    st.subheader("📊 Top 10 Most Volatile Stocks")
    st.dataframe(volatility_analysis)
    st.bar_chart(data = volatility_analysis,x="Ticker",y="Volatility")
if page == "Sector Analysis":

    st.header("Sector Analysis")
    sector_analysis = pd.read_sql(
    """
    SELECT
        sector,
        ROUND(AVG(daily_return),4) AS avg_return
    FROM stocks
    GROUP BY sector
    ORDER BY avg_return DESC
    """,
    conn)
    st.subheader("Average Return by Sector")

    st.dataframe(sector_analysis)
    st.bar_chart(
        data=sector_analysis,
        x="sector",
        y="avg_return"
    )
if page == "Correlation":

    st.header("🔗 Stock Correlation")

    correlation_data = pd.read_sql(
        """
        SELECT date, Ticker, close
        FROM stocks
        """,
        conn
    )

    price_data = correlation_data.pivot(
        index="date",
        columns="Ticker",
        values="close"
    )

    correlation_matrix = price_data.corr()

    st.subheader("Correlation Matrix")

    st.dataframe(correlation_matrix)

    fig, ax = plt.subplots(figsize=(12,10))

    image = ax.imshow(
        correlation_matrix,
        cmap="coolwarm",
        aspect="auto"
    )

    plt.colorbar(image)

    ax.set_xticks(range(len(correlation_matrix.columns)))
    ax.set_xticklabels(
        correlation_matrix.columns,
        rotation=90
    )

    ax.set_yticks(range(len(correlation_matrix.columns)))
    ax.set_yticklabels(correlation_matrix.columns)

    st.pyplot(fig)
if page == "Monthly Analysis":

    st.header("📅 Monthly Analysis")

    monthly_data = pd.read_sql(
        """
        SELECT date, Ticker, close
        FROM stocks
        """,
        conn
    )

    monthly_data["date"] = pd.to_datetime(monthly_data["date"])

    monthly_data["Month"] = monthly_data["date"].dt.strftime("%b")

    monthly_return = (
        monthly_data
        .groupby(["Month","Ticker"])["close"]
        .agg(["first","last"])
        .reset_index()
    )

    monthly_return["monthly_return"] = (
        (monthly_return["last"] - monthly_return["first"])
        / monthly_return["first"]
    )

    selected_month = st.selectbox(
        "Select Month",
        sorted(monthly_return["Month"].unique())
    )

    month_data = monthly_return[
        monthly_return["Month"] == selected_month
    ]

    top5_gainers = (
        month_data
        .sort_values(
            "monthly_return",
            ascending=False
        )
        .head(5)
    )

    top5_losers = (
        month_data
        .sort_values(
            "monthly_return"
        )
        .head(5)
    )

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("📈 Top 5 Gainers")

        st.dataframe(top5_gainers)

        st.bar_chart(
            data=top5_gainers,
            x="Ticker",
            y="monthly_return"
        )

    with col2:

        st.subheader("📉 Top 5 Losers")

        st.dataframe(top5_losers)

        st.bar_chart(
            data=top5_losers,
            x="Ticker",
            y="monthly_return"
        )