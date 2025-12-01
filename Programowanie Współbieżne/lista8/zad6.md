#### Intuicja

Własność **nieczekania** jest wykorzystywana w tym dowodzie głównie w celu zagwarantowania osiągalności stanu krytycznego. Ten sam efekt możemy jednak uzyskać, opierając się na słabszej własności **niewstrzymywania**.

#### Dowód

Załóżmy, że system nie osiąga stanu krytycznego.

Oznaczałoby to trwale zablokowanie się w jednej z wcześniejszych konfiguracji.

Jednak definicja **niewstrzymywania** gwarantuje, że jeśli system przebywa w danym stanie wystarczająco długo, przynajmniej jeden z wątków zdoła ukończyć swoją operację (poczynić postęp).

Zatem system musiałby w końcu przejść do stanu krytycznego.

Reszta dowodu pozostaje niezmienna.
