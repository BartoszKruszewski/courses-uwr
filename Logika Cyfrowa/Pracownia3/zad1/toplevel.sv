module full_adder (input a, b, cin, output logic sum, cout);
    assign sum  = a ^ b ^ cin;
    assign cout = (a & b) | (cin & (a ^ b));
endmodule

// Sumator szeregowy
module adder4 (input [3:0] a, b, input cin, output [3:0] sum, output cout);
    logic c1, c2, c3;

    full_adder fa0 (.a(a[0]), .b(b[0]), .cin(cin), .sum(sum[0]), .cout(c1));
    full_adder fa1 (.a(a[1]), .b(b[1]), .cin(c1),  .sum(sum[1]), .cout(c2));
    full_adder fa2 (.a(a[2]), .b(b[2]), .cin(c2),  .sum(sum[2]), .cout(c3));
    full_adder fa3 (.a(a[3]), .b(b[3]), .cin(c3),  .sum(sum[3]), .cout(cout));
endmodule

// Jednocyfrowy sumator BCD
module bcd_digit_adder (input [3:0] a, b, input cin, output [3:0] sum, output cout);
    logic [3:0] bin_sum;
    logic       bin_carry;
    logic       correct;
    logic [3:0] corr_val;
    logic       unused_carry;

    adder4 binary_add (.a(a), .b(b), .cin(cin), .sum(bin_sum), .cout(bin_carry));

    // Wykrycie czy wynik > 9
    assign correct = bin_carry | (bin_sum[3] & (bin_sum[2] | bin_sum[1]));

    // Korekcja — dodaj 6 jeśli correct=1, 0 jeśli correct=0
    assign corr_val = {1'b0, correct, correct, 1'b0};
    adder4 correct_add (.a(bin_sum), .b(corr_val), .cin(1'b0), .sum(sum), .cout(unused_carry));

    // Przeniesienie wyjściowe = flaga korekcji
    assign cout = correct;
endmodule

// Uzupełnienie do 9 cyfry BCD
module bcd9s_comp (input [3:0] d, output logic [3:0] r);
    assign r[3] = ~d[3] & ~d[2] & ~d[1];
    assign r[2] = ~d[3] & (d[1] ^ d[2]);
    assign r[1] = ~d[3] & d[1];
    assign r[0] = ~d[0];
endmodule

// Dwucyfrowy układ dodająco-odejmujący BCD, wynik mod 100
module bcd_add_sub (input [7:0] a, b, input sub, output [7:0] o);
    logic [7:0] b_comp;
    logic [7:0] b_eff;
    logic       carry_units;
    logic       carry_tens;  // odrzucane (realizacja mod 100)

    // Oblicz uzupełnienie do 9 dla jedności i dziesiątek b
    bcd9s_comp comp_units (.d(b[3:0]), .r(b_comp[3:0]));
    bcd9s_comp comp_tens  (.d(b[7:4]), .r(b_comp[7:4]));

    // Multiplekser bez instrukcji warunkowych
    // b_eff = sub ? b_comp : b
    assign b_eff = ({8{sub}} & b_comp) | ({8{~sub}} & b);

    // Dodaj jedności z cin=sub (=1 przy odejmowaniu — dopełnia uzupełn. do 10)
    bcd_digit_adder add_units (
        .a(a[3:0]), .b(b_eff[3:0]), .cin(sub), .sum(o[3:0]), .cout(carry_units)
    );

    // Dodaj dziesiątki z przeniesieniem z jedności
    bcd_digit_adder add_tens (
        .a(a[7:4]), .b(b_eff[7:4]), .cin(carry_units), .sum(o[7:4]), .cout(carry_tens)
    );

endmodule
