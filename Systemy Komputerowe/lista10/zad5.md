#### Write-back z write allocate

**Write-back** to polityka zapisu danych **przy trafieniu** do pamięci polegająca na odraczaniu zapisania wartości do pamięci, zanim linia nie zostanie zastąpiona. Posiada bit **dirty bit** sygnalizujący czy wartość została poddana zapisowi. Jeżeli bit jest zapalony to podczas zastępowania linii, należy zaktualizować wartość w pamięci głównej.
**Write-allocate** to polityka zapisu danych **przy chybieniu**, zakładająca wczytanie najpierw wartości do cache'u i dopiero wtedy poddanie jej modyfikacji. Pozwala to na zaoszczędzenie czasu przy wielokrotnej modyfikacji.

Obie te polityki najczęściej występują razem.

#### Diagram
