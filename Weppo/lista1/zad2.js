function getDigits(number) {
  var digits = [];
  var digit;
  var number;
  while (number > 0) {
    digit = number % 10;
    digits.push(digit);
    number = (number - digit) / 10;
  }
  return digits;
}

function getSum(numbers) {
  var sum = 0;
  for (var number of numbers) {
    sum += number;
  }
  return sum;
}

function isDivisible(number1, number2) {
  return number1 % number2 == 0;
}

function isGood(number) {
  var digits = getDigits(number);
  for (var digit of digits) {
    if (!isDivisible(number, digit)) {
      return false;
    }
  }
  
  return isDivisible(number, getSum(digits));
}

for (var i = 0; i <= 100000; i++) {
  if (isGood(i)) {
    console.log(i);
  }
}
