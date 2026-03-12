// 4-bitowy blok sumatora z przewidywaniem przeniesienia (CLA)
module cla_4bit(input [3:0] a, b, input cin, output [3:0] s, output G, output P);
    logic [3:0] p, g;
    logic [3:1] c;

    // Propagacja i generowanie na poziomie bitow
    assign p = a ^ b;
    assign g = a & b;

    // Grupowa propagacja i generowanie
    assign P = p[3] & p[2] & p[1] & p[0];
    assign G = g[3] | (p[3] & g[2]) | (p[3] & p[2] & g[1]) | (p[3] & p[2] & p[1] & g[0]);

    // Wewnetrzne przeniesienia CLA
    assign c[1] = g[0] | (p[0] & cin);
    assign c[2] = g[1] | (p[1] & g[0]) | (p[1] & p[0] & cin);
    assign c[3] = g[2] | (p[2] & g[1]) | (p[2] & p[1] & g[0]) | (p[2] & p[1] & p[0] & cin);

    // Suma bitowa
    assign s[0] = p[0] ^ cin;
    assign s[1] = p[1] ^ c[1];
    assign s[2] = p[2] ^ c[2];
    assign s[3] = p[3] ^ c[3];
endmodule

// CLA drugiego poziomu: oblicza wejscia przeniesienia dla kazdej grupy 4-bitowej
module cla_group(input [3:0] Gi, Pi, input cin, output [3:1] c);
    assign c[1] = Gi[0] | (Pi[0] & cin);
    assign c[2] = Gi[1] | (Pi[1] & Gi[0]) | (Pi[1] & Pi[0] & cin);
    assign c[3] = Gi[2] | (Pi[2] & Gi[1]) | (Pi[2] & Pi[1] & Gi[0]) | (Pi[2] & Pi[1] & Pi[0] & cin);
endmodule

// 16-bitowy hierarchiczny sumator z przewidywaniem przeniesienia
module toplevel(input [15:0] a, b, output [15:0] o);
    logic [3:0] group_G, group_P;
    logic [3:1] group_c;
    logic [3:0] group_cin;

    assign group_cin = {group_c, 1'b0};

    cla_4bit cla0(.a(a[3:0]),   .b(b[3:0]),   .cin(group_cin[0]), .s(o[3:0]),   .G(group_G[0]), .P(group_P[0]));
    cla_4bit cla1(.a(a[7:4]),   .b(b[7:4]),   .cin(group_cin[1]), .s(o[7:4]),   .G(group_G[1]), .P(group_P[1]));
    cla_4bit cla2(.a(a[11:8]),  .b(b[11:8]),  .cin(group_cin[2]), .s(o[11:8]),  .G(group_G[2]), .P(group_P[2]));
    cla_4bit cla3(.a(a[15:12]), .b(b[15:12]), .cin(group_cin[3]), .s(o[15:12]), .G(group_G[3]), .P(group_P[3]));

    cla_group grp_cla(.Gi(group_G), .Pi(group_P), .cin(1'b0), .c(group_c));
endmodule
