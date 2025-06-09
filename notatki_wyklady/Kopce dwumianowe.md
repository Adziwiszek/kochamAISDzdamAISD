# Definicja

Drzewa dwumianowe są zdefiniowane rekurencyjnie: $i$-te drzewo dwumianowe składa
się z korzenia oraz poddrzew: $B_0, B_1, \dots, B_{i-1}$.

![[Pasted image 20250529152152.png]]

## Fakt 1 
Drzewo $B_i$ zawiera $2^i$ wierzchołków

**D-d**
$n = 0$ $B_0$ zawiera $1 = 2^0$ wierzchołków.

$n > 0$ Drzewa $B_0, \cdots, B_{i-1}$ mają $\sum_{k=0}^{i-1} 2^k = 2^{i-1} - 1$
wierzchołków, co z korzeniem daje $2^i$.

## Definicja 1

Kopiec dwumianowy to zbiór drzew dwumianowych, które pamiętają elementy z 
uporządkowanego uniwersum zgodnie z porządkiem kopcowym.

## Definicja 2

Rzędem wierzchołka drzewa $T$ nazywamy liczbę jego dzieci. Rzędem $T$ jest rząd
jego korzenia.


Zakładamy, że dzieci każdego wierzchołka są zorganizowane w cykliczną listę
dwukierunkową. Ojciec pamięta wskaźnik do jednego z nich (np. o najmniejszym 
rzędzie)

# Operacje na kopcach dwumianowych

## Łączenie drzew dwumianowych - operacja join

Łączymy dwa drzewa $B_i$ (nigdy nie łączymy drzew o różnych rzędach).
Korzeń drzewa o większej wartości w wierzchołku staje się synem korzenia drzewa
o mniejszej wartości w korzeniu.

Koszt takiej operacji to $O(1)$

![[Pasted image 20250529153549.png]]

## makeheap

Tworzymy nowe drzewo $B_0$.

Koszt $O(1)$

## findmin

W każdym kopcu dwumianowym mamy wskaźnik na najmniejszy element.

Koszt $O(1)$

## insert(i, h)

Wykonujemy $meld(h, makeheap(i))$ (tworzymy jednoelementowy kopiec i dołączamy)

Koszt zależy od kosztu $meld$.

## deletemin(h)

Zależy od meld.

## meld

Są dwie metody realizacji $meld$:
1) "eager" - kopiec przybiera docelowy kształt przed wykonaniem następnej po
  $meld$ operacji;
2) "lazy" - kopiec może utracić strukturę kopca dwumianowego, zostanie mu ona
  przywrócona dopiero podczas wykonywania operacji $deletemin$.

### eager meld

W tej wersji drzewa kopca są dostępne przez tablicę wskaźników. Każdy kopiec
zawiera co najwyżej jedno drzewo każdego rzędu. $i$-ty wskaźnik wskazuje na 
drzewo $i$-tego rzędu.

$meld(h, h')$ tworzy nowy kopiec, stare ulegają likwidacji.

```
def eagermeld(h, h')
    if h.key < h'.key then MIN_H <- MIN_h else  MIN_H <- MIN_h'
    carry <- NIL
    for i <- 0 to maxheapsize
        k <- # wskaźników != NIL pośród {carry, h[i], h'[i]}
        case k of
            0: H[i] <- NIL
            1: H[i] <- niepusty wskaźnik z {carry, h[i], h'[i]}
            2: H[i] <- NIL; carry <- join(B1, B2)
                /* B1, B2 to dwa niepuste wskaźniki z {carry, h[i], h'[i]} */ 
            3: H[i] <- h[i]; carry <- join(h'[i], carry)
```

**Fakt 2** kopiec zawierający $n$ elementów składa się z co najwyżej $\log n$ 
różnych drzew wielomianowych.

Z tego faktu wynika, że koszt $eagermeld$ to $O(\log n)$.

#### deletemin

Wskaźnik MIN wskazuje na drzewo dwumianowe z najmniejszym korzeniem. W stałym
czasie usuwamy to drzewo z kopca, następnie usuwamy korzeń z tego drzewa, 
tworząc rodzinę drzew $B_0, \dots, B_{rząd(B)-1}$. Tworzymy z nich kopiec $h'$ i łączymy z 
poprzednim operacją meld.

Koszt $O(\log n)$.

#### insert 

Pojedyńcza operacja może kosztować $\Omega(\log n)$ gdy kopiec ma drzewa każdego
rzędu, ale można pokazać, że czas zamortyzowany można ograniczyć do $O(1)$.

### lazy meld

Chcemy, żeby wszystkie operacji oprócz $deletemin$ kosztowały $O(1)$ czasu
zamortyzowanego.

Teraz zamiast tablicy wskaźników drzewa dwumianowe kopca łączymy w cykliczną
listę dwukierunkową. $lazymeld(h, h')$ polega na połączeniu list i aktualizacji
wskaźnika MIN w czasie $O(1)$. Teraz kopiec może zawierać wiele drzew tego
samego rzędu. Dopiero $deletemin$ zredukuje liczbę drzew.

#### deletemin

- usuwamy korzeń $x$ drzewa wskazywanego przez MIN;
- dołączamy poddrzewa wierzchołka $x$ do listy drzew kopca;
- redukujemy liczbę drzew w kopcu.

W celu redukcji liczby drzew w kopcu wystarczy raz przeglądnąć listę drzew 
kopca. Pojedyńcza operacja $deletemin$ może być bardzo kosztowna, $O(n)$ gdy
kopiec składa się z $n$ drzew jednoelementowych. Pokażemy, że czas 
zamortyzowany można ograniczyć przez $O(\log n)$.

Utrzymujemy następujący niezmiennik kredytowy:
**Każde drzewo kopca ma 1 jednostkę kredytu na swoim koncie**

Operacjom przydzielamy następujące kredyty:
- $makeheap$ - $2$
- $insert$   - $2$
- $meld$     - $1$
- $findmin$  - $1$
- $deletemin$ - $2\log n$

Kredyty te symbolizują koszt, jaki płaci każda taka operacja. Wystarczają one
na realizację intrukcji niskiego poziomu i utrzymanie niezmiennika kredytowego:
- Operacje $meld$ i $findmin$ nie zmieniają liczby drzew w kopcach, wykonują
  się w stałym czasie.
- Operacje $insert$ i $makeheap$ wykonują się w stałym czasie, ale tworzą nowe
  drzewo. Jedna jednostka jest wydawana na wykonanie operacji niskiego poziomu,
  a druga jest dawana nowemu drzewu (żeby zachować niezmiennik).
- Operacja $deletemin$ może dodać co najwyżej $\log n$ nowych drzew do listy
  drzew kopca (jeśli usunie korzeń z największego drzewa z kopca). Z kredytu
  operacji $deletemin$ przekazujemy po jednej jednostce na konta tych drzew,
  czyli przed fazą redukcji każde drzewo ma jedną jednostkę na swoim koncie.


Podczas redukcji liczby drzew musimy przeglądnąć listę wszystkich drzew kopca
i dokonać pewnej liczby operacji $join$. Za każdą taką operację płacimy jedną
jednostką kredytu, która znajduje się na koncie przyłączonego drzewa (to nowe
drzewo ma swój jeden kredyt, z drzewa do którego robiliśmy przyłączanie). Tą
jednostką płacimy też za odwiedzenie tego drzewa w liście drzew.



