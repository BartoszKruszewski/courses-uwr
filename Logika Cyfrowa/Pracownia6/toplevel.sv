module toplevel (
    output wire [7:0] q,
    input logic [7:0] d,
    input logic i, c, l, r
);

    // Sygnał pośredni - następny stan rejestru
    wire [7:0] next_q;
    wire [7:0] master_q;
    wire [7:0] slave_q;

    // Logika wyboru kolejnego stanu
    assign next_q = (l & r) ? d :
                    (l)     ? {i, q[7:1]} :
                    (r)     ? {q[6:0], i} :
                              q;

    // Master-slave DFF
    assign master_q = c ? master_q : next_q;
    assign slave_q  = c ? master_q : slave_q;
    assign q = slave_q;

endmodule
