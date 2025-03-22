# Krok po kroku analiza powstawania cyklu

## Tabela routingu przed awarią (koszt do E)
| Router | Przez | Koszt |
|--------|-------|-------|
| A      | B     | 3     |
| A      | C     | 3     |
| B      | D     | 2     |
| C      | D     | 2     |
| D      | E     | 1     |

---

## Krok 1: Awaria połączenia D – E
| Router | Przez | Koszt |
|--------|-------|-------|
| D      | -     | ∞     |

D oznacza, że E jest nieosiągalne i ogłasza to sąsiadom (B, C).

---

## Krok 2: B i C otrzymują aktualizację od D
| Router | Przez | Koszt |
|--------|-------|-------|
| B      | D     | ∞     |
| C      | D     | ∞     |

Oba routery wiedzą, że D już nie ma połączenia z E.

---

## Krok 3: B i C szukają alternatywnej drogi
| Router | Przez | Koszt |
|--------|-------|-------|
| B      | C     | 3     |
| C      | B     | 3     |

Każdy z nich zakłada, że drugi nadal ma działającą trasę do E i zwiększa koszt.

---

## Krok 4: Powstanie pętli
| Router | Przez | Koszt |
|--------|-------|-------|
| B      | C     | 4     |
| C      | B     | 4     |

Koszt wzrasta, ale pakiety krążą między B i C w pętli.

---

## Krok 5: Kontynuacja błędnych aktualizacji
| Router | Przez | Koszt |
|--------|-------|-------|
| B      | C     | 5     |
| C      | B     | 5     |

Każda aktualizacja zwiększa koszt, ale sieć nie może dotrzeć do E.

---

## Krok 6: "Liczenie do nieskończoności"
| Router | Przez | Koszt |
|--------|-------|-------|
| B      | C     | ∞     |
| C      | B     | ∞     |

Po wielu iteracjach koszt rośnie do nieskończoności, aż algorytm się ustabilizuje.