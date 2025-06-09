Drzewa samoorganizujące się

splay(x, S) - przeorganizuj S tak, by x znalazł się w korzeniu (jeśli $x \in S$)
jeśli x nie jest w drzewie S to w korzeniu ma się znaleźć $y \in S$ taki, że
- y jest największym mniejszym od x, lub
- y jest najmniejszym większym od x

Interesujące nas operacje
- insert
- delete
- find
- join($S_1, S_2$) - łączenie drzew w jedno (przy założeniu, że $\forall klucz\;k\in S_1,\;klucz\;k'\in S_2 \;\; k < k'$
- split (S,x) - wynik to dwa drzewa $S_1, S_2$, $S_1$ ma klucze mniejsze od $x$, a $S_2$ większe równe

**Spostrzeżenie**
Każdą z tych operacji da się zrealizować poprzez wykonanie stałej liczby 
operacji splay i stałej liczby operacji niskiego rzędu.

delete(x)

skupimy się na analizie splay, zobaczymy ile kosztuje nas ciąg splay-ów

# jak realizować splay(x, S)?

## Naiwnie 

TODO: dodać rysunek

Realizujemy to rotacjami(x) aż dojdziemy do korzenia.
Zły pomysł.
Weźmy drzewo będące ścieżką prostą z $n$ do $1$. Chcemy wykonać ciąg 
$splay(1), splay(2),...,splay(n)$.
splay(1) i splay(2) kosztują n-1 rotacji. Następne rotacje kosztują n-2, n-3,...
suma tych rotacji to $\Omega(n^2)$. Po wszystkich rotacjach wrócimy do oryginalnego
drzewa, ścieżki od $n$ do $1$.

![[Pasted image 20250523065738.png]]
## Lepiej

Rozważamy 3 przypadki:
1) x nie ma dziadka (leży pod korzeniem) -> rotacja(x)
2) w p.p. x jest lewym (prawym) synem ojca, ojciec też jest lewym (prawym) synem -> rotacja(y), rotacja(x)
3) x jest lewym synem, ojciec jest prawym synem LUB x jest prawym synem, ojciec jest lewym synem -> rotacja(x), rotacja(x)

![[Pasted image 20250523065721.png]]

**Intuicja**
Podczas przenoszenia tak jak w naiwnym przykładzie (splay(1)) skraca nam się 
o połowę wysokość drzewa.

**Analiza kosztu splay**
$\mu(x)$ - koszt wierzchołka $x$, 

**Niezmiennik:**
Chcemy, żeby po każdej operacji było $\mu(x)=log(\#$wierzchołków w drzewie o korzeniu $x)$

**Fakt** Operacja splay(x) potrzebuje $3\cdot (log\;n - \mu(x)) + 1$ jednostek.

Oznaczenia:
$\mu(x)$ - wartość konta x przed rotacjami
$\mu'(x)$ - wartość konta x po rotacjach

**Przypadek 1**

przy rotacjach x, y zmieniają się tylko konta x i y
Trzeba dodać troche jednostek, żeby zachować ten niezmiennik

Spostrzeżenie:
$\mu'(x)=\mu(y)$

Musimy uzupełnić tę różnicę poniżej (dosypać kredytów)
$(*) = \mu'(x)+\mu'(y) - \mu(x) - \mu(y)$

na tym etapie mamy do dyspozycji $3(\mu(y) - \mu(x))$ jednostek

ponieważ $\mu'(y) \leq \mu'(x)$, to $(*) \leq \mu'(x) - \mu(x)$

płacimy za $(*)$ z naszych jednostek
pozostanie nam $2(\mu(y) - \mu(x))$ jednostek

problem, gdy $\mu'(x) = \mu(x)$. Wówczas wykorzystujemy tę jedną dodatkową jednostkę

Wykonujemy jeszcze jakieś fizyczne rotacje, je opłacimy za pomocą pozostałych 
jednostek.

**Przypadek 2**
tylko 3 wierzchołki, x, y, z, zmieniają ilość wierzchołków w swoich poddrzewach
$(*) = \mu'(x) +\mu'(y) +\mu'(z) - \mu(x) - \mu(y) - \mu(z)$
fakt: $\mu'(x) = \mu(z)$
$(*) = \mu'(y) +\mu'(z) - \mu(x) - \mu(y)$
fakt: $\mu'(z) \leq \mu'(y) \leq \mu'(x)$
$(*) \leq 2\mu'(x) + 2\mu(x) = 2(\mu'(x) - \mu(x))$

jedna różnica pozostaje nam na opłacenie operacji niskiego rzędu.
Problem, gdy $\mu'(x) =\mu(x)$

**Fakt**


