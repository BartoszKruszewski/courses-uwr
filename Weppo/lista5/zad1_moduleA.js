const moduleB = require("./zad1_moduleB");

function functionA() {
  console.log("Function A");
  moduleB.functionB();
}

module.exports.functionA = functionA;
