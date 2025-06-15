# Zadanie 1

#TODO treść

Chcemy tak dobrać wysokości $h_{i}$ poszczególnych elementów w słowniku, by czas wykonywania operacji na słowniku był jak najmniejszy – minimalizujemy sumę:
$$
COST = \sum\limits_{i=1}^{n}h_{i}p_{i}
$$
Zauważmy, że problem możemy łatwo redukować do pod problemów – jeżeli zgadniemy korzeń drzewa, to wystarczy wyznaczyć optymalne drzewo dla elementów po lewej stronie oraz dla elementów po prawej stronie.
Pozwala to więc na zdefiniowanie następującej reguły programowania dynamicznego:
$$
\begin{align*}
p[i][j] &=  \sum\limits_{k=i}^{j}p_{k}\\
dp[i][j] &=\min_{k\in\{i, \dots, j\}}(dp[i][k-1] + p[i][j] + dp[k+1][j])
\end{align*}
$$
> `dp[i][j] = minimalny koszt drzewa z wierzchołkami z przedziału [i, j]`. 

Mamy $n^{2}$ wartości do wyliczenia oraz wyliczenie jednej wartości kosztuje nas czas liniowy, więc całkowita złożoność to $O(n^{3})$.

Zachodzi tutaj [[Optymalizacja Knutha]] co pozwala zejść ze złożonością do $O(n^{2})$.

# Zadanie 2

#TODO treść


Zaczniemy od pomieszania wszystkich punktów.
Następnie wyznaczamy odległość $d$ pomiędzy dwoma punktami i tworzymy na ich podstawie kubełki o wielkości $\frac{d}{2}$.

Teraz sprawdzając kolejny punkt, jeżeli trafiłby do już zajętego kubełka, to należy ponownie przydzielić kubełki punktom (kubełki już krótszej długości).
Pomimo dużego kosztu ponownego przydzielania kubełków algorytm nie zrobi się kwadratowy, ponieważ oczekujemy, że takie ponowne przydzielanie wartości jest bardzo mało prawdopodobne.

Na koniec trzeba będzie sprawdzić dla każdego punktu jego sąsiednie kwadraty, bo mogą być elementy pomiędzy nimi elementy bliższe, ale jeżeli w każdym kwadracie jest co najwyżej jeden punkt, to zajmie to nam również liniowo wiele czasów (bo sprawdzamy tylko co najwyżej drugich sąsiadów).

### Analiza Złożoności

Niech $\langle d_{1},d_{2},\dots, d_{i}\rangle$ wyznacza rozwiązanie dla zbioru $\langle p_{1},p_{2},\dots,p_{i}\rangle$.
Ponowne grupowanie elementów należy wykonać wtedy, gdy $d_{i} < d_{i-1}$. Niech zdarzenie 'trzeba grupować ponownie po dodaniu punktu $i$' opisuje zero-jedynkowa zmienna $X_{i}$.

Wtedy łączny oczekiwany koszt ponownego grupowania wynosić będzie:
$$
\begin{align*}
E\left( \sum\limits_{i=1}^{n}X_{i} \right) &= \sum\limits_{i=1}^{n}E(X_{i}) \\
&=\sum\limits_{i=1}^{n}P(X_{i} = 1) \cdot i
\end{align*}
$$
Prawdopodobieństwo, że spośród $i$ punktów, $p_{i}$ jest w parze najkrótszych punktów wynosi:
$$
P(X_{i} = 1) = \frac{n-1}{\binom{n}{2}} = \frac{n-1}{\frac{n(n-1)}{2}} = \frac{2}{n}
$$
Stąd potrafimy policzyć oryginalną sumę:
$$
\begin{align*}
E\left( \sum\limits_{i=1}^{n}X_{i} \right) = \sum\limits_{i=1}^{n}P(X_{i} = 1) \cdot i &= \sum\limits_{i=1}^{n} \frac{2}{n}\cdot i \\
&=  \frac{2}{n}\cdot \sum\limits_{i=1}^{n}i \\
&= \frac{2}{n} O(n^{2}) \\
&= O(n)
\end{align*}
$$
Stąd oczekujemy, że ponowne haszowanie będzie nas kosztować liniowo wiele względem $n$.

# Zadanie 3

#TODO treść


Założymy najpierw, że mamy dostępną dobrą funkcję haszującą rozmieszczającą wszystkie elementy równomiernie – elementy mają prawdopodobieństwo $\frac{1}{m}$ trafienia do każdej listy.
Przy takich założeniach będziemy również mieć dobrą funkcję haszującą.

No to teraz rozmieszczamy $n$ elementów na $m$ kubełków.
Kubełek jest pusty jeżeli żaden z $n$ elementów don niego nie trafił. Zdefiniujmy zero-jedynkową zmienną losową $X_{i}$ będącą $1$ jeżeli kubełek jest pusty. Mamy wtedy:
$$
P(X_{i} = 1) = \left( 1 - \frac{1}{m} \right)^{n}
$$
No to teraz oczekiwana liczba pustych kubełków będzie wyrażalna następująco:
$$
E\left( \sum\limits_{i=1}^{m}X_{i} \right) = \sum\limits_{i=1}^{m}E(X_{i}) = m\left( 1 - \frac{1}{m} \right)^{n}
$$

# Zadanie 4

#TODO 

# Zadanie 5

#TODO 

# Zadanie 6

#TODO 
