import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

DB_PATH = "sales.db"

# Funkcje pomocnicze
def connect_db():
    return sqlite3.connect(DB_PATH)

def get_data():
    conn = connect_db()
    df = pd.read_sql_query("SELECT * FROM sales", conn)
    conn.close()
    return df

def insert_sale(product, quantity, price, date):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO sales (product, quantity, price, date) VALUES (?, ?, ?, ?)",
        (product, quantity, price, date)
    )
    conn.commit()
    conn.close()

# Interfejs
st.set_page_config(page_title="Sprzedaż - Dashboard", layout="wide")
st.title("📊 Aplikacja Sprzedażowa (sales.db)")

# Dodawanie nowej sprzedaży
st.header("➕ Dodaj nową sprzedaż")
with st.form("add_sale"):
    col1, col2, col3, col4 = st.columns(4)
    product = col1.text_input("Produkt")
    quantity = col2.number_input("Ilość", min_value=1, value=1)
    price = col3.number_input("Cena jednostkowa", min_value=0.0, format="%.2f")
    date = col4.date_input("Data")
    submitted = st.form_submit_button("Dodaj")
    if submitted:
        insert_sale(product, quantity, price, date.strftime("%Y-%m-%d"))
        st.success("✅ Sprzedaż została dodana!")
        st.balloons()

# Dane i filtrowanie
st.header("📋 Lista sprzedaży")
df = get_data()

products = df['product'].unique().tolist()
filter_product = st.selectbox("Filtruj po produkcie:", ["Wszystkie"] + products)

if filter_product != "Wszystkie":
    df = df[df['product'] == filter_product]

st.dataframe(df, use_container_width=True)

# Wartość sprzedaży dzienna
st.header("📈 Sprzedaż dzienna (ilość × cena)")
df['total'] = df['quantity'] * df['price']
daily_sales = df.groupby("date")["total"].sum().reset_index()

fig1, ax1 = plt.subplots()
ax1.plot(daily_sales["date"], daily_sales["total"], marker='o')
ax1.set_xlabel("Data")
ax1.set_ylabel("Wartość sprzedaży")
ax1.set_title("Sprzedaż dzienna")
plt.setp(ax1.get_xticklabels(), rotation=45, ha='right')
plt.tight_layout()
st.pyplot(fig1)

# Sprzedane sztuki wg produktu
st.header("📊 Sprzedaż wg typu produktu")
product_summary = df.groupby("product")["quantity"].sum().reset_index()

fig2, ax2 = plt.subplots()
ax2.bar(product_summary["product"], product_summary["quantity"], color='green')
ax2.set_xlabel("Produkt")
ax2.set_ylabel("Sprzedane sztuki")
ax2.set_title("Suma sprzedanych produktów wg typu")
st.pyplot(fig2)

