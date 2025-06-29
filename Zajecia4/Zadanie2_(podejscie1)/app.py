from flask import Flask, render_template, request, redirect, url_for

"""
Zbuduj prostą aplikację To-Do, która pozwala użytkownikowi:
• Dodawać nowe zadania
• Oznaczać zadania jako wykonane
• Usuwać zadania z listy
Wymagane trasy:
1. / – strona główna z linkami do:
2. /tasks – strona z listą zadań
3. /about – strona „O aplikacji”
Dwa podejścia do realizacji:
Podejście 1: Logika po stronie Pythona (Flask)
• Lista zadań przechowywana w zmiennej w Pythonie
• Dodawanie przez formularz HTML (metoda POST)
• Usuwanie i oznaczanie jako wykonane przez przekierowania (/delete/<id>,
/done/<id>)
• Widoki renderowane przez Flask (render_template z Jinja2)
Użyjesz: request.form, redirect, url_for, @app.route
"""

app = Flask(__name__)

# Przechowywanie zadań w pamięci
tasks = []
task_id_counter = 1

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/tasks", methods=["GET", "POST"])
def task_list():
    global task_id_counter
    if request.method == "POST":
        content = request.form.get("task")
        if content:
            tasks.append({"id": task_id_counter, "task": content, "done": False})
            task_id_counter += 1
        return redirect(url_for("task_list"))
    return render_template("tasks.html", tasks=tasks)

@app.route("/done/<int:task_id>")
def mark_done(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            break
    return redirect(url_for("task_list"))

@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
    return redirect(url_for("task_list"))

if __name__ == "__main__":
    app.run(debug=True)
