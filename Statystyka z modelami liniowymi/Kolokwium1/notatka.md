# Kolokwium 1: notatka (wykłady 1–3, listy 1–4)

## 1. Podstawy

- **Próba losowa**: $X_1,\dots,X_n$ są iid. Łączna gęstość to $\prod f(x_i,\theta)$.
- **Statystyka**: dowolna funkcja próby. **Estymator** $\hat\theta$: statystyka, którą szacujemy $\theta$.
- **Rachunek**:
  - $E(aX+bY)=aEX+bEY$ (zawsze)
  - $\mathrm{var}(aX+b)=a^2\mathrm{var}X$
  - $\mathrm{var}(X+Y)=\mathrm{var}X+\mathrm{var}Y$ (gdy niezależne)
  - $EX^2=\mathrm{var}X+(EX)^2$ ← kluczowe w zadaniach typu $aX^2+bY^2$
- **Sumy**:
  - $\sum B(1,p)\sim \mathrm{Bin}(n,p)$
  - $\sum N(\mu,\sigma^2)\sim N(n\mu,n\sigma^2)$
  - $\sum\Gamma(a,\theta)\sim\Gamma(na,\theta)$, gdy $\theta$ jest parametrem skali
  - $\sum \mathrm{Pois}(\lambda)\sim\mathrm{Pois}(n\lambda)$

## 2. Własności estymatorów

| pojęcie | wzór |
|---|---|
| obciążenie | $\mathrm{bias}=E\hat\theta-\theta$ |
| nieobciążony | $E\hat\theta=\theta$ |
| asympt. nieobciążony | $E\hat\theta_n\to\theta$ |
| MSE | $E(\hat\theta-\theta)^2=\mathrm{bias}^2+\mathrm{var}$ |

- $\bar X$: $E\bar X=\mu$, $\mathrm{var}\bar X=\sigma^2/n$.
- $S^2=\frac1{n-1}\sum(X_i-\bar X)^2$ jest nieobciążony dla $\sigma^2$. Tożsamość: $\sum(X_i-\bar X)^2=\sum X_i^2-n\bar X^2$.
- **Średnia ważona** $\sum w_iX_i$ jest nieobciążona dla $\mu \iff \sum w_i=1$. Ma wtedy $\mathrm{var}=\sigma^2\sum w_i^2$, a najmniejszą wariancję dają równe wagi.
- Porównanie dwóch nieobciążonych estymatorów: lepszy ma mniejszą wariancję (wtedy też mniejszy MSE).

### Jak policzyć wariancję estymatora

**Reguły**
- $\mathrm{var}(cT)=c^2\mathrm{var}T$
- niezależne $X_i$: $\mathrm{var}\sum a_iX_i=\sum a_i^2\mathrm{var}X_i$
- $\mathrm{var}T=ET^2-(ET)^2$
- normalny: $\sum(X_i-\mu)^2/\sigma^2\sim\chi^2_n$ (wariancja $2n$), stąd $\mathrm{var}S^2=\frac{2\sigma^4}{n-1}$

**Przypadki**
1. **Kombinacja liniowa**: stałe do kwadratu, potem suma wariancji. Np. $\mathrm{var}\frac{X_1+2X_2+3X_3}6=\frac{14}{36}\mathrm{var}X$.
2. **Min lub max**: $F_{\max}=F^n$, $f_{\max}=nF^{n-1}f$. Liczysz $ET$ i $ET^2$, potem odejmujesz. Np. dla $U(0,\theta)$: $\mathrm{var}\max=\frac{n\theta^2}{(n+1)^2(n+2)}$.
3. **$g(\bar X)$ nieliniowe**: metoda delta, $\mathrm{var}\,g(\bar X)\approx g'(\mu)^2\sigma^2/n$. Np. dla $1/\bar X$ z Exp o tempie $\theta$: $\approx\theta^2/n$.
4. **MLE przy dużym $n$**: $\mathrm{var}\approx 1/(nI(\theta))$.

## 3. Informacja Fishera, Cramér–Rao, efektywność

- **Informacja Fishera**: $I(\theta)=E\left(\frac{\partial\log f}{\partial\theta}\right)^2=-E\,\frac{\partial^2\log f(X,\theta)}{\partial\theta^2}$. W próbie jest jej $nI(\theta)$.
  - Pomocniczo: $E\,\partial_\theta\log f=0$.
  - Warunki regularności: nośnik **nie zależy** od $\theta$ (np. dla $U[0,\theta]$ CR nie działa).
