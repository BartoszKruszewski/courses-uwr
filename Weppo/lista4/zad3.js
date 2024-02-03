function Person(name) {
  this.name = name;
}

function Worker(name, job) {
  Person;
  this.job = job;
}

Worker.prototype = Person.prototype;
const worker1 = new Worker("a", "Developer");

console.log(Object.getPrototypeOf(worker1));

Worker.prototype = new Person();
const worker2 = new Worker("b", "Developer");

console.log(Object.getPrototypeOf(worker2));

Worker.prototype = Object.create(Person.prototype);
const worker3 = new Worker("c", "Developer");

console.log(Object.getPrototypeOf(worker3));
