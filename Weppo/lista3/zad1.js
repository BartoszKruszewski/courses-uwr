function fib(n) {
  if (n <= 2) {
    return 1;
  }
  return fib(n - 1) + fib(n - 2);
}

function memoize(fn) {
  var cache = {};
  return function (n) {
    if (n in cache) {
      console.log(`n: ${n}`);
      return cache[n];
    } else {
      var result = fn(n);
      cache[n] = result;
      return result;
    }
  };
}

// fib = memoize(fib);
console.time("mem_fib");
console.log(memoize(fib)(40));
console.log(memoize(fib)(40));
console.timeEnd("mem_fib");

// console.time("fib");
// console.log(fib(40));
// console.log(fib(40));
// console.log(fib(40));
// console.timeEnd("fib");
