const o = {
  field1: 42,
  "field 2": "hello",
};

console.log(o.field1);
console.log(o["field 2"]);

// uzywajac . nie mozemy odwolac sie do skladowych ze spacja w nazwie
// operator . jest używany, gdy klucz jest znanym identyfikatorem.
// operator [] pozwala na dostęp za pomocą zmiennych lub wyrażeń.
