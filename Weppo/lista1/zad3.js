function isPrime(number) {
  if (number < 2) {
    return false;
  }

  divider = 2;
  while (divider * divider <= number) {
    if (number % divider == 0) {
      return false;
    }
    divider += 1;
  }

  return true;
}

for (i = 2; i <= 100000; i++) {
  if (isPrime(i)) {
    console.log(i);
  }
}
