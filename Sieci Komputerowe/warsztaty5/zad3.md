1. Co się wydarzyło po zmianie IP na Virbian2?
Virbian1 nadal wysyłał pakiety ICMP do starego adresu 192.168.0.2, używając znanego wcześniej adresu MAC. Virbian2 odbierała ramkę (bo MAC się zgadzał), ale odrzucała pakiet na poziomie IP, ponieważ nie był już do niej skierowany.

2. Dlaczego Virbian2 wysłała zapytanie ARP?
Chciała przekazać pakiet dalej do IP 192.168.0.2, ale nie znała jego nowego adresu MAC (tablica ARP została wyczyszczona po zmianie IP), więc musiała go ponownie ustalić.

3. Dlaczego nikt nie odpowiedział na zapytanie ARP?
Bo adres 192.168.0.2 nie był już przypisany do żadnej maszyny w sieci.

4. Dlaczego Virbian2 wysłała komunikat ICMP Redirect?
Bo uznała, że Virbian1 ma błędną trasę do 192.168.0.2 i poinformowała ją, że pakiety powinny iść inną drogą – mimo że fizycznie były już w tej samej sieci.