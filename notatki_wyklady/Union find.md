# Union find

## Pierwszy sposób

mamy tablicę dla każdego elementu w jakim zbiorze on jest (mamy id dla zbiorów)
mamy tabelkę o długości $n$ i dla indeksu $i$ $t_i$ mówi w jakim podzbiorze jest $x_i$

Find $O(1)$

Union $O(n)$

## Modyfikacja

Dla każdego podzbioru nawlekamy jego elementy na listę. Mamy strukturę, w której
dla każdego zbioru mamy wskaźnik na pierwszy i na ostatni element tego ciągo-zbioru.


Find $O(1)$

Union -  max liczność podzbioru

## Kolejna modyfikacja

"mniejszy podciąg dołączamy do większego"

Teraz w tej strukturze trzymamy również długość listy dla każdego zbioru

mamy ciąg operacji do wykonania sigma
$\sigma: op_1, op_2, ..., op_m$

Mamy dwa tryby wykonania $\sigma$:
1) offline - ciąg $\sigma$ jest znany od początku, możemy zrobić jakieś optymizacje
2) online - tutaj ciąg $\sigma$ nie jest znany

Jaki jest sumaryczny koszt $\sigma$?

**Koszt Find** 
$\#Find * O(1) = O(m)$

**Koszt Union** 

Analiza groszkowa kosztu. Dodajemy groszek do elementu za każdym razem, gdy
Union przejdzie przez ten element.
Kosztem operacji union obciążamy elementy mniejszego zbioru (każdy jego element
obciążamy jedną jednostką, groszkiem)

Koszt wszystkich operacji Union to $\sum_{i=1}{n}$ obciążenie elementu i
możemy oszacować to przez maksymalne obciążenie pojedyńczego elementu
**Jakie jest maksymalne obciążenie pojedyńczego elementu**
Kiedy obciążamy element na początku to jest on w zbiorze jedno elementowym.
Następnym razem, gdy go obciążymy to będzie to przy Union ze zbiorem przynajmniej 
dwu elementowym, groszek będzie potem w zbiorze przynajmniej 4 elementowym.

I tak znowu, jeśli element zbioru 4 elementowego jest obciążany to znaczy, że 
złączyliśmy go ze zbiorem przynajmniej 4 elementowym.

Odp $\leq$ # ile razy element może być dołączany do większego podzbioru $\leq \:log\:n$
Średnie obciążenie jest nie większe niż log.
**Czyli koszt łączy Union $\leq\:n\:log\:n$**

Czy to musi być lista?

## Struktura drzewiasta 

- Każdy podzbiór to jest jedno poddrzewo
- Wskaźniki są tylko do rodzica
- Identyfikator podzbioru to korzeń drzewa

Na początku singletony wskazują na siebie.
Podczas łączenia singletonów robimy tak, że jeden wskazuje na drugiego jako na 
swojego rodzica.

### Łączenia dwóch drzew

Operacja Find to ilość wierzchołków ile musimy przejść do korzenia. 

**Operacja Union, zbalansowane łączenie**
Będziemy podłączać mniejsze drzewo (pod względem liczby wierzchołków) podwieszamy pod większe.

**Operacja $Find(v)$, kompresja ścieżek**
Koszt pojedynczej operacji to długość ścieżki, którą przejdziemy od $v$ od korzenia

Za każdym razem gdy odwiedzamy v to musimy przejść od ścieżki do korzenia.
Żeby zrobić optymalizację to podpinamy wszystkie wierzchołki (ze ścieżki z v do korzenia) do korzenia. Robimy to tak, że robimy jedno przejście od $v$ do korzenia, a potem drugie i każdy wierzchołek na ścieżce z $v$ do korzenia podpinamy do korzenia.

**Lemat** Każde drzewo o wysokości $h$ ma $\geq 2^h$ wierzchołków
**D-d**
Kiedy powstało drzewo o wysokości h to przyłączyliśmy drzewo o wysokości $h-1$ do jakiegoś większego. Z założenia indukcyjnego to dołączane ma $\geq 2^{h-1}$ 
wierzchołków. Skoro to do którego dołączamy jest większe to ono również ma $\geq 2^{h-1}$ wierzchołków.
Zatem drzewo o wysokości $h$ ma $\geq 2^{h}$ wierzchołków.

Niech $\sigma'$ to ciąg operacji Union powstały z wyrzucenia z $\sigma$ wszystkich
operacji Find. (alternatywnie to $\sigma$ z Find, które nie kompresują ścieżek)

**Def.** Rzędem wierzchołka $v$ względem ciągu operacji $\sigma$ jest wysokość 
$v$ w lesie powstałym po wykonaniu $\sigma'$

Patrzymy na $v$ i jego poddrzewo. Wysokość tego poddrzewa to rząd $v$.

