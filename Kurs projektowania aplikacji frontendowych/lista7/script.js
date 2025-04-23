const form = document.getElementById("add-todo-form");
const input = form.querySelector("input[name='todo-name']");
const list = document.getElementById("todo-list");
const clearBtn = document.getElementById("todos-clear");
const countSpan = document.getElementById("count");

let todos = [
    { text: "Buy milk", completed: false },
    { text: "Go to the gym", completed: true },
    { text: "Read a book", completed: false },
    { text: "Write code", completed: true },
    { text: "Walk the dog", completed: false },
    {
        text:
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. " +
            "Mauris vel metus sed justo vehicula rutrum vel ut est. " +
            "Maecenas a dictum nunc. Proin congue libero risus, et lobortis purus venenatis eu. " +
            "Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. " +
            "Morbi pulvinar ullamcorper tortor, quis cursus quam.",
        completed: false,
    },
];

const render = () => {
    list.innerHTML = "";
    todos.forEach((t, i) => {
        const li = document.createElement("li");
        li.className = `todo__container${t.completed ? " todo__container--completed" : ""}`;
        li.innerHTML = `
      <div class="todo-element todo-name">${t.text}</div>
      <button class="todo-element todo-button move-up">↑</button>
      <button class="todo-element todo-button move-down">↓</button>
      <button class="todo-element todo-button">${t.completed ? "Revert" : "Done"}</button>
      <button class="todo-element todo-button">Remove</button>
    `;

        const [up, down, toggle, remove] = li.querySelectorAll("button");

        up.onclick = () => i > 0 && ([todos[i - 1], todos[i]] = [todos[i], todos[i - 1]], render());
        down.onclick = () => i < todos.length - 1 && ([todos[i], todos[i + 1]] = [todos[i + 1], todos[i]], render());
        toggle.onclick = () => (todos[i].completed = !todos[i].completed, render());
        remove.onclick = () => (todos.splice(i, 1), render());

        list.appendChild(li);
    });
    countSpan.textContent = todos.filter(t => !t.completed).length;
};

form.onsubmit = e => {
    e.preventDefault();
    const text = input.value.trim();
    if (text) todos.push({ text, completed: false });
    input.value = "";
    render();
};

clearBtn.onclick = () => (todos = [], render());

render();
