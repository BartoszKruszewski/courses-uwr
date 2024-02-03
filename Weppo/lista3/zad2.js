function forEach(a, f) {
  for (i in a) {
    f(a[i]);
  }
}

function map(a, f) {
  var new_a = [];
  for (i in a) {
    new_a[i] = f(a[i]);
  }
  return new_a;
}

function filter(a, f) {
  var new_a = [];
  for (i in a) {
    if (f(a[i])) {
      new_a.push(i);
    }
  }
  return new_a;
}

var a = [1, 2, 3, 4];

forEach(a, (_) => {
  console.log(_);
});

console.log(filter(a, (_) => _ < 3));

console.log(map(a, (_) => _ * 2));
