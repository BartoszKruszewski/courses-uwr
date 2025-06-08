<script lang="ts">
  type Todo = { id: number; name: string; completed: boolean };

  let text = "";
  let todos: Todo[] = [];

  function add() {
    if (!text.trim()) return;
    todos = [...todos, { id: Date.now(), name: text.trim(), completed: false }];
    text = "";
  }

  function remove(id: number) {
    todos = todos.filter((t) => t.id !== id);
  }

  function toggle(id: number) {
    todos = todos.map((t) =>
      t.id === id ? { ...t, completed: !t.completed } : t,
    );
  }

  function moveUp(idx: number) {
    if (idx === 0) return;
    const copy = [...todos];
    [copy[idx - 1], copy[idx]] = [copy[idx], copy[idx - 1]];
    todos = copy;
  }

  function moveDown(idx: number) {
    if (idx === todos.length - 1) return;
    const copy = [...todos];
    [copy[idx], copy[idx + 1]] = [copy[idx + 1], copy[idx]];
    todos = copy;
  }

  function clearAll() {
    todos = [];
  }
</script>

<div class="body__wrapper">
  <header class="header__wrapper">
    <h1>Hello!</h1>
  </header>

  <main class="main">
    <section>
      <form class="add-item__container" on:submit|preventDefault={add}>
        <input
          class="add-item__element add-item__input"
          placeholder="What's on your mind?"
          bind:value={text}
          required
        />
        <button class="add-item__element add-item__submit">Add</button>
      </form>
    </section>

    <section class="todos__container">
      <header class="todos-header__container">
        <h2>
          Todo List ({todos.filter((t) => !t.completed).length} remaining)
          <button id="todos-clear" class="todos-clear" on:click={clearAll}>
            Clear all
          </button>
        </h2>
      </header>

      <ul id="todo-list" class="todos__list">
        {#each todos as todo, i (todo.id)}
          <li
            class="todo__container {todo.completed
              ? 'todo__container--completed'
              : ''}"
          >
            <div class="todo-element todo-name">{todo.name}</div>

            <button
              class="todo-element todo-button move-up"
              on:click={() => moveUp(i)}>↑</button
            >
            <button
              class="todo-element todo-button move-down"
              on:click={() => moveDown(i)}>↓</button
            >

            {#if !todo.completed}
              <button
                class="todo-element todo-button"
                on:click={() => toggle(todo.id)}
              >
                Done
              </button>
            {:else}
              <button
                class="todo-element todo-button"
                on:click={() => toggle(todo.id)}
              >
                Revert
              </button>
            {/if}

            <button
              class="todo-element todo-button"
              on:click={() => remove(todo.id)}
            >
              Remove
            </button>
          </li>
        {/each}
      </ul>
    </section>
  </main>
</div>
