# Najważniejsze punkty z .lst

[SEKCJE I ROZMIARY]
- Sekcje: .text ≈ 0x2238, .data ≈ 0x00CC, .bss ≈ 0x14 — rozmiar .text wyraźnie rośnie po włączeniu %f w printf/scanf
- Wniosek: obsługa float I/O wciąga duże fragmenty vfprintf/vfscanf/konwersji, istotnie „puchnąc” kod.

# Operacje

## INT8_T
- Dodawanie: pojedyncze add (ADD = 1 cykl) — najkrótsze i najszybsze.
- Mnożenie: mul (8×8, wynik w r1:r0) — sprzętowo 2 cykle.
- Dzielenie: __divmodhi4 — brak instrukcji dzielenia, realizacja programowa.

## INT16_T
- Dodawanie: add/adc na młodszym i starszym bajcie — krótka sekwencja.
- Mnożenie: kilka MUL + sumy/ADC (składanie 16×16→32).
- Dzielenie: __divmodhi4 — wolniejsze wywołanie biblioteczne. 

## INT32_T
- Dodawanie: cztery add/adc po bajtach (32-bit) — nadal kompaktowo. 
- Mnożenie: mulsi3 — sekwencja 8×8 MUL + dodania z przeniesieniem. 
- Dzielenie: __divmodsi4 — kosztowna rutyna, brak sprzętowego dzielenia. 

## INT64_T
- Dodawanie: adddi3 — pomocnicza rutyna dla 64-bit. 
- Mnożenie: mulsidi3 — składanie 64-bit z 32×32, później przesunięcia dla formatowania. 
- Dzielenie: divdi3 — najcięższa rutyna integer, czasowo i rozmiarowo. 
- Wydruk hi:lo: lshrdi3 (przesunięcia), a następnie printf dwóch 32-bitowych połówek. 

## FLOAT
- Arytmetyka: cmpsf2/addsf3/mulsf3/divsf3 — wszystko soft-float (brak FPU w AVR). 
- I/O: duże bloki vfprintf/vfscanf/ftoaengine + tablice potęg 10 (.Lpowr10/.Lbase10) po włączeniu %f. 

# WYDAJNOŚĆ
- Dodawanie: najszybsze (ADD/ADC = 1 cykl), minimalny kod, skaluje się liniowo z szerokością.
- Mnożenie: 8×8 MUL = 2 cykle; dla 16/32 bitów kilka MUL + ADD/ADC — średni koszt. 
- Dzielenie: tylko programowe (__divmod*/*di3), długie i wolne ścieżki. 
- Float: soft-float + formatowanie %f → najwolniejsze, najbardziej zwiększa rozmiar .text.
