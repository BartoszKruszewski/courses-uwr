module nwd_controller (
    input  logic clk, nrst, start, eq, lt,
    output logic ready, load, swap, sub, done
);
    logic state; // 0: READY, 1: BUSY

    always_ff @(posedge clk or negedge nrst) begin
        if (!nrst) state <= 1'b0;
        else       state <= (state == 1'b0) ? start : !eq;
    end

    assign ready = (state == 1'b0) && !start;
    assign load  = (state == 1'b0) && start;
    assign done  = (state == 1'b1) && eq;
    assign swap  = (state == 1'b1) && !eq && lt;
    assign sub   = (state == 1'b1) && !eq && !lt;
    
endmodule

module nwd_datapath (
    input  logic       clk, nrst, load, swap, sub, done,
    input  logic [7:0] ina, inb,
    output logic [7:0] out,
    output logic       eq, lt
);
    logic [7:0] a, b;

    assign eq = (a == b);
    assign lt = (a < b);

    always_ff @(posedge clk or negedge nrst) begin
        if (!nrst) begin
            a <= 8'd0; b <= 8'd0; out <= 8'd0;
        end else begin
            if (load) begin a <= ina; b <= inb; end
            if (swap) begin a <= b;   b <= a;   end
            if (sub)  begin a <= a - b;         end
            if (done) begin out <= a;           end
        end
    end
    
endmodule

module nwd (
    input  logic       clk, nrst, start,
    input  logic [7:0] ina, inb,
    output logic       ready,
    output logic [7:0] out
);
    logic eq, lt, load, swap, sub, done;

    nwd_controller u_ctrl (.*);
    nwd_datapath   u_data (.*);

endmodule
