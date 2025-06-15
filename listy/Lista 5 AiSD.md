#TODO naprawić obrazki!

# Zadanie 1

![[Pasted image 20250507155939.png]]

**Otoczka wypukła zbioru A** - najmniejszy zbiór wypukły zawierający A.

Nie da się go rozwiązać, bo w modelu drzew decyzyjnych możemy jedynie porównywać elementy w sposób $a < b$.

Żeby określić, czy punkt $(x_k, y_k)$ leży na lewo/prawo od prostej musimy (przechodzącej przez punkty $(x_i, y_i)$, $(x_j, y_j)$) obliczyć wyrażenie $(x_j - x_i)(y_k - y_i) - (x_k - x_i)(y_j - y_i)$.

Nie mamy narzędzi, żeby to zrobić w naszym modelu drzew decyzyjnych.

---

# Zadanie 2

![[Pasted image 20250507162505.png]]

Pokażemy to poprzez redukcję problemu sortowania do problemu znajdowania otoczki wypukłej.

**WAŻNE:** Powiedzieć, że w modelu liniowych drzew decyzyjnych problem sortowania również ma dolną granicę $\Omega(n\:log\:n)$. 

Niech $S=(x_1, x_2, ..., x_n)$ to dane wejściowe dla problemu sortowania.

Tworzymy z nich w czasie $O(n)$ $S'=((x_1,x_1^2), (x_2, x_2^2), ..., (x_n, x_n^2))$, dane dla algorytmu $A$ rozwiązującego problem otoczki wypukłej.

Uruchamiamy program $A$ na danych $S'$ i dostajemy $S''=((x_{i_1},x_{i_1}^2), (x_{i_2},x_{i_2}^2), ...,(x_{i_n},x_{i_n}^2))$, skąd możemy wyciągnąć posortowane punkty $x_{i_1}$. Dzieje się tak, bo punkty z $S'$ były punktami z paraboli, więc wszystkie muszą być w otoczce i będą posortowane względem współrzędnej x. (Możemy je dostać w 2-óch posortowanych składowych, bo otoczka nie musi się zaczynać od punktu najbardziej na lewo. W takim wypadku zaczynamy przechodzić przez punkty z $S''$ i patrzymy, kiedy przestaną rosnąć współrzędne x)

Niech $T(n)$ to czas działania algorytmu $A$ w modelu liniowych drzew decyzyjnych. Wtedy czas sortowania to $T(n) + O(n)$. Zatem $T(n) = \Omega(n \: log \: n)$, bo inaczej moglibyśmy sortować szybciej.

---

# Zadanie 3

![[Pasted image 20250509112311.png]]

Niech $S(v)$ to zbiór punktów $\mathbb{R}^n$, które osiągają wierzchołek $v$ w modelu liniowych drzew decyzyjnych. Wiemy z wykładu, że $S(v)$ jest zbiorem wypukłym.

