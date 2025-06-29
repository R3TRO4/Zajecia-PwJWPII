from flask import Flask, render_template_string, abort

app = Flask(__name__)

# Przykładowi użytkownicy
users = {
    1: {"name": "Ala", "age": 22},
    2: {"name": "Bartek", "age": 25},
    3: {"name": "Celina", "age": 30}
}

@app.route("/")
def home():
    return render_template_string("""
        <h1>Witamy w naszej aplikacji!</h1>
        <ul>
            <li><a href="/about">O nas</a></li>
            <li><a href="/users">Lista użytkowników</a></li>
        </ul>
    """)

@app.route("/about")
def about():
    return "<h2>O nas</h2><p>To prosta aplikacja demonstracyjna we Flasku.</p>"

@app.route("/users")
def list_users():
    links = "".join(
        f'<li><a href="/user/{uid}">{info["name"]}</a></li>'
        for uid, info in users.items()
    )
    return f"<h2>Użytkownicy</h2><ul>{links}</ul>"

@app.route("/user/<int:user_id>")
def user_profile(user_id):
    user = users.get(user_id)
    if user:
        return f"<h2>Profil</h2><p>{user['name']}, {user['age']} lat</p>"
    return "<h2>Błąd</h2><p>Użytkownik nie istnieje</p>", 404

if __name__ == "__main__":
    app.run(debug=True)
