function createFs(n) {
  var fs = [];
  for (var i = 0; i < n; i++) {
    fs[i] = (function (i) {
      return function () {
        // dodatkowe zagniezdzenie funkcji
        return i;
      };
    })(i);
  }
  return fs;
}

var myfs = createFs(10);
console.log(myfs[0]());
console.log(myfs[2]());
console.log(myfs[7]());
