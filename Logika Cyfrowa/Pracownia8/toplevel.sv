module pwm_generator (
	input logic clk,
  	input logic [15:0] d,
  	input logic [1:0] sel,
  	output logic [15:0] cnt, cmp, top,
  	output logic out
);

    always_ff @(posedge clk) begin
      	if (sel == 2'd1) cmp <= d; // Ładowanie rejestru porównania 
      	if (sel == 2'd2) top <= d; // Ładowanie rejestru wartości szczytowej  
      	if (sel == 2'd3) cnt <= d; // Ładowanie licznika lub normalna praca
      	else if (cnt >= top) cnt <= 16'd0; // Przekręcenie się licznika
        else cnt <= cnt + 16'd1; // Normalna iteracja
    end

  	assign out = (cnt < cmp) ? 1'b1 : 1'b0; // Ustalenie wyjścia na podstawie wartości licznika
endmodule
