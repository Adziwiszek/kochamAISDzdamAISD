# Algorytm Quicksort

```
def quicksort(A[1..n], p, r)
    if r - p jest małe then 
        insert_sort(A[p..r])
    else
        choose_pivot(A, p, r)
        q <- partition(A, p, r)
        quicksort(A, p, q)
        quicksort(A, q + 1, r)
```

# Implementacja procedury partition

Zakładamy, że w momencie wywołania `partition(A, p, r)` pivot znajduje się w
komórce `A[p]`. 

Procedura przestawia elementy podtablicy `A[p..r]` dokonując
jej podziału na dwie części: w pierwszej `A[p..q]` są elementy nie większe od
pivota `q`, w drugiej `A[q+1..p]` są elementy nie mniejsze od pivota.

Granica tego podziału, wartość `q` jest przekazywana jako wynik procedury.

```
def partition(A[1..n], p, r)
    x <- A[p] // zakładamy, że pivot jest w komórce A[p]
    i <- p - 1
    j <- r + 1
    while i < j do
        // pomijamy te elementy, które są już w dobrych częściach tablicy
        repeat j <- j - 1 until A[j] <= x  
        repeat i <- i + 1 until A[i] >= x
        // jeśli i < j w tym miejscu to są dwa elementy A, które są w złych
        // częściach tablicy, więc je zamieniamy
        // w p.p. przeszliśmy już cały fragment tablicy, więc zwracamy pivot
        if i < j 
            then zamień A[i] i A[j] miejscami
            else return j   
```

**Fakt 1** Koszt procedury `partition(A[1..n], p, r)` wynosi $\Theta(r-p)$

Fakt ten wynika z tego, że procedura kończy się tylko gdy `i > j`, więc dwie
pętle zmieniające `i` i `j` muszą się wykonać $r-p$ razy.

# Wybór pivota

Może się wydawać, że mediana jest najlepszym pivotem, bo idealnie podzieli
tablicę na dwie równe części. Jest algorytm do znajdowania mediany w czasie
liniowym, dzięki niemy moglibyśmy mieć quicksort w $\Theta(n\;log\;n)$, ale
stałe w tym algorytmie są niepraktyczne.

## Prosta metoda deterministyczna

Jako pivot wybieramy pierwszy element tablicy. Dla danych uporządkowanych może
to skutkować kwadratowym czasem działania (procedurat partition będzie 
produkować jedno elementowe zbiory), ale dla danych losowych algorytm działa
bardzo szybko.

## Prosty wybór zrandomizowany

```
def choosepivot(A[1..n], p, r)
    i <- random(p, r)
    zamień A[p] i A[i] miejscami
```

Przy takim wyborze również może się zdarzyć, że algorytm będzie działał w
czasie kwadratowym, jednak takie prawdopodobieństwo jest bardzo małe.

Nie istnieją dane lepsze i gorsze. Na każdych algorytm może działać jednakowo
szybko i na każdych może się trafić czas kwadratowy.

## Mediana z małej próbki

Można jako pivot brać medianę z trzech elementów (trzech wylosowanych lub 
pierwszego, środkowego i ostatniego). Płacimy za to cenę dodatkowych porównań
(i losowania liczb), ale w praktyce zastosowanie 'mediany z trezch' przyspiesza
quicksort o kilka, a nawet kilkanaście procent.

# Oczekiwany koszt algorytmu

Załóżmy, że jako pivot jest wybierany z jednakowym prawdopodobieństwem dowolny
element tablicy. Pokażemy, że przy tym założeniu oczekiwany koszt algorytmu
quicksort to $\Theta(n\;log\;n)$. Zakładamy, że wszystkie elementy tablicy są
różne.

Niech $n=r-p+1$ oznacza liczbę elementów w tablicy `A[p..r]`, niech:

$$
rank(x, A[p.r])=|\{ j\;:\;p \leq j \leq r \; \wedge \; A[j] \leq x\}|
$$

Czyli $rank(x, A[p.r])$ to liczba elementów w poddablicy `A[p..r]` mniejszych od $x$.

W momencie wywołania partition w `A[p]` znajduje się losowy element z `A[p..r]`,
więc:

$$
\forall i=1...n\;\;\; \mathbf{Pr} [rank(A[p], A[p..r]) = i] = \frac{1}{n}
$$

Wynik procedury partition zależy od wartości $rank(x, A[p.r])$. Gdy jest ona
równa $i$ (dla $i = 2..n$), to wynikiem partition jest $p+i-2$. Gdy jest równa
1 to wynikiem jest $p$.

