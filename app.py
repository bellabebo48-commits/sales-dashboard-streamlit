# =========================================================
# STREAMLIT INTERACTIVE SALES DASHBOARD
# =========================================================
# FILE NAME:
#app.property
#
#REQUIRED LIBBRARIES INSTALL COMMAND:
#
# pip install streamlit pandas matplotlib openpyxl
#
# RUN COMMAND:
#
# streamlit run app.py
#
# IMPORTANT:
# Put Product_Sales_Dataset.xlsx
# in the SAME folder as app.py
# =========================================================

# -------------------------
# IMPORT LIBRARIES
# -------------------------
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------
# PAGE TITLE
# -------------------------
st.set_page_config(
    page_title="Interactive Sales Dashboard",
    layout="wide"
)

st.title("📊 Interactive Product Sales Dashboard")

# =========================================================
# LOAD EXCEL FILE 
# =========================================================
file_path = "Product_Sales_Dataset.xlsx"

#Read Excel File
df = pd.read_excel(
    file_path,
    sheet_name="Sales_Data"
)

# =========================================================
# SHOW DATASET
# ---------------------------
st.subheader(" Dataset Preview")

st.dataframe(df)

# =========================================================
#KPT SECTION
# =========================================================

#Calculate KPIs
total_sales = df["Sales_Amount"].sum()

total_profit = df["Profit"].sum()

total_orders = df["Order_ID"].count()

# Crete 3 colums
col1, col2, col3 = st.columns(3)

#Display KPIs
col1.metric("Total Sales", total_sales)

col2.metric("Total Profit", round(total_profit, 2))

col3.metric("Total Orders", total_orders)

# =========================================================
# SALES BY REGION
# =========================================================

st.subheader("Sales by Region")

# Group Data
sales_region = (
    df.groupby("Region")["Sales_Amount"]
    .sum()
)

# Crete Figure
fig1,ax1 = plt.subplots(figsize=(6,4))

# Plot Chart
sales_region.plot(
    kind="bar" ,
    ax=ax1
)

# Titles
ax1.set_title("Sales by Region")
ax1.set_xlabel("Region")
ax1.set_ylabel("Sales")

# Show in Streamlit
st.pyplot(fig1)

# =========================================================
# PROFIT BY REGION
# ==========================================================

st.subheader("Profit Distribution by Region")

# Group Data
profit_region = (
        df.groupby("Region")["Profit"]
        .sum()
    )

# Create Figure
fig2, ax2 = plt.subplots(figsize=(6,6))

# Pie Chart
profit_region.plot(
    kind="pie" ,
    autopct="%1.1f%%",
    ax=ax2
)

# Remove y label
ax2.set_ylabel("")

# Title
ax2.set_title("Profit by Region")

# Show Chart
st.pyplot(fig2)

# =========================================================
# ORDER BY REGION
# =========================================================

st.subheader("Order by Region")

# Group Data
orders_region = (
        df.groupby("Region")["Order_ID"]
        .count()
    )

# Create Figure
fig3, ax3 = plt.subplots(figsize=(6,4))

# Line Chart
orders_region.plot(
        kind="line",
        marker="o",
        ax=ax3
    )

# Titles
ax3.set_title("Orders by Region")
ax3.set_xlabel("Region")
ax3.set_ylabel("Orders")

# Grid
ax3.grid(True)

# Show Chart
st.pyplot(fig3)

# =========================================================
# TOP PRODUCTS
# =========================================================

st.subheader("top 5 Product by Sales")

# Top Products
top_products= (
    df.groupby("Product_Name")["Sales_Amount"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
    )

# Create Figure
fig4, ax4 = plt.subplots(figsize=(7,4))

# Horizontal Bar Chart
top_products.plot(
        kind="barh",
        ax=ax4
    )

# Titles
ax4.set_title("Top Products")
ax4.set_xlabel("Sales")
ax4.set_ylabel("Products")
    
# Show Chart
st.pyplot(fig4)

# =========================================================
# END MESSAGE
# =========================================================

st.success("Dashboard Successfully Created")