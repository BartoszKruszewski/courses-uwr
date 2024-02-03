function iterativeFib(n) {
  if (n < 2) {
    return 1;
  }
  a = 1;
  b = 1;
  c = 1;
  for (i = 0; i < n; i++) {
    a = b;
    b = c;
    c = a + b;
  }
  return c;
}

function recursiveFib(n) {
  if (n < 2) {
    return 1;
  }
  return recursiveFib(n - 1) + recursiveFib(n - 2);
}

console.time("Iterative run time");
for (i = 2; i <= 40; i++) {
  iterativeFib(i);
}
console.timeEnd("Iterative run time");

console.time("Recursive run time");
for (i = 2; i <= 40; i++) {
  recursiveFib(i);
}
console.timeEnd("Recursive run time");
