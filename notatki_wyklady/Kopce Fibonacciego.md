# Struktura kopców Fibonacciego

Jak kopce dwumianowe, są zbiorem drzew, które pamiętają wierzchołki w porządku
kopcowym. Teraz drzewa nie muszą być drzewami dwumianowymi (każdy wierzchołek
może stracić jednego syna).

Jak kopce dwumianowe w wersji lazy.

# Operacje

Operacje $makeheap$, $insert$, $findmin$, $meld$ są takie same jak na kopcach
dwumianowych.

## cut(h, p)

Operacja ta odcina $p$ od jego ojca $p'$ i dołącza operacją $meld$ poddrzewo
zakorzenione w $p$ do listy drzew kopca. Jeśli $p$ jest pierwszym synem utraconym
przez $p'$ to odnotowujemy ten fakt. W przeciwnym wypadku robimy $cut(h, p')$.

W ten sposób odcinamy wierzchołki, aż natrafimy na taki, który nie stracił 
jeszcze syna.

## decrement(h, p, val)

Zmniejszamy wartośc klucza w wierzchołku $p$. Jeśli nowa wartość psuje porządek
kopcowy (tzn. wartość $p$ jest mniejsza od jego ojca) to robimy $cut(h,p)$.

### Zamortyzowany koszt

Każdy wierzchołek ma swoje konto. Jest ono niepuste tylko u wierzchołków, które
utraciły jednego syna.

Operacji $decrement$ przydzielamy 4 jednostki kredytu. Jedną jednostką opłacamy
koszt operacji niskiego poziomu i operację $meld$ przyłączenia drzewa o korzeniu
$p$ do kopca. Drugą umieszczamy na tym nowym drzewie (nadal jest niezmiennik, że
każde drzewo ma jednostkę na swoim koncie).

Pozostałe dwie jednostki wykorzystujemy wtedy, gdy wykonamy $cut(h, p)$ i $p$ 
jest pierwszym synem odciętym od swojego ojca. Dajemy je wówczas na konto ojca
$p$, będą one wykorzystane, gdy $p'$ utraci drugiego syna i będziemy musieli 
odciąć go od drzewa (opłacimy wówczas nimi operacje $cut$).

## deletemin(h)

Analogicznie jak w kopcach dwumianowych. Podczas redukcji łączymy drzewa o 
jednakowym rzędzie (zdefiniowanym jako liczba synów korzenia), otrzymując 
drzewo o rzędzie o jeden wyższym.

Teraz jednak drzewa nie są dwumianowe i nie można oczekiwać, że łączone drzewa
będą identyczne.

Aby wykazać, że $O(\log n)$ jest nadal ograniczeniem tej operacji musimy dowieść,
że stopień wierzchołków drzew występujących w kopcach Fibonacciego jest 
ograniczony przez $O(\log n)$. To będzie także ograniczenie na liczbę różnych
rzędów drzew.

**Lemat 1**
Dla każdego wierzchołka $x$ kopca Fibonacciego o rzędzie $k$, drzewo zakorzenione
w $x$ ma rozmiar wykładniczy względem $k$.

**D-d**
Niech $x$ będzie dowolnym wierzchołkeim kopca i niech $y_1, y_2, \dots, y_k$
będą jego synami uporządkowanymi w kolejności przyłączania ich do $x$. 

W momencie przyłączania $y_i$ do $x$-a, $x$ miał co najmniej $i-1$ synów.
$y_i$ też miał co najmniej $i-1$ synów, bo łączymy drzewa o tym samym rzędzie.

Od tego momentu $y_i$ mógł stracić co najwyżej jednego syna (bo inacej zostałby
odcięty od $x$-a). Czyli w każdym momencie $i$-ty syn każdego wierzchołka ma
rząd co najmniej $i-2$.

Niech $F_i$ to najmniejsze drzewo o rzędzie $i$ spełniające powyższą zależność.
$F_0$ jest drzewem jednowierzchołkowym, a $F_i$ składa się z korzenia oraz $i$
poddrzew: $F_0, F_1, F_2, \dots, F_{i-2}$. 

Liczba wierzchołków $|F_i|$ jest nie mniejsza niż $1 + \sum_{j=0}^{i-2} |F_i|$.
Indukcyjnie pokazujemy, że jest to równe $i$-tej liczbie Fibonacciego.
Stąd liczba wierzchołków w drzewie o rzędzie $k$ jest nie mniejsza niż $\phi^k$,
gdzie $\phi = \frac{1 + \sqrt{5}}{2}$.

**Wniosek 2**
Każdy wierzchołek w n-elementowym kopcu Fibonacciego ma stopień ograniczony
przez $O(\log n)$.

## delete(h, p)

Operację $delete(h, p)$ można wykonać poprzez $decrement(h, p, -\infty)$, a 
następnie $deletemn(h)$. Zamortyzowany koszt to $O(\log n)$.

**Uwaga**
W ten sam sposób możemy wykonywać delete na kopcach dwumianowych. Wówczas
decrement musi polegać na przesunięciu zmniejszonego elementu do korzenia
drzewa (w kopcu Fibonacciego zamiast tego $cut$ odwala za nas robotę).
