var n = 1;
console.log(typeof Object.getPrototypeOf(n)); // object, poniewaz wszystko w js ma przypisany pusty prototyp
n.foo = "foo";
console.log(n.foo); //undefined, poniewaz przypisanie pola do liczby jest niedozwolone
