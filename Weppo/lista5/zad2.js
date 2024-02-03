const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.question("Podaj swoje imie: ", (name) => {
  console.log(`Witaj ${name}!`);
  rl.close();
});
