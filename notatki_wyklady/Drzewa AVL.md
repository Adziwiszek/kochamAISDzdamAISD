# Definicja

BST jest drzewem AVL, jeśli dla każdego wierzchołka wysokość jego lewego i
prawego poddrzewa różnią się o co najwyżej 1.

# Zasadnicza cecha

## Twierdzenie 1

Wysokość drzewa AVL o $n$ wierzchołkach jest mniejsza niż $1.4405\;log(n+2)$.

**Fakt 1** Liczba wierzchołków w dowolnym drzewie binarnym jest o 1 mniejsza od
liczby pustych wskaźników (tj. równych NULL/NIL).

**Dowód twierdzenia 1**

Niech $\rho(i) =$ liczba wierzchołków w minimalnym (wielkościowo) drzewie AVL 
o wysokości $i$.

Indukcyjnie po wysokości drzewa $h$ dowodzimy, żr $\rho(h) = F_{h+2}$ (liczba 
Fibonacciego).

$\rho(1) = 2$, $\rho(2) = 3$

Dla $h>2$:
Niech $T$ będzie minimalnym drzewem AVL o  $h \geq 3$. Z minimalności $T$ wiemy,
że jedno z poddrzew podwieszonych pod jego korzeniem musi być minimalnym 
drzewem AVL o wysokości $h-1$, a drugie o minimalnym drzewem AVL 
o wysokości $h-2$. Każdy pusty wskaźnik $T$ jest pustym wskaźnikiem w jednym z 
tych poddrzew, więc:
$$
\rho(h) = \rho(h-1) + \rho(h-2)
$$

TODO: przekształcenia

# Operacje słownikowe na drzewach AVL

Wyszukiwanie elementu odbywa się tak jak dla BST.

## Rotacje

**Własności**
- rotacje nie zmieniają porządku infiksowego elementów
- pojedyńczą rotację można wykonać w czasie stałym

## Wstawianie elementu

Niech $M$ będzie pierwszym wierzchołkiem na drodze od wstawionego elementu do
korzenia, w którym nastąpiło naruszenie równowagi AVL. Oznacza to, że przed 
operacją wstawienia poddrzewa $M$ były różnej wysokości i operacja dodania 
zwiększyła wysokość wyższego poddrzewa.

Załóżmy, że tym poddrzewem jest lewe poddrzewo (analogicznie dla prawego) i 
oznaczmy, jego korzeń jako $L$.

Procedura balansowania rozważa dwa przypadki:
1) w drzewie o korzeniu $L$ zwiększyła się wysokość lewego poddrzewa.
2) w drzewie o korzeniu $L$ zwiększyła się wysokość prawego poddrzewa.

**Przypadek 1**
![[Pasted image 20250522174648.png]]

**Przypadek 2**
![[Pasted image 20250522174729.png]]

Po zbalansowaniu wysokość drzewa zakorzenionego w $L$ (w przypadku 1) oraz $M$
(w przypadku 2) jest równa wysokości drzewa zakorzenionego w $M$ przed operacją
wstawienia. Dlatego nie trzeba balansować $T$ w innych węzłach.

## Usuwanie elementu

TODO

# Zastosowanie drzew zbalanasowanych do implementacji list