Chcielibyśmy pokazać, że dla dowolnego liniowego drzewa decyzyjnego rozwiązującego problem 3SUM będzie ono miało przynajmniej $log_3{\:n!}$ liści (bo wtedy pokażemy, że jego dolną granicą jest $\Omega(n\: log n)$.

## Problem Różność Elementów

Na wykładzie pokazaliśmy, że problem Różność Elementów ma dolną granicę $\Omega(n\: log n)$ w modelu liniowych drzew decyzyjnych.

## Redukcja problemu Różność elementów do 3SUM

**Dane:** $(x_1, x_2, ..., x_n) \in \mathbb{R}^n$ 
**Wyjście:** Tak/Nie

$M = |max(x_k)| + 1$



---

# Zadanie 4

![[Pasted image 20250509120012.png]]

## Pseudokod

**Wejście:** tablica $S$
**Wyjście:** TAK, jeśli $\exists \:1 \leq i < j < k \leq n \:\: x_i + x_j + x_k = 0$, NIE w przeciwnym przypadku

```
sort(S)
n = len(S)
for i = 0..n-2:
	a = S[i]
	start = i + 1
	end = n - 1
	while start < end:
		b = S[start]
		c = S[end]
		if a + b + c == 0:
			print "TAK"
			return
		if a + b + c > 0:
			end -= 1
		else:
			start += 1
```

## Dowód poprawności

Załóżmy, że istnieją $a,b,c$, które sumują się do 0. (zakładamy $a<b<c$, bo posortowaliśmy tablicę $S$)

Skoro wskaźniki przesuwają się tylko w jedną stronę to w pewnym momencie będziemy mieli $S[i] = a$. 

Teraz jak jesteśmy w pętli while to przesuwamy wskaźniki start i end.

**Lemat** Jeśli start lub end wskazują już na docelowe b lub c, to nasz program ich 
nie przesunie.
**D-d**
BSO niech $S[end]=c$. Niech $S[start]= b'$, wtedy $b'<b$, czyli $a+b'+c < a+b+c=0$. Zatem nasz program przesunie start o 1 w prawo. 

Skoro mamy a ustawione to nasz program przesuwa sobie wskaźniki start i end. Kiedy jednym z nich trafi na docelowe a lub b, to nie będzie już go przesuwać. Wtedy będzie przesuwał ostatni wskaźnik aż natrafi na trzecią szukaną liczbę.

## Złożoność

Pętla for wykonuje się n-1 razy. Dla każdego i wewnętrzna pętla wykona się maksymalnie n-i-1 razy. Czyli łącznie mamy $O(n^2)$.

# Zadania 6

#TODO Treść

Problem $3SUM$ dostaje na wejście $n$ liczb rzeczywistych $x_{1},\dots,x_{n}$.
Będziemy chcieli przekształcić je na punkty $\mathbb{R}^{2}$ w taki sposób, by otrzymać $(x_{1},x_{1}^{3}),\dots,(x_{n},x_{n}^{3})$.

Weźmy trzy wartości $a,b,c$ i sprawdźmy, czy punkty $(a,a^{3}),(b,b^{3}),(c,c^{3})$ są współliniowe, gdy się zerują:
$$\begin{align*}
\frac{1}{2}(a^{3}(c-b) + b^{3}(a-c) + c^{3}(b-a)) &= 0\\
a^{3}(c-b) + b^{3}(a-c) + c^{3}(b-a) &= 0\\
a^{3}(c-b) + b^{3}(a-c) + c^{3}(b-a) &+ \\
\boxed{
a^{2}b^{2}-ab^{2}c + abc^{2}-a^{2}c^{2}
+a^{2}bc-a^{2}b^{2} + b^{2}c^{2}-abc^{2}
+a^{2}c^{2}-a^{2}bc + ab^{2}c - b^{2}c^{2}} &= 0\\
(a^{2}c - a^{2}b + b^{2}a-b^{2}c + c^{2}b-c^{2}a)(a+b+c) &= \\
(a^{2}c - a^{2}b - abc + ab^{2} -ac^{2} + abc + bc^{2}-b^{2}c)(a + b + c) &= \\
(a - c)(a - b)(c - b)(a + b + c) &= 0
\end{align*}$$
Wychodzimy od wzoru na pole trójkąta (tak naprawdę [[Wyznacznik Macierzy]]).
Następnie przekształcamy do postaci, która jest zerowa tylko dla $a + b + c=0$, co wystarcza, bo bierzemy parami różne punkty.

Otrzymujemy więc $\text{punkty współliniowe}\iff\text{3SUM}$.

#### Co Jeżeli Nie Bierzemy Parami Różnych Punktów?

Wtedy by algorytm działał poprawnie musimy zagwarantować, by do algorytmu znajdującego punkty współliniowe trafiły wyłącznie elementy *różne* – inaczej znajdziemy trywialne proste przechodzące przez wiele punktów w *jednym punkcie*.

To można zrobić bardzo prosto w czasie $O(n\log n)$ na początku sortując wszystkie wartości, a następnie eliminując powtórzenia.
Dla każdej powtarzającej się wartości sprawdzamy dodatkowo wyszukiwaniem binarnym, czy istnieje odpowiadająca tej parze trzecia wartość taka, że będą się sumować do zera.
Przy okazji być może znajdziemy trójkę składającą się z samych zer.

# Zadanie 7

#TODO Treść

Zdefiniujmy sekwencje $X_{i},Y_{i} : i\in\{1,\dots,2n\}$ w taki sposób, by porównanie $X_{k}[i] < Y_{k}[j]$ miało taką samą wartość dla $2n-1$ sekwencji.
Wtedy będziemy mogli ułoży algorytm adwersarza, który dla każdego zapytania o porównanie będzie odpowiadał w taki sposób, by odrzucić tylko dokładnie jedną parę sekwencji.

Niech *standardową* sekwencją będzie taka w której mamy kolejność:
$$X[1] < Y[1] < X[2] < Y[2] < \dots < X[n] < Y[n]$$
Dalej weźmy $n$ sekwencji w którym *jedynie* $X[i]$-ty element przesunięty jest o jedną w prawo w ciągu nierówności.
Kolejne $n-1$ sekwencji można uzyskać przesuwając po kolei przesuwając $X[i]$-te elementy w lewo w ciągu nierówności (nie można przesunąć pierwszego, więc dlatego o jeden mniej).

Teraz po kolei rozważmy dla ilu sekwencji prawdziwe są kolejne porównania:

|               | $i < j-1$ | $i = j-1$              | $i=j$                   | $i=j+1$                | $i > j+1$ |
| ------------- | --------- | ---------------------- | ----------------------- | ---------------------- | --------- |
| $X[i] < Y[j]$ | T         | T                      | T oprócz $X[i]$ w prawo | F oprócz $X[i]$ w lewo | F         |
| $Y[i] < X[j]$ | T         | T oprócz $X[i]$ w lewo | F oprócz $X[i]$ w prawo | F                      | F         |
Czyli faktycznie będziemy potrafili eliminować co najwyżej jedną sekwencję każdym porównaniem.

# Zadanie 8

#TODO 

> Mniej więcej trzeba pokazać, że można wymusić by element największy przegrał z $\lceil \log_{2}n \rceil$ innymi elementami, a wtedy wyznaczenie drugiego-największego wymaga wybrania największego z przegranych.
