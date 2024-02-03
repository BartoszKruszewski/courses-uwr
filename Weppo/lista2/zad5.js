const myObject = {
  myField: 42,
  myMethod: function () {
    return "Hello, World!";
  },
  //get myProperty() {
  //return this.myField;
  //},
  //set myProperty(value) {
  //this.myField = value;
  //},
};

console.log(myObject.myField); // 42
console.log(myObject.myMethod()); // "Hello, World!"
myObject.myProperty = 100; // Ustawienie wartości poprzez akcesor "set"
console.log(myObject.myProperty); // 100

// Dodawanie pola
Object.defineProperty(myObject, "newField", {
  value: "This is a new field",
  writable: true, // Możliwość zapisu (domyślnie false)
  enumerable: true, // Własność będzie wyświetlana w pętlach (domyślnie false)
  configurable: true, // Możliwość ponownej konfiguracji (domyślnie false)
});

// Dodawanie metody
myObject.newMethod = function () {
  return "This is a new method";
};

// Dodawanie właściwości z akcesorami get i set
Object.defineProperty(myObject, "newProperty", {
  get: function () {
    return this.newField;
  },
  set: function (value) {
    this.newField = value;
  },
});

console.log(myObject.newField);
console.log(myObject.newMethod());
myObject.newProperty = "New Value";
console.log(myObject.newProperty);
