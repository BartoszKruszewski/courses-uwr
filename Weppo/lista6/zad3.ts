function forEach<T>(a: T[], f: (t: T) => void): void {
  for (var i in a) {
    f(a[i]);
  }
}

function map<T, L>(a: T[], f: (t: T) => L): L[] {
  var new_a: L[] = [];
  for (var i in a) {
    new_a[i] = f(a[i]);
  }
  return new_a;
}

function filter<T>(a: T[], f: (t: T) => boolean): T[] {
  var new_a: T[] = [];
  for (var i in a) {
    if (f(a[i])) {
      new_a.push(a[i]);
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
