module toplevel (
    input  logic clk, nrst,
    input  logic door, start, finish,
    output logic heat, light, bell
);

    // definicja stanów
    typedef enum logic [2:0] {
        CLOSED = 3'd0,
        OPEN   = 3'd1,
        COOK   = 3'd2,
        PAUSE  = 3'd3,
        BELL   = 3'd4
    } state_type;

    state_type state, next_state;

    // rejestr stanu
    always_ff @(posedge clk or negedge nrst) begin
        if (!nrst) state <= CLOSED;
        else state <= next_state;
    end

    // logika przejść
    always_comb begin
        next_state = state; // pętla domyślna
        case (state)
            CLOSED: begin
                if (door) next_state = OPEN;
                else if (start && !door) next_state = COOK;
            end
            OPEN: if (!door) next_state = CLOSED;
            COOK: begin
                if (door) next_state = PAUSE;
                else if (finish && !door) next_state = BELL;
            end
            PAUSE: if (!door) next_state = COOK;
            BELL: if (door) next_state = OPEN;
            default: next_state = CLOSED;
        endcase
    end

    // Funkcja wyjściowa
    always_comb begin
        unique case (state)
          	CLOSED:  {heat, light, bell} = 3'b000;
            OPEN:    {heat, light, bell} = 3'b010;
            COOK:    {heat, light, bell} = 3'b110;
            PAUSE:   {heat, light, bell} = 3'b010;
            BELL:    {heat, light, bell} = 3'b001;
            default: {heat, light, bell} = 3'b000;
        endcase
    end
endmodule
