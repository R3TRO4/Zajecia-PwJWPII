from flask import Flask, render_template

"""
Podejście 2: Logika po stronie JavaScript (frontend)
• Lista zadań przechowywana w localStorage lub w zmiennej JS
• Wszystko dzieje się w przeglądarce (dodawanie, usuwanie, oznaczanie)
• Flask tylko dostarcza statyczne pliki i szablon HTML
• Stylizacja i interakcje w pełni w CSS + JS
Użyjesz: addEventListener, createElement, localStorage, fetch (opcjonalnie)
"""

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
