module toplevel(output [3:0] o, input [3:0] i, input l, input r);
  
  // sciezka krytyczna ma 3 bramki:
  // - glówny OR
  // - AND sprawdzajacy warunek
  // - dodatkowe NOTy
  function shift(input prev, curr, next);
    shift = (l && prev) || (r && next) || (!l && !r && curr);
  endfunction
  
  // operacje dla każdego bitu wykonują się równolegle
  // stąd ścieżka krytyczna całego ukladu nie przekracza 3 bramek
  assign o = {
    shift(i[2], i[3], 0   ),
    shift(i[1], i[2], i[3]),
    shift(i[0], i[1], i[2]),
    shift(0,    i[0], i[1])
  };
endmodule