Czyli zmienna `q` z procedury quicksort przyjmuje wartość $p$ z 
prawdopodobieństwem $\frac{2}{n}$, a każdą z pozostałych wartości (tj. $p+1,p+2,...,r-1$)
z prawdopodobieństwem $\frac{1}{n}$.

Oczekiwany czas działania partition wyraża się równaniem:

$$
\begin{cases}
    T(1) = 1 \\
    T(n) = \frac{1}{n}[(T(1) + T(n-1)) + \sum_{d=1}^{n-1}(T(d) + T(n -d))] + \Theta(n)
\end{cases}   
$$

Zmienna $d=q-p+1$ oznacza długość pierwszej z poddtablic.

Ponieważ $T(1) = \Theta(1)$, a $T(n-1)$ w najgorszym przypadku jest równe $\Theta(n^2)$, więc

$$
\frac{1}{n}(T(1) + T(n-1)) = O(n)
$$

Pozwala nam to pominąć ten składnik, bo jest on uwzględniany w ostatnim członie 
sumy. Więc:

$$
T(n) = \frac{1}{n}\sum_{d=1}^{n-1}(T(d) + T(n -d)) + \Theta(n)
$$

W tej sumie każdy element $T(k)$ dodawany jest dwukrotnie, możemy ją przepisać
jako:

$$
T(n) = \frac{2}{n}\sum_{k=1}^{n-1}T(k) + \Theta(n)
$$

Zakładamy, że:

$$
T(n) = \frac{2}{n}\sum_{k=1}^{n-1}T(k) + \Theta(n) \leq an\;log\;n + b
$$

dla pewnych stałych $a,b>0$. Naszym zadaniem jest pokazać, że takie stałe 
istnieją. Bierzemy $b$ odpowiednio duże by $T(1) \leq b$. Dla $n>1$ mamy:

$$
T(n) = \frac{2}{n}\sum_{k=1}^{n-1}(ak\;log\;k + b) + \Theta(n) 
\leq \frac{2a}{n}\sum_{k=1}^{n-1}k\;log\;k + \frac{2b}{n}(n-1) + \Theta(n) 
$$

Oszacujemy $\frac{2a}{n}\sum_{k=1}^{n-1}k\;log\;k$, tak, żeby pozbyć się składnika $\Theta(n)$. 

**Fakt 2** $\sum_{k=1}^{n-1}k\;log\;k \leq \frac{1}{2}n^2 log\;n - \frac{1}{8}n^2$

**D-d**
Rozbijamy sumę na dwie części:

$$
\sum_{k=1}^{n-1}k\;log\;k = \sum_{k=1}^{\lceil n/2 \rceil - 1}k\;log\;k +
\sum_{k=\lceil n/2 \rceil}^{n-1}k\;log\;k
$$

Szacujemy $log\;k \leq log\;\frac{n}{2}$ dla $k<\lceil n/2 \rceil$ oraz $log\;k \leq log\;n$ dla $k\geq\lceil n/2 \rceil$

$$
\begin{align*}
\sum_{k=1}^{n-1}k\;log\;k  
&\; \leq ((log\;n) - 1)\sum_{k=1}^{\lceil n/2 \rceil - 1}k
+ log\;n \sum_{k=\lceil n/2 \rceil}^{n-1}k \\
&\; = log\;n\sum_{k=1}^{n}k\;\; - \sum_{k=1}^{\lceil n/2 \rceil-1}k \\
&\; \leq \frac{1}{2}n(n-1)log\;n - \frac{1}{2}(\frac{n}{2}-1)\frac{n}{2} \\
&\; \leq \frac{1}{2}n^2 log\;n - \frac{1}{8}n^3
\end{align*}
$$

Teraz wracamy do $T(n)$:

$$
\begin{align*}
&\frac{2a}{n}\sum_{k=1}^{n-1}k\;log\;k + \frac{2b}{n}(n-1) + \Theta(n) \\
&\leq \frac{2a}{n}(\frac{1}{2}n^2 log\;n - \frac{1}{8}n^3) + \frac{2b}{n}(n-1) + \Theta(n) \\
&\leq an\;log\;n - \frac{a}{4}n + 2b + \Theta(n) \\
&= an\;log\;n + b + (\Theta(n) + b - \frac{a}{4}n)
\end{align*}
$$

Składową $(\Theta(n) + b - \frac{a}{4}n)$ możemy pominąć dobierając stałą $a$ tak, żeby
$\frac{a}{4} \geq \Theta(n) + b$. Dobór zależy tylko od stałej $b$ i od stałej ukrytej pod $\Theta$.
Możemy więc za $a$ przyjąć odpowiednio dużą stałą.

To kończy sprawdzanie, że $T(n) \leq an\;log\;n + b$ dla pewnych stałych $a,b>0$.

