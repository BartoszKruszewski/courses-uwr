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

function* take(it, top) {
  var n = 0;
  for (var _result; (_result = it.next()); !_result.done) {
    if (n++ > top) {
      break;
    }
    yield _result.value;
  }
}

for (let num of take(fib(), 10)) {
  console.log(num);
}
