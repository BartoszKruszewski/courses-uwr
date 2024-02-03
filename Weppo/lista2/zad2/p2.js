const person = {
  1: "John",
  2: "Doe",
};

console.log(person[1]);
console.log(person["2"]);

// jeśli argumentem operatora [] jest liczba,
// JavaScript przekształci ją w string i użyje jako klucza

const key = {
  toString: function () {
    return "2";
  },
};

console.log(person[key]);

// jeśli argumentem operatora [] jest inny obiekt,
// JavaScript przekształci ją w string i użyje jako klucza

const myArray = [10, 20, 30];
console.log(myArray["1"]);

// jeśli argumentem operatora [] dostępu jest string,
// JavaScript przekształci go w liczbę (jeśli to możliwe) i użyje jako indeksu

const index = {
  valueOf: function () {
    return 1;
  },
};

console.log(myArray[index]); // 20

// analogicznie dla innych obiektów
