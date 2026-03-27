// wybiera 8 bitów z konkatenacji a i b licząc od pozycji n
module funnel_shifter (input [7:0] a, b, input [3:0] n, output [7:0] o);
    logic [15:0] concat;
    assign concat = {a, b};
  	assign o = 8'(concat >> n);
endmodule

// ogólny moduł przesuwający
// i - wejście
// n - wartość przesunięcia
// ar - rodzaj przesunięcia (arytmetyczne, logiczne)
// lr - kierunek (lewo, prawo)
// rot - czy rotacja (rotacja, przesunięcie)
module shift_rotate (input [7:0] i, input [3:0] n, input ar, lr, rot, output [7:0] o);
    logic [7:0] fs_a, fs_b;
    logic [3:0] fs_n;

    assign fs_a = lr  ? i :
                  rot ? i :
                  ar  ? {8{i[7]}} : 8'b0; // przesunięcie arytmetyczne dodaje bit znaku

    assign fs_b = lr  ? (rot ? i : 8'b0) : i;
  	assign fs_n = lr ? (4'd8 - n) : n; // "odwrócenie" n w zależności od kierunku

    funnel_shifter fs_inst (.a(fs_a), .b(fs_b), .n(fs_n), .o(o));
endmodule
