function fib(n: number): number {
  if (n <= 2) {
    return 1;
  }
  return fib(n - 1) + fib(n - 2);
}

function memoize(fn: (n: number) => number): (n: number) => number {
  const cache: Record<number, number> = {};
  return (n: number) => {
    if (n in cache) {
      return cache[n];
    } else {
      const result = fn(n);
      cache[n] = result;
      return result;
    }
  };
}

const mem_fib: (n: number) => number = memoize(fib);
console.log(mem_fib(40));
