const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const randomNum = Math.floor(Math.random() * 101);

function main() {
  rl.question("Podaj liczbe od 0 do 100: ", (input) => {
    let answear = parseInt(input);

    if (answear < randomNum) console.log("Moja liczba jest większa.");
    else if (answear > randomNum) console.log("Moja liczba jest mniejsza.");
    else {
      console.log("Gratulacje, zgadles liczbe!");
      rl.close();
    }

    if (answear !== randomNum) {
      main();
    }
  });
}

main();
