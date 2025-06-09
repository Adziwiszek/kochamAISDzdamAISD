# Problem MinMax

Mamy problem jednoczesnego znalezienia minimum i maximum w zbiorze $S$.

## **Twierdzenie** 
Algorytm rozwiązujący powyższy problem (robiący tylko porównania
w zbiorze $S$) musi wykonać przynajmniej $\lceil \frac{3}{2}n - 2 \rceil$ porównań.

**D-d**
Rozważamy grę pomiędzy algorytmem a adwersarzem. Algorytm chce wskazać 
minimalny i maksymalny element w $S$ w mniej niż $\lceil \frac{3}{2}n - 2 \rceil$ porównań.
Adwersarz chce pokazać, że potrzeba do tego przynajmniej tyle porównań.

**Algorytm nie zna zbioru $S$, wie tylko, że ma on $n$ elementów.**

Algorytm pyta o porównanie dwóch elementów z $S$, a adwersarz odpowiada na to 
pytanie. **Po tym algorytm nie zna wartości dwóch elementów z $S$, wie tylko w 
jakiej są relacji.**

## **Strategia dla adwersarza**
W trakcie gry adwersarz dzieli $S$ na 4 rozłączne podzbiory:

$A = \{i\: |\: a_i$ nie był jeszcze porównywany $\}$
$B = \{i\: |\: a_i$ wygrał już jakieś porównanie i nie przegrał żadnego $\}$
$C = \{i\: |\: a_i$ przegrał już jakieś porównanie i nie wygrał żadnego $\}$
$D = \{i\: |\: a_i$ wygrał już jakieś porównanie i jakieś już przegrał $\}$

Początkowo $|A|=n$, $|B|=|C|=|D|=0$.

Adwersarz rozpoczyna grę z kandydatami na wartości elementów $a_i$. W trakcie
rozgrywki adwersarz będzie modyfikował $a_i$ w ramach potrzeby tak, żeby 
spełniały warunek:
$$
(*) \:\:\:\:\:\:\: 
\forall a \in A\:\:\forall b \in B\:\: \forall c \in C\:\: \forall d \in D
\:\:\:\: b > d > c \wedge b > a > c
$$

Wystarczy do tego zwiększać elementy z $B$ i zmniejszać te z $C$.
Pozostawia to prawdziwe dotychczasowe odpowiedzi adwersarza.

## **Lemat** Strategia adwersarza jest zawsze wygrywająca

**Dowód lematu**
W trakcie gry elementy przechodzą ze zbioru $A$ do $B$ lub $C$, a następnie 
dopiero do $D$.

Dla danych spełniających $(*)$
- **jedno porównanie może usunąć co najwyżej dwa elementy z $A$.** Skoro do tej 
  pory dwa elementy nie były porównywane to po porównaniu jeden trafi do $B$, 
  drugi do $C$. Jeżeli w porównaniu bierze udział tylko jeden element z $A$ to
  w oczywisty sposób jest to prawda.
- **dodanie jednego elementu do zbioru $D$ wymaga jednego porównania.** Do $D$ mogą
  trafić tylko elementy z $B$ lub z $C$. Jeśli porównamy między sobą jakieś dwa
  elementy z $B$ lub $C$ każdy to mamy 2 możliwości:
    - są z tego samego zbioru. Wtedy jeden z nich po porównaniu pozostanie w 
      tym zbiorze, drugi trafi do $D$ (Np. jeśli są z $B$ to ten co wygra nadal
      będzie niezwyciężony, więc zostanie w $B$, przegrany trafi do $D$).
    - jeśli są z różnych to argument jest podobny jak powyżej.
- **porównania, w których udział bierze element z $A$ nie zwiększają mocy $D$.** Z
  założenia $(*)$ wszystkie elementy z $A$ są mniejsze od tych z $B$ i większe 
  od tych z $C$. Dlatego porównując $a \in A$ z jakimś elementem z $B$ lub $C$
  wiemy, że ten drugi element pozostanie w swoim zbiorze (czyli nie spadnie do $D$).

Dopóki $A$ jest niepusty i któryś ze zbiorów $B$ lub $C$ zawiera więcej niż jeden
element to algorytm nie może udzielić poprawnej odpowiedzi.

Na opróżnienie $A$ potrzeba $\lceil \frac{n}{2} \rceil$ porównań.

Następnie potrzeba $n-2$ porównań na przesłanie wszystkich, poza dwoma, 
elementów do zbioru $D$.

To kończy dowód lematu i twierdzenia.
