module d_latch (input logic en, nrst, d, output logic q);
    assign q = !nrst ? 1'b0 : (en ? d : q);
endmodule

module dff (input  wire clk, nrst, d,output wire q);
    wire qm;
  	d_latch master (~clk, nrst, d, qm);
  	d_latch slave (clk, nrst, qm, q);
endmodule

module counter4 (input wire clk, nrst, step, down, output wire [3:0] out);
  logic [3:0] d; // Wyjście multipleksera z wyliczonym następnym stanem
	
  	// Logika kombinacyjna wyliczania następnego stanu
    always_comb begin
        unique case ({down, step})
            2'b00: begin // +1
                d[0] = ~out[0];
                d[1] =  out[1] ^  out[0];
                d[2] =  out[2] ^ (out[1] & out[0]);
                d[3] =  out[3] ^ (out[2] & out[1] & out[0]);
            end

            2'b01: begin // +2
                d[0] =  out[0];
                d[1] = ~out[1];
                d[2] =  out[2] ^  out[1];
                d[3] =  out[3] ^ (out[2] & out[1]);
            end

            2'b10: begin // -1
                d[0] = ~out[0];
                d[1] =  out[1] ^ ~out[0];
                d[2] =  out[2] ^ (~out[1] & ~out[0]);
                d[3] =  out[3] ^ (~out[2] & ~out[1] & ~out[0]);
            end

            2'b11: begin // -2
                d[0] =  out[0];
                d[1] = ~out[1];
                d[2] =  out[2] ^ ~out[1];
                d[3] =  out[3] ^ (~out[2] & ~out[1]);
            end
        endcase
    end

    // Cztery przerzutniki przechowujące stan licznika
  	genvar i;
  	for (i = 0; i < 4; i = i+1)
  		dff ff (clk, nrst, d[i], out[i]);
endmodule
