// zamiana tablicy na set, has dziala w O(1), zamiast  includes w O(n)

const ids = new Set();

const generateId = () => {
    let id = 0;

    do {
        id++;
    } while (ids.has(id));

    ids.add(id);
    return id;
};

console.time("generateId");

for (let i = 0; i < 3000; i++) {
    generateId();
}

console.timeEnd("generateId");
