let tasks = JSON.parse(localStorage.getItem("tasks")) || [];

function saveTasks() {
    localStorage.setItem("tasks", JSON.stringify(tasks));
    renderTasks();
}

function addTask() {
    const input = document.getElementById("new-task");
    const text = input.value.trim();
    if (text) {
        tasks.push({ text, done: false });
        input.value = "";
        saveTasks();
    }
}

function toggleDone(index) {
    tasks[index].done = !tasks[index].done;
    saveTasks();
}

function deleteTask(index) {
    tasks.splice(index, 1);
    saveTasks();
}

function renderTasks() {
    const list = document.getElementById("task-list");
    list.innerHTML = "";
    tasks.forEach((task, index) => {
        const li = document.createElement("li");
        li.innerHTML = `
            ${task.done ? "<s>" + task.text + "</s>" : task.text}
            <button onclick="toggleDone(${index})">${task.done ? "Cofnij" : "Zrobione"}</button>
            <button onclick="deleteTask(${index})">Usuń</button>
        `;
        list.appendChild(li);
    });
}

renderTasks();
