**SRP (Single Responsibility Principle)**  
Zasada ta mówi, że każda klasa (lub moduł) powinna mieć wyłącznie jedną odpowiedzialność, a wszelkie funkcje czy zadania wykraczające poza tę odpowiedzialność należy wydzielić do osobnych klas lub modułów.

**ISP (Interface Segregation Principle)**  
Zasada ta nakazuje tworzenie małych, wyspecjalizowanych interfejsów zamiast jednego dużego. Klasy implementujące interfejsy nie powinny być zmuszane do definiowania metod, których nie potrzebują. Dzięki temu unika się zbędnych zależności i zbyt rozbudowanych interfejsów.

**Różnica**  
- SRP dotyczy przede wszystkim **poziomu klasy i jej obowiązków**, minimalizując liczbę powodów do zmiany.
- ISP dotyczy **projektowania interfejsów** tak, aby implementacje były możliwie najbardziej precyzyjne i nie obciążały klas nadmiarem niewykorzystanych metod.