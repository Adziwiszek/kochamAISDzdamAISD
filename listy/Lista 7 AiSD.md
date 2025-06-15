# Zadanie 1

#TODO treść

Niech $\sigma$ składa się z $u$ operacji `union` oraz $f$ operacji `find`

Po wykonaniu wszystkich operacji `union` struktura składać się będzie z lasu drzew. W korzeniu każdego drzewa znajdować się będzie etykieta grupy.
`union` wykonuje się w czasie stałym, więc łączny czas będzie proporcjonalny do $u$.

**Obserwacja:**
Każda operacja `union` tworzy dokładnie jedną nową krawędź (łączącą korzenie drzew odpowiadających podzbiorom).

**Lemat 1:**
Każdą krawędź nie połączoną z korzeniem drzewa przejdziemy tylko raz.
**d-d:**
Jeżeli przejdziemy przez krawędź, to wykonujemy operację `find`.
W drugiej części operacji `find` usuniemy tą krawędź i połączymy wierzchołek początkowo bezpośrednio z korzeniem.

**Obserwacja:**
Dla każdej operacji find przejdziemy dokładnie jedną krawędź prowadzącą do korzenia.

### Oszacowanie Ilości Operacji

- $\Theta(u)$ – operacji z funkcji `union`
- $\Theta(f)$ – przejścia do korzenia
- $\Theta(u)$ – przejścia i usuwanie krawędzi

> Ładniej analizą zamortyzowaną

# Zadanie 2

#TODO treść

Kluczowym faktem jest tutaj występowanie tylko jednej instrukcji `insert(i)` dla każdego $i$. To pozwoli nam na użycie efektywnych struktur dla zbiorów.

Sekwencję $\sigma$ możemy zapisać jako:
$$
\sigma_{1}D\sigma_{2}\dots D\sigma_{k+1}
$$
Gdzie $D$ oznacza operację `DeleteMin`.

### Dodatkowa Operacja UnionFind

- `*.insert(el, tag)` – wstawia `el` do zbioru identyfikowanego przez `tag`

Potrzebować będziemy dwóch struktur [[Union Find]]:

- `buckets` – Pozwala sprawdzić do którego kubełka należy dany element
- `bounds` – Ograniczenie od góry na wartość elementu z operacji `Min(i)`

Oraz globalnej tablicy `boundVal[1.2n]` która będzie mapować klucze `bound` na faktyczne maksymalne wartości.

### Sekwencje

#### Pomiędzy DeleteMin

Dla $j$-tego przedziału operacji `insert(i)` oraz `Min(i)` znajdującego się w $\sigma_{j}$ operacją `DeleteMin` wyznaczamy

- $p_{j}$ – zbiór kandydatów na $j$-ty `DeleteMin`
- $m_{j}$ – minimalną wartość występującą w `Min(i)`

```
// l i r to ograniczenia na przedział, który badamy
def process_range(inst[n], l, r, j):
	m = inf
	for i in r..l:
		match inst[i] begin
			Min(m') => m = min(m, m'),
			Insert(i) => if i < m then
				bounds::insert(i, j)
				buckets::insert(i, j)
		end

	boundVal[n + j] = m
	boundVal[j] = inf
	return LinkedList{
		{ tag = n + j },
		{ tag = j }
	}
```

Na podstawie tych wartości wyznaczamy tablicę dwustronnych linked list $ll$ zawierającą w każdym swoim elemencie:

1) Tag zbioru union-find z `bound` grupujący wartości według ograniczenia na maksymalny element
2) Tag zbioru union find ze wszystkimi elementami w 'grupie'

Początkowo dla każdego zbioru niech linked list zawiera jako pierwszy element tag na pusty kubełek, który posiada `boundVal` równy

```
def preprocess(inst[n]):
	l = 1

	ll[]
	for i in 1..n:
		if inst[i] == DeleteMin:
			ll.push(process_range(l, r))
			l = i+1
	
	ll.push(process_range(l, n)) // być może puste, ale trudno!
	return ll
```

### Wyniki Dla Operacji DeleteMin

Wynik $i$-tego zapytania przechowamy w $i$-tym elemencie tablicy `ans`.

```
def findAns(ll[k+1], n):
	LinkedList links{1, 2, ..., k+1}
	linkInx[k+1] = 'wskaźnik na i-ty element linked list'
	ans[k+1]

	for i in 1..n:
		bucket = buckets.find(i)
		bound = boundVal[bounds.find(i)]
		
		// Jeżeli aktualny element będzie wyrzucony przez minimum to idź dalej
		if i >= bound:
			continue
		
		ans[bucket] = i
		
		// Znaleziono, więc trzeba kandydatów na 'ten' deleteMin dołączyć do następnego
		nextBucket = linkInx[bucket].next
		LinkedList::removeNode(linkInx[bucket])
		
		buckets.join(bucket, nextBucket, nextBucket)
		concatMonotonic(ll[bucket], ll[nextBucket])


def concatMonotonic(ll, lr):
	l = ll.end
	r = lr.start
	
	while l != NULL && boundVal[l.tag] >= boundVal[r.tag]:
		bounds.join(l.tag, r.tag, r.tag)
		l = l.prev

	if l != NULL:
		l.next = r
		r.prev = l
```

