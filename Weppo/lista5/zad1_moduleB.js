const moduleA = require("./zad1_moduleA");

function functionB() {
  console.log("Function B");
  moduleA.functionA();
}

module.exports.functionB = functionB;
