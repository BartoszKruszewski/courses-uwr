module ram1k16 (
    input  logic        clk,
    input  logic        we,
    input  logic [9:0]  waddr,
    input  logic [15:0] wdata,
    input  logic [9:0]  raddr,
    output logic [15:0] rdata
);
    logic [15:0] mem [0:1023];

    always_ff @(posedge clk) begin
        if (we)
            mem[waddr] <= wdata;
    end

    assign rdata = mem[raddr];
endmodule

module toplevel (
    input  logic        nrst,
    input  logic        step,
    input  logic [15:0] d,
    input  logic        push,
    input  logic [1:0]  op,
    output logic [15:0] out,
    output logic [9:0]  cnt
);
    logic [15:0] top; // rejestr szczytu stosu

    // Porty RAM
    logic        ram_we;
    logic [9:0]  ram_waddr;
    logic [15:0] ram_wdata;
    logic [9:0]  ram_raddr;
    logic [15:0] ram_rdata;

    ram1k16 ram (
        .clk  (step),
        .we   (ram_we),
        .waddr(ram_waddr),
        .wdata(ram_wdata),
        .raddr(ram_raddr),
        .rdata(ram_rdata)
    );

    // ram_we=1 tylko przy push gdy stos nie jest pełny i jest co zapisać (cnt>=1)
    assign ram_we    = push && (cnt >= 10'd1) && (cnt < 10'd1023);
    // Adres zapisu: bieżący szczyt trafia na pozycję cnt-1
    assign ram_waddr = cnt - 10'd1;
    // Dane do zapisu: aktualny szczyt (przed jego nadpisaniem przez d)
    assign ram_wdata = top;
    // Adres odczytu: drugi element od góry (potrzebny przy ADD i MUL)
    assign ram_raddr = (cnt >= 10'd2) ? cnt - 10'd2 : 10'd0;

    always_ff @(posedge step or negedge nrst) begin
        if (!nrst) begin
            // Reset asynchroniczny: zeruj szczyt i licznik
            // (pamięć RAM nie jest czyszczona)
            top <= 16'd0;
            cnt <= 10'd0;
        end else begin
            if (push) begin
                // Odłożenie d na stos (ignoruj gdy stos pełny: cnt=1023)
                if (cnt < 10'd1023) begin
                    top <= d;
                    cnt <= cnt + 10'd1;
                end
            end else begin
                case (op)
                    2'd0: ; // NOP - brak operacji

                    2'd1: begin
                        // Minus unarny: negacja szczytu stosu
                        if (cnt >= 10'd1)
                            top <= -top;
                    end

                    2'd2: begin
                        // Dodawanie: top = top + element_pod_szczytem, cnt--
                        if (cnt >= 10'd2) begin
                            top <= top + ram_rdata;
                            cnt <= cnt - 10'd1;
                        end
                    end

                    2'd3: begin
                        // Mnożenie: top = top * element_pod_szczytem, cnt--
                        if (cnt >= 10'd2) begin
                            top <= top * ram_rdata;
                            cnt <= cnt - 10'd1;
                        end
                    end
                endcase
            end
        end
    end
  
    // Wyjście to zawsze aktualny szczyt stosu
    assign out = top;

endmodule
