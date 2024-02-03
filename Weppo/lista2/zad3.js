console.log("Wyrazenie: ");
console.log(
  (![] + [])[+[]] +
    (![] + [])[+!+[]] +
    ([![]] + [][[]])[+!+[] + [+[]]] +
    (![] + [])[!+[] + !+[]]
);

console.log("\nPierwsza Grupa: ");
console.log(typeof (![] + []), ![] + []);
console.log(typeof +[], +[]);
console.log(typeof (![] + [])[+[]], (![] + [])[+[]]);

console.log("\nDruga Grupa: ");
console.log(typeof (![] + [])[+!+[]], (![] + [])[+!+[]]);
console.log(typeof (![] + []), ![] + []);
console.log(typeof +!+[], +!+[]);

console.log("\nTrzecia Grupa: ");
console.log(
  typeof ([![]] + [][[]])[+!+[] + [+[]]],
  ([![]] + [][[]])[+!+[] + [+[]]]
);
console.log(typeof [![]], [![]]);
console.log(typeof [][[]], [][[]]);
console.log(typeof ([![]] + [][[]]), [![]] + [][[]]);
console.log(typeof +!+[], +!+[]);
console.log(typeof [+[]], [+[]]);
console.log(typeof [+!+[] + [+[]]], [+!+[] + [+[]]]);

console.log("\nCzwarta Grupa: ");
console.log(typeof (![] + [])[!+[] + !+[]], (![] + [])[!+[] + !+[]]);
console.log(typeof (![] + []), ![] + []);
console.log(typeof [!+[] + !+[]], [!+[] + !+[]]);
