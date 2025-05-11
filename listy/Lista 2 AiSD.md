# Zadanie 3

![[Pasted image 20250320133619.png]]

1) pokazać, że każdą kwotę da się wydać za pomocą Fibonacciego

# Zadanie 6

![[Pasted image 20250326111207.png]]

**Lemat 1**
Załóżmy, że mamy drzewo maksymalnie pokolorowane (n kolorowań) dla pewnego k. Po doczepieniu s wierzchołków (przynajmniej 1 dla każdego liścia) będzie pokolorowane dla $k' = k + 2$ przez $n + s$ wierzchołków (kolorujemy te nowe liście)

**D-d**
Po doczepieniu każda ścieżka liściowa zwiększyła swoją długość o 2 
(mogły się też pojawić nowe liście, ale wtedy jako starą ścieżkę liściową liczymy ścieżkę od ojców nowych liści).

Skoro $k' = k + 2$ to możemy pokolorować wszystkie nowe liście, nie przekroczymy
$k'$ bo najdłuższe ścieżki (ścieżki liściowe) nie przekraczają $k'$.

**ZNWP**, że to nie jest maksymalne kolorowanie. Wtedy moglibyśmy pokolorować 
jeszcze jeden wierzchołek, ale to nie mógłby być liść w $T'$. Zatem pokolorujmy 
jakiś inny wierzchołek wyżej. 

Ale teraz usuńmy nowo pokolorowane liście i wróćmy do starego $k$. 
Tylko, że tym razem w tym kolorowaniu mamy 1 dodatkowy wierzchołek, czyli 
dostajemy sprzeczność bo tamto stare kolorowanie było maksymalne dla tego $k$.

**Algorytm**

Przypadki bazowe:

- k = 1: możemy pokolorwać tylko 1 wierzchołek w drzewie

- k = 2: kolorujemy wszystkie liście (czemu to jest poprawne?)

Przypadek indukcyjny: (k > 2)

Zakładamy, że umiemy pokolorować drzewa o $x \leq n$ wierzchołkach dla pewnego $k$

Jeśli chcielibyśmy pokolorować drzewo dla $n + 1$ wierzchołków to odczepiamy wszystkie liście, zmniejszamy $k$ o 2 i kolorujemy 'indukcyjnie' nasze mniejsze drzewo.

Następnie przyczepiamy liście i zwiększamy $k$ o 2. Kolorujemy wszystkie liście.
Z **Lematu 1** to kolorowanie będzie maksymalne.

---

# Zadanie 7

![[Pasted image 20250326113142.png]]

## Lemat 1

$P(a,b)$, $P(a,c)$, $P(b,c)$ mają 1 wspólny wierzchołek $v$.

**D-d**

1) istnieje taki punkty wspólny, bo inaczej cykl
2) nie mogą mieć więcej, bo się cykle porobią
## Lemat 2

Dwa z trzech wierzchołków $a,b,c$ muszą być najbardziej oddalonymi wierzchołkami (krańcami średnicy).

**D-d**

Weźmy wierzchołki $a$, $b$, $c$, załóżmy, że dają maksymalnie dużo krawędzi.

Jeśli wśród nich nie ma żadnego krańca średnicy to BSO weźmy sobie $a$.
Z $a$ możemy pójść do najbardziej oddalonego wierzchołka od niego (znalezionego dfs-em) i dostać lepszy wynik. Zamieniamy $b$ lub $c$ z tym nowym najdalszym wierzchołkiem (jeżeli jest on w poddrzewie $v$, $b$ to zamieniamy go z $b$, analogicznie dla $c$). Powtarzamy tę procedurę jeszcze raz, tym razem biorąc ten nowy wierzchołek.

## Lemat 3

Niech $a$, $b$ są krańcami średnicy $T$. Najbardziej oddalony od $ab$ wierzchołek $c$ da maksymalny wynik. Czyli wynik nie zależy od wyboru średnicy.

**D-d**

Niech $(a,b,c)$ i $(x,y,z)$ to wierzchołki, $a,b,x,y$ to krańce dwóch średnic, $c$ jest najbardziej oddalonym wierzchołkiem od $ab$, $z$ analogicznie dla $xy$.

**ZNWP**, że $R(a,b,c) < R(x,y,z)$, gdzie $R$ to funkcja licząca wierzchołki jak w zadaniu.

Skoro $P(a,b)=P(x,y)$ to $P(c,ab) < P(z,xy)$

Z założeń mamy:
- $P(c,xy) \leq P(z,xy)$
- $P(x,ab),P(y,ab),P(z,ab) \leq P(c,ab)$, analogicznie dla $z$ i $xy$

Niech y_ab to kraniec $P(y, ab)$.
**BSO** niech $y$ i $b$ oraz $a$ i $x$ są obok siebie, niech $z$ łączy się z y_ab.

$P(a, x\_ab) = P(x, x\_ab)$ oraz  $P(b, y\_ab) = P(y, y\_ab)$, bo to średnice.

$P(y,ab) \leq P(c,ab) < P(z,xy)$, co daje nam sprzeczność, bo $xy$ to średnica, a wyszło nam, że $P(x,z) > P(x,y)$

x -> x_ab -> y_ab -> y
x -> x_ab -> y_ab -> z
## Algorytm

Znajdujemy dwa najbardziej oddalone wierzchołki dwoma dfsami. $O(n + m)$

odpalamy dfsa z jednego z wierzchołków średnicy i liczymy wierzchołki najbardziej oddalone od średnicy. Jak mamy krawędź $v \rightarrow u$ to jeśli oba są na średnicy to nic nie robimy a w p.p. $d[u] = d[v]+1$  

---
# Zadanie 8

![[Pasted image 20250328101531.png]]


1) możemy zamiast przekształcać pi w sigme to pi w identyczność
2) problem znalezienia minimalnego kosztu swapów jest równoważny 
