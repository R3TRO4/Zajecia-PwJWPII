from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Flask działa!'

if __name__ == '__main__':
    app.run(debug=True)
