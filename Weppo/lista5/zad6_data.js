const fs = require("fs");

const ipAddresses = [
  "12.34.56.78",
  "23.45.67.89",
  "123.245.167.289",
  "45.67.89.12",
  "67.89.12.34",
];

const httpMethods = ["GET", "POST", "PUT", "DELETE", "PATCH"];

const resources = [
  "/page1",
  "/page2",
  "/image.jpg",
  "/style.css",
  "/script.js",
];

const statusCodes = [200, 301, 404, 500];

function randomChoice(values) {
  return values[Math.floor(Math.random() * values.length)];
}

function generateRandomDate() {
  const startDate = new Date(2000, 0, 1);
  const endDate = new Date();

  const randomTime =
    startDate.getTime() +
    Math.random() * (endDate.getTime() - startDate.getTime());

  return new Date(randomTime);
}

const generateRandomLog = () => {
  const date = generateRandomDate();
  const hours = date.getHours().toString().padStart(2, "0");
  const minutes = date.getMinutes().toString().padStart(2, "0");
  const seconds = date.getSeconds().toString().padStart(2, "0");

  const ipAddress = randomChoice(ipAddresses);
  const httpMethod = randomChoice(httpMethods);
  const resource = randomChoice(resources);
  const statusCode = randomChoice(statusCodes);

  return `${hours}:${minutes}:${seconds} ${ipAddress} ${httpMethod} ${resource} ${statusCode}`;
};

const logFilePath = "log.txt";
const numberOfLogs = 1000;

const logData = [];
for (let _ = 0; _ < numberOfLogs; _++) {
  logData.push(generateRandomLog());
}

fs.writeFileSync(logFilePath, logData.join("\n"));
