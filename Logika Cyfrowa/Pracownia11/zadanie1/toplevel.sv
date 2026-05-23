module fast_exp (
    input  logic        clk,
    input  logic        nrst,
    input  logic        start,
    input  logic [15:0] inx,
    input  logic [7:0]  inn,
    output logic        ready,
    output logic [15:0] out
);

    localparam logic READY = 1'b0;
    localparam logic BUSY  = 1'b1;

    logic        state;
    logic [15:0] x, a;
    logic [7:0]  n;

    logic [15:0] mul_op1;
    logic [15:0] mul_out;

    assign ready = (state == READY);

    // Multiplekser sterujący jednym z wejść mnożarki.
    // Jeżeli n jest parzyste (n[0]==0), mnożymy x * x.
    // Jeżeli n jest nieparzyste (n[0]==1), mnożymy a * x.
    assign mul_op1 = (state == BUSY && n[0] == 1'b0) ? x : a;
    
    // Pojedyncza, jawnie zdefiniowana operacja mnożenia
    assign mul_out = mul_op1 * x;

    always_ff @(posedge clk or negedge nrst) begin
        if (!nrst) begin
            state <= READY;
            a     <= '0;
            x     <= '0;
            n     <= '0;
        end else case (state)
            READY: begin
                if (start) begin
                    a     <= 16'd1;
                    x     <= inx;
                    n     <= inn;
                    state <= BUSY;
                end
            end
            BUSY: begin
                if (n == 8'd0) begin
                    state <= READY;
                end else if (n[0] == 1'b0) begin
                    x <= mul_out;   // Wynik z pojedynczej mnożarki trafia do x
                    n <= n >> 1;
                end else begin
                    a <= mul_out;   // Wynik z pojedynczej mnożarki trafia do a
                    n <= n - 8'd1;
                end
            end
        endcase
    end

    assign out = a;

endmodule