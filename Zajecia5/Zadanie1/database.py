import sqlite3

# Połącz z bazą
conn = sqlite3.connect("sales.db")
cursor = conn.cursor()

def run_queries():
    # a) Sprzedaż tylko produktu „Laptop”
    print("a) Laptop sales:")
    cursor.execute("SELECT * FROM sales WHERE product = 'Laptop';")
    for row in cursor.fetchall():
        print(row)

    # b) Dane z dni 2025-05-07 i 2025-05-08
    print("\nb) Sales from 2025-05-07 and 2025-05-08:")
    cursor.execute("SELECT * FROM sales WHERE date IN ('2025-05-07', '2025-05-08');")
    for row in cursor.fetchall():
        print(row)

    # c) Transakcje z ceną jednostkową powyżej 200 zł
    print("\nc) Price > 200:")
    cursor.execute("SELECT * FROM sales WHERE price > 200;")
    for row in cursor.fetchall():
        print(row)

    # d) Łączna wartość sprzedaży dla każdego produktu
    print("\nd) Total sales per product:")
    cursor.execute("""
        SELECT product, SUM(quantity * price) AS total_sales
        FROM sales
        GROUP BY product;
    """)
    for row in cursor.fetchall():
        print(row)

    # e) Dzień z największą liczbą sprzedanych sztuk
    print("\ne) Day with highest total quantity:")
    cursor.execute("""
        SELECT date, SUM(quantity) AS total_quantity
        FROM sales
        GROUP BY date
        ORDER BY total_quantity DESC
        LIMIT 1;
    """)
    print(cursor.fetchone())

    conn.close()