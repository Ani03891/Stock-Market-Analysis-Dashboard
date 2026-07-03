 # 📈 Stock Market Analysis Dashboard

## 📌 Project Overview

This project is a Stock Market Analysis Dashboard built using Python, Pandas, MySQL, and Streamlit. It analyzes historical stock market data, performs feature engineering, stores processed data in MySQL, and presents insights through an interactive dashboard.

---

## 🚀 Features

- Market Summary Dashboard
- Top 10 Gainers
- Top 10 Losers
- Volatility Analysis
- Cumulative Return Analysis
- Sector-wise Performance
- Stock Correlation Heatmap
- Monthly Top Gainers & Losers
- Interactive Streamlit Dashboard

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- MySQL
- SQLAlchemy
- PyMySQL
- Streamlit
- PyYAML

---

## 📂 Project Structure

```
STOCK_ANALYSIS_PROJECT
│
├── Data/
├── output_csv/
├── scripts/
│   ├── yaml_to_csv.py
│   ├── combine_csv.py
│   ├── visualization.py
│   ├── load_to_mysql.py
│   ├── analysis.py
│   └── app.py
│
├── cleaned_stock_data.csv
├── master_stock_data.csv
├── Sector_data.csv
├── requirements.txt
└── README.md
```

---

## 📊 Dashboard Pages

- Dashboard
- Stock Analysis
- Volatility Analysis
- Sector Analysis
- Correlation Analysis
- Monthly Analysis

---

## ⚙️ How to Run

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Load Data into MySQL

```bash
python scripts/load_to_mysql.py
```

### Run the Streamlit Dashboard

```bash
streamlit run scripts/app.py
```

---

## 📈 Key Insights

- Identifies the top-performing and worst-performing stocks.
- Measures stock volatility using standard deviation.
- Compares average returns across sectors.
- Visualizes relationships between stock prices using a correlation heatmap.
- Tracks monthly gainers and losers.

---

## 👩‍💻 Author

**Anitha Preethi**