- **Nierówność Craméra–Rao**: $\mathrm{var}\hat\theta\ge\frac{(m'(\theta))^2}{nI(\theta)}$, gdzie $m=E\hat\theta$. Dla nieobciążonego: $\mathrm{var}\hat\theta\ge\frac1{nI(\theta)}$.
- **Efektywny**: nieobciążony i $\mathrm{var}\hat\theta=\frac1{nI(\theta)}$.
- **Efektywność bezwzględna**: $e(\hat\theta)=\dfrac{1/(nI)}{\mathrm{var}\hat\theta}\le1$. **Asymptotycznie efektywny**: $e\to1$.
- **Efektywność względna**: $e(\hat\theta_1,\hat\theta_2)=\dfrac{\mathrm{var}\hat\theta_2}{\mathrm{var}\hat\theta_1}$. Gdy $>1$, $\hat\theta_1$ jest lepszy.

**Przepis „pokaż, że jest efektywny”:**
1. Policz $E\hat\theta=\theta$.
2. Policz $\mathrm{var}\hat\theta$.
3. Policz $\log f$, potem $\partial^2_\theta$, potem $I=-E(\cdot)$.
4. Sprawdź, czy $\mathrm{var}\hat\theta=1/(nI)$.

Uwaga: $n$ to **liczba wszystkich obserwacji** w próbie, także wtedy, gdy estymator używa tylko części z nich.

## 4. MLE (estymator największej wiarogodności)

- $L(\theta)=\prod f(x_i,\theta)$, $l=\log L=\sum\log f(x_i,\theta)$, $\hat\theta_{MLE}=\arg\max L$.
- **Przepis (nośnik niezależny od θ)**:
  1. Rozwiąż $l'(\theta)=0$.
  2. Sprawdź, że $l''<0$.
- **Nośnik zależy od θ** (np. $U(0,\theta)$, $x\ge\theta$): nie różniczkujemy. Zapisujemy $L$ z indykatorem i patrzymy na monotoniczność:
  - $f=\frac1\theta$ na $(0,\theta]$: $L=\theta^{-n}\mathbb 1\{\max x_i\le\theta\}$ maleje, więc $\hat\theta=\max X_i$.
  - $f=2x/\theta^2$ na $(0,\theta]$: $L\propto\theta^{-2n}\mathbb 1\{\max\le\theta\}$, więc $\hat\theta=\max X_i$.
  - $f=e^{\theta-x}$ dla $x\ge\theta$: $L=e^{n\theta-\sum x}\mathbb 1\{\min x_i\ge\theta\}$ rośnie, więc $\hat\theta=\min X_i$.
- **Ograniczony zbiór parametrów**: $L$ rośnie do $\bar x$, a potem maleje, więc rzutujemy $\bar X$ na dozwolony przedział.
  - $\theta\in[1/3,1]$: $\hat\theta=\max(\bar X,1/3)$.
  - Poisson z $\theta\ge5$: $\hat\theta=\max(\bar X,5)$.
  - $\theta\le1/2$: $\min(\bar X,1/2)$.
- **Niezmienniczość**: $\widehat{g(\theta)}_{MLE}=g(\hat\theta_{MLE})$. Przykłady:
  - Exp ze średnią $\theta$: $\hat P(X\le2)=1-e^{-2/\bar X}$.
  - Pois ($\theta\ge5$): $\hat P(X>2)=1-e^{-\hat\theta}(1+\hat\theta+\hat\theta^2/2)$, gdzie $\hat\theta=\max(\bar X,5)$.
- **Asymptotyka**: $\sqrt n(\hat\theta-\theta_0)\xrightarrow{D}N\!\left(0,\frac1{I(\theta_0)}\right)$, czyli $\hat\theta\approx N(\theta,\frac1{nI(\theta)})$ (dla $n\ge30$).
- **Metoda delta**: $\sqrt n(g(\hat\theta)-g(\theta_0))\to N\!\left(0,\frac{g'(\theta_0)^2}{I(\theta_0)}\right)$.
- **Newton / estymator jednokrokowy**: $\hat\theta^{(1)}=\hat\theta^{(0)}-\dfrac{l'(\hat\theta^{(0)})}{l''(\hat\theta^{(0)})}$. Jako $\hat\theta^{(0)}$ bierzemy np. estymator z metody momentów. Wynik jest asymptotycznie efektywny.

## 5. Metoda momentów

- Przyrównaj $\hat m_k=\frac1n\sum X_i^k$ do $EX^k(\theta)$. Bierzesz tyle momentów, ile jest parametrów.
- Wygodniej: $\bar X=EX$ oraz $\hat\sigma^2=\frac1n\sum(X_i-\bar X)^2=\mathrm{var}X$.
- Estymatory z tej metody bywają mało efektywne, ale są dobrym startem dla metody Newtona.

| rozkład | momenty | estymatory MM |
|---|---|---|
| $N(\theta_1,\theta_2)$ | $EX=\theta_1$, $\mathrm{var}=\theta_2$ | $\hat\theta_1=\bar X$, $\hat\theta_2=\hat\sigma^2$ |
| $\Gamma(\theta_1,\theta_2)$ (z $\theta_2$ jako tempem) | $\theta_1/\theta_2$, $\theta_1/\theta_2^2$ | $\hat\theta_2=\bar X/\hat\sigma^2$, $\hat\theta_1=\bar X^2/\hat\sigma^2$ |
| log-normalny | $EX=e^{\theta_1+\theta_2/2}$, $EX^2=e^{2\theta_1+2\theta_2}$ | $\hat\theta_2=\ln\hat m_2-2\ln\hat m_1$, $\hat\theta_1=2\ln\hat m_1-\tfrac12\ln\hat m_2$ |
| Laplace ($b=\sqrt{\theta_2}$) | $EX=\theta_1$, $\mathrm{var}=2\theta_2$ | $\hat\theta_1=\bar X$, $\hat\theta_2=\hat\sigma^2/2$ |
| jednostajny $[\theta_1\pm\sqrt{3\theta_2}]$ | $EX=\theta_1$, $\mathrm{var}=\theta_2$ | $\hat\theta_1=\bar X$, $\hat\theta_2=\hat\sigma^2$ |
| geometryczny $(1-\theta)^x\theta$, $x\ge0$ | $EX=\frac{1-\theta}\theta$ | $\hat\theta=\frac1{1+\bar X}$ |

## 6. Ściąga rozkładów

$I$ to informacja Fishera dla jednej obserwacji. Wszystkie MLE z tej tabeli (oprócz U) są efektywne lub asymptotycznie efektywne.

| rozkład | $EX$ | $\mathrm{var}X$ | $I(\theta)$ | MLE | MLE ≈ |
|---|---|---|---|---|---|
| $B(1,\theta)$ | $\theta$ | $\theta(1-\theta)$ | $\frac1{\theta(1-\theta)}$ | $\bar X$ | $N(\theta,\frac{\theta(1-\theta)}n)$ |
| $\mathrm{Bin}(m,\theta)$ | $m\theta$ | $m\theta(1-\theta)$ | $\frac m{\theta(1-\theta)}$ | $\bar X/m$ | efektywny |
| $\mathrm{Pois}(\theta)$ | $\theta$ | $\theta$ | $\frac1\theta$ | $\bar X$ | $N(\theta,\frac\theta n)$ |
| $N(\theta,\sigma^2)$, $\sigma$ znane | $\theta$ | $\sigma^2$ | $\frac1{\sigma^2}$ | $\bar X$ | $N(\theta,\frac{\sigma^2}n)$, dokładnie |
| $N(\mu,\theta)$, $\mu$ znane | $\mu$ | $\theta$ | $\frac1{2\theta^2}$ | $\frac1n\sum(X_i-\mu)^2$ | $N(\theta,\frac{2\theta^2}n)$, efektywny |
| Exp, $EX=\theta$ (skala) | $\theta$ | $\theta^2$ | $\frac1{\theta^2}$ | $\bar X$ | $N(\theta,\frac{\theta^2}n)$ |
| Exp, $EX=1/\theta$ (tempo) | $1/\theta$ | $1/\theta^2$ | $\frac1{\theta^2}$ | $1/\bar X$ | $N(\theta,\frac{\theta^2}n)$ |
| $\Gamma(\alpha,\theta)$, skala, $\alpha$ znane | $\alpha\theta$ | $\alpha\theta^2$ | $\frac\alpha{\theta^2}$ | $\bar X/\alpha$ | $N(\theta,\frac{\theta^2}{n\alpha})$ |
| $\beta(\theta,1)$ | | | $\frac1{\theta^2}$ | $-n/\sum\log X_i$ | $N(\theta,\frac{\theta^2}n)$ |
| $U(0,\theta)$ | $\theta/2$ | $\theta^2/12$ | brak (nieregularny) | $\max X_i$ | — |

Dodatkowe fakty:
- $U(a,b)$: $E\min=a+\frac{b-a}{n+1}$, $E\max=b-\frac{b-a}{n+1}$.
- Rozkład geometryczny liczący próby do sukcesu: $E=1/p$, $\mathrm{var}=(1-p)/p^2$.
- Kostka: $E=3.5$, $\mathrm{var}=35/12$.

## 7. Wyniki z list (do sprawdzenia)

**Lista 1**
- **Z1**: $Y\sim\mathrm{Bin}(n,p)$, $E(Y/n)=p$, $\mathrm{var}(Y/n)=\frac{p(1-p)}n$.
- **Z2b**: $Y\sim\Gamma(na,\theta)$, $c=\frac1{na}$.
- **Z3**:
  - a) $E=3.5$, $\mathrm{var}=\frac{35}{1200}\approx0.029$, $\sigma\approx0.171$
  - b) suma 100 rozkładów geometrycznych z $p=1/6$: $E=600$, $\mathrm{var}=3000$, $\sigma\approx54.8$
  - c) $\mathrm{Bin}(100,\tfrac38)$: $E=37.5$, $\mathrm{var}=23.44$, $\sigma\approx4.84$
- **Z4**:
  - a) $N(n\mu,n\sigma^2)$
  - b) $N(\sqrt n\mu,\sigma^2)$
  - c) $Y=\frac{a^TX}{\|a\|^2}a$, gdzie $a^TX\sim N(\mu\sum a_i,\sigma^2\|a\|^2)$
