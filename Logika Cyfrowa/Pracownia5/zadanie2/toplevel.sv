module gray_to_binary (input  logic [31:0] i, output logic [31:0] o);
    integer k;
    always_comb begin
      	o = '0;
        o[31] = i[31];
        for (k = 30; k >= 0; k--) begin
          o[k] = o[k+1] ^ i[k]; // wzór z wykładu z petlą zamiast rekurencji
        end
    end

endmodule
