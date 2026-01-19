Algorytm zastępuje rywalizację o jeden licznik współpracą w strukturze drzewa binarnego, redukując zatory przy dużym obciążeniu.
​
Działanie opiera się na trzech głównych krokach:

1. **Precombining/Combining**: Wątki wspinają się od liści do korzenia. Jeśli dwa wątki spotkają się w węźle, łączą swoje siły: jeden (pasywny) przekazuje swoją wartość i czeka, a drugi (aktywny) zabiera ich wspólną sumę i idzie wyżej.
​
2. **Operation**: Do korzenia dociera tylko jeden wątek z "dużą" sumą zebraną od innych. Aktualizuje on główny licznik tylko raz.
​
3. **Dystrybucja wyników**: Wątek aktywny wraca w dół drzewa, "budzi" czekających partnerów i rozdaje im odpowiednie wyniki
