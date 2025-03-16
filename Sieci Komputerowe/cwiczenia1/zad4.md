▶ 0.0.0.0/0 → do routera A
▶ 10.0.0.0/8 → do routera B
▶ 10.3.0.0/24 → do routera C
▶ 10.3.0.32/27 → do routera B
▶ 10.3.0.64/27 → do routera B
▶ 10.3.0.96/27 → do routera B

▶ 10.3.0.64/27 → do routera B
▶ 10.3.0.96/27 → do routera B
sklejamy w
▶ 10.3.0.64/26 → do routera B

▶ 10.3.0.32/27 → do routera B
▶ 10.3.0.64/26 → do routera B
zawieraja sie w 
▶ 10.0.0.0/8 → do routera B
ale rowniez w
▶ 10.3.0.0/24 → do routera C

mozemy wiec usunac je ale zmodyfikowac
▶ 10.3.0.0/24 → do routera C
na dwa wpisy
▶ 10.3.0.0/27 → do routera C
▶ 10.3.0.128/25 → do routera C
które pokryja "dziury" w routingu

ostatecznie tablica bedzie wygladac

▶ 0.0.0.0/0 → do routera A
▶ 10.0.0.0/8 → do routera B
▶ 10.3.0.0/27 → do routera C
▶ 10.3.0.128/25 → do routera C
