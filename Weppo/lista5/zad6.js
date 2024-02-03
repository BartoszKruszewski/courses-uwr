const fs = require("fs");
const readline = require("readline");

const clientRequests = new Map();

const fileStream = fs.createReadStream("log.txt");
const rl = readline.createInterface({ input: fileStream });

rl.on("line", (line) => {
  const ipAddress = line.split(" ")[1];
  if (clientRequests.has(ipAddress)) {
    clientRequests.set(ipAddress, clientRequests.get(ipAddress) + 1);
  } else {
    clientRequests.set(ipAddress, 1);
  }
});

rl.on("close", () => {
  [...clientRequests]
    .sort((a, b) => b[1] - a[1])
    .slice(0, 3)
    .forEach(([ip, count]) => {
      console.log(`${ip} ${count}`);
    });
});
