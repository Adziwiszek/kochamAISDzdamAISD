**Punkt wyjścia** konstrukcja słownika

Zakładamy, że uniwersum $U$ jest duże.

Chemy mieć szybko-wyliczalną funkcję $h$ do liczenia w jakim  miejscu w wektorze
$R$ będzie $x$. Powinna "zachowywać się" jak funkcja losowa.

Przykłady funkcj haszujących:
- h(k) = k mod p, p - pierwsza, równa m
- $h(k) = \lfloor m(kA - \lfloor kA \rfloor) \rfloor$, $A\in (0,1)$ np $\frac{\sqrt{5} - 1}{2}$

# Wstawianie

Liczymy $h(k)$ i wstawiamy $k$ na listę w odpowiednim miejscu.

# Find

liczymy $h(k)$ i patrzymy czy w odpowiedniej liście znajduje się $k$.

# Oczekiwany czas

$m$ - rozmiar tablicy
$n$ - liczba kluczy wstawionych do słownika

Jaka jest oczekiwana długość listy? $\frac{n}{m}$ NAUCZYĆ SIĘ JAK TO POKAZAĆ FORMALNIE

Każda lokalizacja w tablicy jest tak samo prawdopodobna, ma 
prawdopodobieństwo $\frac{1}{m}$.

## Find(k)

koszt = $O(\frac{n}{m})$


Zakładamy, że tablica staje się za mała, gdy $n=m$.

Co robić, gdy tablica $R$ jest już za mała? Operacje są wtedy za drogie (nie w 
czasie stałym)

Robimy nową tablicę $R'$ o rozmiarze $2m$ i przechodzimy przez całą tablicę $R$ 
przehaszowując kluczę z $R$ do $R'$.
 
~~Mieliśmy $k_1 = \Theta(m)$ kluczy~~

Zakładamy, że tablica staje się za mała, gdy $n=m$.

Robimy przehaszowanie $n$ kluczy w czasie $O(n)$.

(*) Wstawiamy $n$ kluczy

przehaszowujemy $2n$ kluczy w $O(2n)$

Możemy obarczyć każdy wstawiony klucz w (*) 2 jednostkami, opłacą one koszt
przehaszowania tych $2n$ kluczy

Ustawiamy próg na zmniejszanie tablicy (np nie więcej niż $\frac{1}{4}$ pozycji
jest zajęta). Można wrzucić koszt zmniejszania w amortyzacje.

# Metody pamiętania elementów

## Adresowanie otwarte

Nie mamy list, umieszczamy klucze na liście $R$. Co zrobić jak wystąpi kolizja?

### Rozwiązywanie kolizji

teraz mamy funkcję haszującą z dwoma parametrami $h(k, i)$ (i to numer próby).

robimy $h(k, 0), h(k, 1), \dots, h(k, m-1)$ prób, chcemy, żeby to była permutacja
liczb $0,1,...,m-1$

**Metoda liniowa**

$h'(k)$ - pierwotna funkcja haszująca

$h(k, i) = (h'(k) + i)\mod m$

Jak robimy Find(k) to powtarzamy tę sekwencję aż napotkamy ten klucz, albo trafimy
na pustą komórkę.

Jak usuwamy element to usuwamy go, ale wstawiamy w jego komurce status, że 
kiedyś był tam element, żeby Find(k) działał poprawnie.

Przy metodzie kwadratowej jest tendencja do robienia się zlepków.

**Metoda kwadratowa**

$h(k, i) = (h'(k) + c_1 \cdot i + c_2 \cdot i^2)\mod m$

Ta metoda ma troche mnieszą tendencję do robienia zlepków.

**Podwójne haszowanie**

$h(k, i) = (h_1(k) + i\cdot h_2(k))\mod m$

Z tą metodą dostajemy $n^2$ możliwych permutacji

Zał. $h(k, 0), ..., h(k, m-1)$ to losowa permutacja liczb $0, 1, \dots, m-1$
**Fakt** 
przy tym założeniu i $\alpha = \frac{n}{m} \leq 1$ to oczekiwana liczba prób
w poszukiwaniu zakończonym fiaskiem $\leq \frac{1}{1-\alpha}$

A w poszukiwaniu zakończonym sukcesem $\leq \frac{1}{\alpha} \cdot \ln \frac{1}{1-\alpha} + \frac{1}{\alpha}$
DOWÓD TEGO JEST W CORMENIE

# Haszowanie uniwersalne

**Def** Niech $H$ - rodzina funkcji haszujących $U \rightarrow \{0,\dots, m-1\}$

$H$ nazywamy rodziną uniwersalną, jeśli:

$$
\forall x,y \in U \;\; x\neq y. \;\;  |\{h \in H : h(x) = h(y)\}| \leq \frac{|H|}{m}
$$

$k_1, \dots, k_n$ - dowolny zbiór kluczy

Oczekiwana liczba kolizji, w których bierze udział ustalony (ale dowolny) 
klucz k $\leq 1$.

**Przykład** rodziny uniwersalnej

Niech $p$ - liczba pierwsza większa niż moc uniwersum
$$
a \in Z_{p}^{*} \;\; b \in Z_{p} \;\;\;\; h_{a,b} (x) = ((ax + b) \mod p) \mod m
$$

**Fakt**
Zbiór $H_{p, m} = \{h_{a,b}...\}$ jest rodziną uniwersalną
