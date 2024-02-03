function Foo() {
  function Qux() {
    console.log("To jest funkcja prywatna Qux");
  }

  this.Bar = function () {
    console.log("To jest metoda publiczna Bar");
    Qux();
  };
}

var myFoo = new Foo();
myFoo.Bar();
//myFoo.Qux(); // blad przy wywolaniu
