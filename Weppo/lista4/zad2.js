function isOwnProperty(obj, property) {
  return obj.hasOwnProperty(property);
}

function enumerateAllFields(obj) {
  var i = 1;
  for (var field in obj) {
    console.log(i++, field);
  }
}

function enumerateOwnFields(obj) {
  var i = 1;
  for (var field in obj) {
    if (isOwnProperty(obj, field)) console.log(i++, field);
  }
}

var p = {
  name: "jan",
};

var q = {
  surname: "kowalski",
};

Object.setPrototypeOf(p, q);

console.log(isOwnProperty(p, "name"));
console.log(isOwnProperty(p, "surname"));

console.log("\nAll fields:");
enumerateAllFields(p);
console.log("\nOwn fields:");
enumerateOwnFields(p);