- **Z6**:
  - a) oba nieobciążone. $\mathrm{var}\hat\lambda_1=\frac\lambda3$, $\mathrm{var}\hat\lambda_2=\frac{7\lambda}{18}$, więc lepszy $\hat\lambda_1$.
  - b) oba nieobciążone. $\mathrm{var}\hat\theta_1=\frac{\theta^2}9$, $\mathrm{var}\hat\theta_2=\frac{\theta^2}8$, więc lepszy $\hat\theta_1$.
- **Z7**:
  - a) $(1-a)(\sigma^2+4)+a(\sigma^2+9)=\sigma^2$, stąd $a=-\frac45$
  - b) $a+4b=0$ oraz $a+3b=1$, stąd $a=4$, $b=-1$
- **Z8**:
  - $\min$ jest asympt. nieobciążony dla $a$
  - $\max$ jest asympt. nieobciążony dla $b$
  - $\bar X$ oraz $\frac{X_{n-1}+X_n}2$ są nieobciążone dla $\frac{a+b}2$

**Lista 2**
- **Z2** ($6n$ obserwacji, granica CR $=\frac\lambda{6n}$):
  - $\mathrm{var}\hat\lambda_1=\frac\lambda{3n}$, $e=\frac12$
  - $\mathrm{var}\hat\lambda_2=\frac\lambda{2n}$, $e=\frac13$
  - lepszy $\hat\lambda_1$; efektywny jest $\bar X$ ze wszystkich $6n$ obserwacji
- **Z3** ($n=4$, granica CR $=\frac{\theta^2}{4\alpha}$):
  - $\mathrm{var}\hat\theta_1=\frac{5\theta^2}{18\alpha}$, $e=0.9$
  - $\mathrm{var}\hat\theta_2=\frac{13\theta^2}{50\alpha}$, $e=\frac{25}{26}$
  - lepszy $\hat\theta_2$
- **Z4** (Rayleigh):
  - $c=\sqrt{2/\pi}$
  - $EX^2=2\sigma^2$, $\mathrm{var}(c\bar X)=\frac{(4-\pi)\sigma^2}{\pi n}$
  - $I=\frac4{\sigma^2}$, granica CR $=\frac{\sigma^2}{4n}$
  - $e=\frac{\pi}{4(4-\pi)}\approx0.915$

**Lista 3**
- **Z1**: MLE z tabeli w sekcji 6.
- **Z2**: a) $\min X_i$, b) $\max X_i$.
- **Z3**: a) $\max(\bar X,\tfrac13)$, b) $\max(\bar X,5)$.
- **Z4**: z niezmienniczości (sekcja 4).

**Lista 4**: tabela w sekcji 5.
