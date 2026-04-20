module toplevel (input  logic [15:0] i, output logic [15:0] o);
    logic [3:0] a0, a1, a2, a3;

    always_comb begin
        a0 = i[3:0];
        a1 = i[7:4];
        a2 = i[11:8];
        a3 = i[15:12];

        // Sieć sortująca dla 4 elementów
        // Każdy krok to komparator: jeśli lewa > prawa, zamień miejscami

        if (a0 > a1) {a0, a1} = {a1, a0};  // sortuj dolną parę
        if (a2 > a3) {a2, a3} = {a3, a2};  // sortuj górną parę
      	if (a0 > a2) {a0, a2} = {a2, a0}; // wyłania minimum globalne w a0
      	if (a1 > a3) {a1, a3} = {a3, a1}; // wyłania maksimum globalne w a3
      	if (a1 > a2) {a1, a2} = {a2, a1}; // porównaj środkowe elementy

        o = {a3, a2, a1, a0}
    end

endmodule
