function fib() {
  let a = 0;
  let b = 1;

  return {
    next: function () {
      const value = a;
      [a, b] = [b, a + b];
      return { value, done: false };
    },
  };
}

function* fib_gen() {
  let a = 0;
  let b = 1;
  while (true) {
    const v = a;
    [a, b] = [b, a + b];
    yield v;
  }
}

var n = 0;
/*
var _it = fib();
for (var _result; (_result = _it.next()); !_result.done) {
  console.log(_result.value);
  if (n++ > 100) {
    break;
  }
}
*/

for (var i of fib_gen()) {
  console.log(i);
  if (n++ > 100) {
    break;
  }
}
