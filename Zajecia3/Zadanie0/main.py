from flask import Flask

"""
Utwórz środowisko wirtualne Pythona, w którym znajdą się pakiety Flask (w wersji co
najmniej 3.0) oraz SQLAlchemy (dokładnie 2.0.40), instalując je z przygotowanego przez
Ciebie pliku requirements.txt.
"""
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Flask działa!'

if __name__ == '__main__':
    app.run(debug=True)
