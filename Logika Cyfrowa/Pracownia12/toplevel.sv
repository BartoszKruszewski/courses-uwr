// Moduł pamięci synchronicznej
module dp_ram (
    input  logic       clk, we,
    input  logic [2:0] raddr, waddr,
    input  logic [7:0] wdata,
    output logic [7:0] rdata
);
    logic [7:0] mem [0:7];

    always_ff @(posedge clk) begin
        if (we) begin
            mem[waddr] <= wdata;
        end
        rdata <= mem[raddr];
    end
endmodule

// Ścieżka sterowania (Control Path)
module sort_control (
    input  logic clk, nrst, start,
    input  logic cmp_i_7, cmp_j_7, cmp_c_m, cmp_i_jm,
    output logic i_ld, i_sel, j_ld, j_sel, jm_ld, jm_sel, m_ld,
    output logic [1:0] raddr_sel,
    output logic waddr_sel, wdata_sel, logic_we, ready
);
    enum logic [2:0] {
        READY_ST,
        OUTER_ST,
        INNER_ST,
        END_ST,
        SWAP_ST
        } state, next_state;

    // Rejestr stanu (odświeżany co cykl zegara)
    always_ff @(posedge clk or negedge nrst) begin
        if (!nrst) begin
            state <= READY_ST;
        end else begin
            state <= next_state;
        end
    end

    // Logika kombinacyjna automatu
    always_comb begin
        // Wartości domyślne sygnałów sterujących
        next_state = state;
        {ready, i_ld, i_sel, j_ld, j_sel, jm_ld, jm_sel, m_ld, waddr_sel, wdata_sel, logic_we} = '0;
        raddr_sel = 2'b00;

        case (state)
            READY_ST: begin
                ready = 1'b1;
                // Inicjalizacja sortowania
                if (start) begin 
                    i_ld = 1'b1; 
                    raddr_sel = 2'b00; // Przygotowanie komórki mem[0]
                    next_state = OUTER_ST; 
                end
            end
            
            OUTER_ST: begin
                // Jeśli i = 7, koniec sortowania
                if (cmp_i_7) begin
                    next_state = READY_ST;
                end else begin 
                    // Przygotowanie do algorytmu szukania minimum
                    j_ld = 1'b1; 
                    jm_ld = 1'b1; 
                    m_ld = 1'b1; 
                    raddr_sel = 2'b01; 
                    next_state = INNER_ST; 
                end
            end
            
            INNER_ST: begin
                // Zapisz nowe minimum, jeśli znaleziono mniejszy element (c < m)
                if (cmp_c_m) begin 
                    m_ld = 1'b1; 
                    jm_ld = 1'b1; 
                    jm_sel = 1'b1; 
                end
                
                // Zakończ pętlę wewnętrzną gdy doszliśmy do końca tablicy (j=7)
                if (cmp_j_7) begin 
                    raddr_sel = 2'b11; // Odczytaj i-ty element w przygotowaniu na ew. zamianę
                    next_state = END_ST; 
                end else begin 
                    j_ld = 1'b1; 
                    j_sel = 1'b1; 
                    raddr_sel = 2'b10; 
                    next_state = INNER_ST; 
                end
            end
            
            END_ST: begin
                // Jeśli obecny element jest poprawny, nie zamieniaj go
                if (cmp_i_jm) begin 
                    i_ld = 1'b1; 
                    i_sel = 1'b1; 
                    raddr_sel = 2'b01; 
                    next_state = OUTER_ST; 
                end else begin 
                    logic_we = 1'b1; // Włącz zapis i przygotuj stan Swap
                    next_state = SWAP_ST; 
                end
            end
            
            SWAP_ST: begin
                // Zamiana w pamięci najmniejszej odnalezionej wartości
                logic_we = 1'b1; 
                waddr_sel = 1'b1; 
                wdata_sel = 1'b1; 
                i_ld = 1'b1; 
                i_sel = 1'b1; 
                raddr_sel = 2'b01; 
                next_state = OUTER_ST;
            end
            
            default: begin
                next_state = READY_ST;
            end
        endcase
    end
endmodule

// Ścieżka danych (Data Path)
module sort_datapath (
    input  logic clk, nrst,
    input  logic i_ld, i_sel, j_ld, j_sel, jm_ld, jm_sel, m_ld,
    input  logic [1:0] raddr_sel,
    input  logic waddr_sel, wdata_sel,
    output logic cmp_i_7, cmp_j_7, cmp_c_m, cmp_i_jm,
    output logic [2:0] logic_raddr, logic_waddr,
    output logic [7:0] logic_wdata,
    input  logic [7:0] mem_rdata
);
    logic [2:0] i, j, jm;
    logic [7:0] m, c;

    assign c = mem_rdata;

    // Przerzutniki indeksów i wartości pamięci
    always_ff @(posedge clk or negedge nrst) begin
        if (!nrst) begin
            {i, j, jm, m} <= '0;
        end else begin
            if (i_ld)  i  <= i_sel  ? (i + 3'd1) : 3'd0;
            if (j_ld)  j  <= j_sel  ? (j + 3'd1) : (i + 3'd1);
            if (jm_ld) jm <= jm_sel ? j : i;
            if (m_ld)  m  <= c;
        end
    end

    // Komparatory wspierające układ sterowania
    assign cmp_i_7  = (i == 3'd7);
    assign cmp_j_7  = (j == 3'd7);
    assign cmp_c_m  = (c < m);
    assign cmp_i_jm = (i == jm);

    // Koder adresu odczytu z pamięci algorytmu
    always_comb begin
        case (raddr_sel)
            2'b00: logic_raddr = 3'd0;
            2'b01: logic_raddr = i + 3'd1;
            2'b10: logic_raddr = j + 3'd1;
            2'b11: logic_raddr = i;
            default: logic_raddr = 3'd0;
        endcase
    end

    // Multipleksery przygotowujące do zapisu/podmiany w pamięci
    assign logic_waddr = waddr_sel ? i : jm;
    assign logic_wdata = wdata_sel ? m : c;
endmodule

// Moduł nadrzędny łączący (Top-Level)
module selection_sort (
    input  logic       clk, nrst, start, wr,
    input  logic [2:0] addr,
    input  logic [7:0] datain,
    output logic [7:0] dataout,
    output logic       ready
);
    logic cmp_i_7, cmp_j_7, cmp_c_m, cmp_i_jm;
    logic i_ld, i_sel, j_ld, j_sel, jm_ld, jm_sel, m_ld;
    logic [1:0] raddr_sel;
    logic waddr_sel, wdata_sel, logic_we, ext_control;
    logic [2:0] logic_raddr, logic_waddr, mem_raddr, mem_waddr;
    logic [7:0] logic_wdata, mem_rdata, mem_wdata;
    logic mem_we;

    sort_control  ctrl (.*);
    sort_datapath dp   (.*);

    // Decyzja komu przypisać kontrolę nad pamięcią na podstawie flagi ready
    assign ext_control = ready && !start;
    assign mem_raddr   = ext_control ? addr   : logic_raddr;
    assign mem_waddr   = ext_control ? addr   : logic_waddr;
    assign mem_wdata   = ext_control ? datain : logic_wdata;
    assign mem_we      = ext_control ? wr     : logic_we;
    assign dataout     = mem_rdata;

    // Instrukcja implementacji pamięci synchronicznej RAM
    dp_ram ram (
        .clk(clk), 
        .raddr(mem_raddr), 
        .waddr(mem_waddr),
        .we(mem_we), 
        .wdata(mem_wdata), 
        .rdata(mem_rdata)
    );
endmodule
