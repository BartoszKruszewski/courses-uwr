const x = 42;
console.log(typeof x);

const name = "John";
console.log(typeof name);

const person = { name: "Alice" };
console.log(typeof person);

function greet() {
  return "Hello!";
}
console.log(typeof greet);

console.log();

class Vehicle {
  drive() {
    console.log("Vehicle is moving.");
  }
}

class Car extends Vehicle {
  honk() {
    console.log("Car is honking.");
  }
}

const myCar = new Car();
console.log(myCar instanceof Car);
console.log(myCar instanceof Vehicle);

const myVehicle = new Vehicle();
console.log(myVehicle instanceof Car);