**Lemat** Wierzchołków o rzędzie $r$ jest $\leq \frac{n}{2^r}$
**D-d** 
W poddrzewie $v$ jest co najmniej $2^r$ wierzchołków.
Jeśli jest jakiś inny wierzchołek o rzędzie $r$ to jest on w innym poddrzewie.
Zatem wierzchołków o rzędzie $r$ może być tyle ile można utworzyć niezależnych 
grup wierzchołków o wysokości $r$.
Nie może być innego wierzchołka w poddrzewie $v$ o rzędzie $r$. Żaden wierzchołek
powyżej $v$ mający w swoim poddrzewie poddrzewo $v$ nie ma rzędu $r$.

Zatem $\#$ wierzchołków o rzędzie $r$ $\leq$ liczba niezależnych podzbiorów o mocy $\geq 2^r$

**Lemat** Jeśli w trakcie wykonywania $\sigma$ $w$ staje się potomkiem $v$ to $rząd(w) \leq rząd(v)$

**Wniosek** maksymalny rząd wierzchołka $\leq\:log\:n$

**Def**
$F(0) = 1$
$F(i) = 2^{F(i-1)}$, dla $i > 0$

$\log^{*}n = min\{k: F(k) \geq n\}$

Rzędy wierzchołków dzielimy na grupy, rząd $i$ trafia do grupy $log^{*}i$

| $n$ | $\log^* n$ |
| --- | ---------- |
| 0   | 0          |
| 1   | 0          |
| 2   | 1          |
| 3   | 2          |
| 4   | 2          |
| 5   | 3          |
| 6   | 3          |
| ... | ...        |
| 15  | 3          |
| 16  | 3          |
| 17  | 4          |
| ... | ...        |



**Analiza kosztu wykonania $\sigma$**

$n$ - moc uniwersum (zał. $\#Union=n-1)$)
$m$ - $\#$ operacji Find

$koszt(\sigma) = koszt(Union) + koszt(Find)$

$koszt(Union) = O(n)$

Koszt pojedynczej instrukcji Find ~ Find(v) - długość ścieżki od $v$ do korzenia

Ten koszt rozdzielimy między:
- instrukcję Find(v)
- odwiedzane wierzchołki

Wykonująć Find(v) za odwiedzenie wierzchołka $u$ obciążamy jedną jednostką:
- intstrukcję Find(v), jeśli $u$
  - jest korzeniem
  - jest synem korzenia
  - $u$ ma rząd w innej grupie niż rząd ojca(u)
- $u$ w przeciwnym przypadku

jest $log^{*}n$ grup dla n wierzchołków

Pojęcia: rząd, grupa, 

## Szacujemy obciążenie instrukcji Find(v)

Jest co najwyżej $\log^{*}n + 2$ zmian grupy idąc z $v$ do korzenia  (syn korzenia i korzeń)

**Fakt** Instrukcja Find(v) zostanie obciążona $O(\log^{*}n)$ jednostkami.

## Szacujemy obciążenie wierzchołków

Zrobimy to oddzielnie dla każdej grupy rzędów.

Pytanie: Ile jest wierzchołków o rzędach w grupie g?
$$
= \sum_{r-rząd\;z\;grupy\;g} \# \; o\;rzędzie\;r 
$$

Korzystamy z oszacowania na liczbę wierzchołków o rzędzie r. Jest ich $< \frac{n}{2^r}$.

$$
\leq \sum_{r=F(g-1)+1}^{F(g)} \frac{n}{2^r}
$$

$$
\leq \frac{n}{2^{F(g-1)+1}} \cdot \sum_{k=1}^{\infty} \frac{1}{2^k}
$$

$$
= \frac{n}{2^{F(g-1)+1}} \cdot 2 = \frac{n}{2^{F(g-1)}} = \frac{n}{F(g)}
$$

Pytanie: Ile jest wierzchołków o rzędach w grupie g?
Odpowiedź: Nie więcej niż $\frac{n}{F(g)}$.

Każdy wierzchołek o rzędzie z grupy g może być obciążony nie więcej niż 
$F(g) - F(g-1)$ razy.

(Bo za każdym obciążeniem $v$ zmienia ojca na ojca' o wyższym rzędzie.
Jak zmieni na ojca który ma rząd w wyższej grupie to nie będziemy już obciążać
wierzchołka $v$, bo jego ojciec będzie miał rząd w wyższej grupie)

**Wniosek**
obciążenie wszystkich wierzchołków o rzędach w grupie g $\leq \frac{n}{F(g)} (F(g)-F(g-1)) \leq n$

**Wniosek**
Obciążenie wszystkich wierzchołków 
$\leq \#\;grup \cdot obciążenie \; wszystkich \; wierzchołków \; z \; grupy$
$\leq (\log^{*}n) \cdot n$

stąd koszt wszystkich findów $\leq (m+n) \log^{*}n$

**Notatki**
max rząd wierzchołka $\leq \log n$

max nr grupy $\leq \log^{*}(\log n) = (\log^{*}n) - 1$