### Poprawność

**Twierdzenie:**
`buckets` zawsze poprawnie wyznacza dla której z kolei operacji `MinDelete` kandydatem jest dany element
**d-d**:
Jest tak na początku (oczywiste) oraz po znalezieniu odpowiedzi na $j$-te zapytanie wszystkie elementy kandydujące teraz przeniesiemy do kandydatury na następny możliwy

**Twierdzenie:**
`bounds` przechowuje dla każdego elementu poprawne ograniczenia.
**d-d:**
Jest tak na początku (oczywiste). Znany następują, gdy chcemy by wcześniejsze elementy mogły kandydować na dalsze pozycje. Wtedy oczywiście wartości elementów ograniczone zostaną przez najmniejsze `i` dla którego występuje operacja `Min(i)` przed następnym celem.

**Twierdzenie:**
Wybieramy poprawny element dla `DeleteMin`.
**d-d:**
Jeżeli `buckets` i `bounds` są poprawne, to przeglądając elementy od najmniejszego i wybierając pierwszy możliwy faktycznie wybierzemy minimum.

### Złożoność Czasowa

W najgorszym wypadku w strukturze union-find będziemy mieć $n$ elementów, więc to daje nam ograniczenie $O(n\log^{*}n)$.
Wszystkie inne operacje są liniowe.

> Można to zrobić jedną strukturą union-find

# Zadanie 3

#TODO treść

**Obserwacja:**
Po operacji `link(r, v)` wysokości elementów mogą ulec zmianie tylko jeżeli korzeń drzewa którego elementem jest `v` zostanie podpięty do innego drzewa.
**Wniosek:**
Można (a nawet trzeba) podpiąć drzewo `r` do korzenia drzewa zawierającego `v`.

### Link

```
Element[n]
h[n]
h_cost[n]
size[n]

def link(r, v):
	rr = find(r)
	vr = find(v)
	
	if size[vr] >= size[rr]:
		size[vr] += size[rr]
		h_cost[rr] += h[v] + 1 - h_cost[vr]
		Element[rr]->parent = Element[vr]
	else:
		size[rr] += size[vr]
		h_cost[rr] += h[v] + 1
		heigth[vr] -= h_cost[rr]
		Element[vr]->parent = Element[rr]


def find(v):
	root = NULL
	l = []
	curr = Element[v]
	while curr != curr.parent:
		l.push(curr)
		curr = curr.parent
	
	root = curr
	root_cost = h_cost[root.id]
	sum = root_cost
	h[root.id] = sum
	
	for el in l.reverse():
		sum += heigth[el.id]
		h_cost[el.id] = sum - root_cost
		h[el.id] = sum
		el.parent = root

def depth(v):
	find(v)
	return h[v]
```

### Złożoność Obliczeniowa

Taka sama jak standardowego problemu union-find.
Jedyną różnicą jest utrzymywanie dodatkowej tablicy, gdzie każda operacja zajmuje stały dodatkowy czas.

### Poprawność

Wynika z utrzymywanie przez wszystkie operacje niezmiennika:
$$
\sum\limits_{u\in\text{path(v,r)}}\text{h\_cost}[u] = \text{h}[v]
$$
# Zadanie 4

#TODO

# Zadanie 5

#TODO treść

Ważny jest tutaj fakt, że krawędzie grafu tworzą sekwencję. Będziemy więc mogli przeprowadzić działania w pewnym sensie odwrotne do [[Algorytm Kruskala|algorytmu Kruskala]].

### Algorytm

Niech początkowo każdy wierzchołek jest zawarty jako singleton w strukturze [[Union Find]] dostępny za pomocą swojego indeksu.
Dodatkowo przydadzą się następujące struktury:

- `Optional< int > connected[]` – dodanie jakiej krawędzi spowodowało podłączanie tego zbioru do $v$. Jeżeli puste, to zbiór nadal nie podłączony.
	- Początkowo `connected[v] = None`

Dalej będziemy chcieli wykonać następujące przetwarzanie:
```
def solve(e[1..m]):
	for i in m..1 {
		(v, u) = e[i]
		v = find(v), u = find(u)
		match connected[v], connected[u] {
			None, None -> union(v, u),
			Some(_), None -> connected[u] = Some(i),
			None, Some(_) -> ...
			Some(_), Some(_) -> NOP
		}
	}

def query(v):
	connected[find(v)]
```

### Złożoność Czasowa

Korzystamy ze struktury union find dla $n$ elementów oraz wykonujemy na niej $m$ operacji, stąd czas działania wynosi: $O(m\log^{*}n)$.