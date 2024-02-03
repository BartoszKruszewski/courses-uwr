function foo(n: number): number {
  return n + 1;
}

function bar(n: number): number {
  return n - 1;
}

export { foo, bar }; // dowolna ilosc obiektow
export default foo; // jeden obiekt na plik
