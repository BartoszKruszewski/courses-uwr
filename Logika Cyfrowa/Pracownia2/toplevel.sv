module circuit (input [3:0] i, output o);
    logic a = i[3];
    logic b = i[2];
    logic c = i[1];
    logic d = i[0];

    // wynik z mapy Karnaugha (razem z mostami)
    assign o = (~a &  c &  d) |
               (~b &  c &  d) |
               (~a &  b &  d) |
               ( b & ~c &  d) |
               (~a &  b &  c) |
               ( b &  c & ~d) |
               ( a & ~b &  d) |
               ( a & ~c &  d) |
               ( a & ~b &  c) |
               ( a &  c & ~d) |
               ( a &  b & ~c) |
               ( a &  b & ~d);
endmodule
