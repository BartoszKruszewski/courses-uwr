function MyObject(name) {
  return { name };
}
const obj1 = new MyObject("a");
const obj2 = new MyObject("b");
const obj3 = new MyObject("c");

Object.setPrototypeOf(obj1, obj2);
Object.setPrototypeOf(obj2, obj3);

function getLastProto(o) {
  var p = o;
  do {
    o = p;
    p = Object.getPrototypeOf(o);
  } while (p);
  return o;
}

console.log("\nObjects:");
console.log(obj1);
console.log(obj2);
console.log(obj3);

console.log("\nPrototypes:");
console.log(Object.getPrototypeOf(obj1));
console.log(Object.getPrototypeOf(obj2));
console.log(Object.getPrototypeOf(obj3));

console.log("\nLast Prototypes:");
console.log(getLastProto(obj1));
console.log(getLastProto(obj2));
console.log(getLastProto(obj3));
