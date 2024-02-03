function sum() {
  let suma = 0;
  for (let i = 0; i < arguments.length; i++) {
    suma += arguments[i];
  }
  return suma;
}

console.log(sum(1, 2, 3));

console.log(sum(1, 2, 3, 4, 5));
