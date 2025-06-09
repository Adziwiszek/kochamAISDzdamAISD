# Warunki na drzewo czerwono-czarne

0) jest BST
1) każdy wierzchołek jest czerwony lub czarny
2) każdy liść jest czarny
3) jeśli wierzchołek jest czerwony, to obaj jego synowie są czarni
4) na każdej ścieżce prowadzącej z danego wierzchołka do liścia jest
  jednakowa liczba czarnych wierzchołków

Liśćmi są wierzchołki zewnętrzne odpowiadające NIL

**Definicja** Liczbę czarnych wierzchołków na ścieżce z wierzchołka x
(ale bez tego wierzchołka) do liścia nazywamy czarną wysokością x,
oznaczamy $bh(x)$.

**Fakt** BR Tree o n wierzchołkach wewnętrznych ma wysokość nie większą
niż $2\log(n+1)$

# Operacje słownikowe na drzewach czerwono-czarnych

Operacja wyszukiwania elementu nie dokonuje żadnych zmian w drzewie

## Wstawianie elementu

Jak w BST. Nowemu wierzchołkowi nadajemy kolor czerwony i przywracamy
drzewu własność drzewa BR.

Jedyną własnością, która może zostać zaburzona jest 3)

**Przywracanie 3)**

Własność 3 może być zaburzona tylko, gdy nowo dodany wierzchołek $x$
ma czerwonego ojca, tylko w tym miejscu gdzie dodano $x$.

(zakładamy, że ojciec $x$ jest lewym synem swojego ojca, w p.p. symetrycznie)

### Przypadek 1
Wujek $x$ jest czerwony.

- zmieniamy kolory
  - dziadka $x$ malujemy na czerwono (dotąd był czarny, bo ojciec
    $x$ był czerwony)
  - ojca i wujka $x$ malujemy na czarno
- x $\leftarrow$ $dziadek(x)$
- wywołujemy się rekurencyjnie dla $x$

### Przypadek 2
Wujek $x$ jest czarny i $x$ jest prawym synem.

- y $\leftarrow$ $ojciec(x)$
- $rotacja(x)$
- $x \leftarrow y$

W ten sposób otrzymujemy przypadek 3

### Przypadek 3
Wujek $x$ jest czarny i $x$ jest lewym synem.

- dziadka $x$ malujemy na czerwono
- ojca $x$ malujemy na czarno
- $rotacja(ojciec(x))$

## Usuwanie elementu
Jak w BST, usuwamy wierzchołek i przywracamy własności.

Chcemy usunąć $y$, $x$ jest jego następnikiem. Podstawiamy $x$ za $y$
(wartość, kolor zostaje bez zmian?), usuwamy $x$ (który ma co najwyżej jednego
syna.

Następuje problem, jeśli ten $x$ był czarny, bo może zostać zaburzona własność
4 drzewa (lub 3 jeśli syn $x$ był czerwony i ojciec $x$ jest czerwony). 
Wtedy czarny kolor przesuwamy na syna $x$ (który był jedynakiem albo liściem).
Ma on teraz czarny i super czarny kolor. Chcemy się pozbyć super czarnego.


### Przypadek 1
Brat $x$ jest czerwony (ojciec jest czarny)

- brata $x$ kolorujemy na czarno
- ojca $x$ kolorujemy na czerwono
- $rotacja(x)$


