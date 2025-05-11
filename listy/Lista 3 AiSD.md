
# Zadanie 3

![[Pasted image 20250404110655.png]]

złożoność dzielenia (łączna) $rlogn$, bo każdy przedział $(p, k)\in S$ pojawia się w maksymalnie $logn$ przedziałach

złożoność czasowa całego 
$T(n)=2T(\frac{n}{2}) + \theta(n)$


---

# Zadanie 4
![[Pasted image 20250408125756.png]]

**Algorytm**
```
posortuj proste po współczynniku kierunkowym a, pozbywamy się równoległych
stack = [] 
for l in proste:
	if len(stack) == 0:
		stack.push((l, None))
	if len(stack) == 1:
		# cross oblicza punkt przecięcia dwóch prostych
		stack.push((l, cross(l, stack.top())))
	for l in proste:
		(k, x) = stack.top()
		# usuwamy proste ze stosu, które są przesłaniane przez l
		while k(x) < l(x): 
			stack.pop()
			(k, x) = stack.top()
		stack.push(l, cross(l, k))
```
Złożoność tego algorytmu (bez sortowania) to $O(n)$ czasowa (bo każdy element może być "rozważany" tylko dwa razy, raz przy dodawaniu na stos i raz przy usuwaniu)
Pamięciowa $O(n)$

ostatecznie czasowa to $O(nlogn)$ 

**Lemat**
mamy stos z prostymi stworzony przez algorytm i prostą l.
niech k to prosta z góry stosu, $x_0$ to punkt przecięcia k z drugą z góry prostą ze stosu.
jeśli l(x) > k(x) to l przesłania prostą k. 
(fakt, że są posortowane po 'a' pomaga)

Jak mamy ten lemat to w widać, że usuwamy tylko przesłonięte proste.
Jakiś dowód z niezmiennikiem, że w każdym kroku pętli mamy na stosie tylko widoczne proste z tych rozważanych do tej pory.

---
# Zadanie 5

![[Pasted image 20250413144220.png]]

## k = 2

$x = a \cdot 2^m + b$, gdzie $a$ i $b$ to połowy liczby $x$
$$x^2=(a\cdot 2^m+b)^2=a^2\cdot2^{2m}+2ab\cdot2^m+b^2$$
$2ab = (a + b)^2 - a^2 - b^2$

Czyli musimy rekurencyjnie obliczyć:
- $a^2$
- $b^2$
- $(a+b)^2$

$T(n)=3T(\frac{n}{2}) + n$
$T(n)=\Theta(n^{log_{2}3})$, czyli otrzymaliśmy taką samą złożoność jak algorytm karatsuby dla $k=2$

## k = 3

$x= a \cdot 2^{2m} + b \cdot 2^m + c$
$$x^2 = a^2\cdot2^{4m} + 2ab\cdot2^{3m}+(b^2+2ac)\cdot2^{2m} + 2bc\cdot2^m+c^2$$

## nie da się asymptotycznie szybciej kwadracić niż mnożyć

$(a+b)^2 = a^2 + 2ab + b^2$

$a\cdot b = \frac{(a+b)^2 - a^2 - b^2}{2}$ 

możemy mnożyć kwadracić, więc gdybyśmy mogli szybciej kwadracić to moglibyśmy szybciej mnożyć.


---

# Zadanie 6

---
# Zadanie 7

![[Pasted image 20250414164338.png]]

Rozwiązuję zadanie b.

- $e[\:]$ - lista sąsiedztwa drzewa
- $size[\:]$ - tablica z wielkościami poddrzew zakorzenionych w danym wierzchołku

```
fun get_size(v, p=-1):
	size[v] = 1
	for i in e[v]:
		if i == p: continue
		size[v] += get_size(i, v)
	return size[v]
```

```
fun get_centroid(v, p=-1):
	for i in e[v]:
		if i == p: continue
		if size[i] * 2 > n:
			return get_centroid(i, v)
	return v
```

Korzystamy z tych dwóch funkcji w taki sposób:
```
get_size(0)
centroid = get_centroid(0)
to_check[centroid] = true # nasza granica dla poddrzewa
```

**Lemat**
Funkcja get_size i get_centroid zwraca centroid w drzewie w $O(n)$, niezależnie od tego gdzie zaczniemy.

Następnie wywołujemy się rekurencyjnie dla każdego centroidu:
1) tab[]
2) puszczamy dfs-a szukającego odległość wierzchołków od centroidu
3) count()

```
def count(centroid):
	for i in e[centroid]:
		find_paths(i, centroid)
		add_subtree(i, centroid)
	zero_tab()
```

find_paths() zlicza ile jest ścieżek pomiędzy poddrzewami centroidu oddalonymi o C

add_subtree() uzupełnia tab o wierzchołki z poddrzewa i

---

# Zadanie 8

![[Pasted image 20250414113609.png]]

Podczas scalania:
```python
def merge_and_count(L, R):
    merged = []
    i = j = 0
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            merged.append(L[i])
            i += 1
        else:
            merged.append(R[j])
            count += len(L) - i
            j += 1
    # dodajemy to co zostało
    merged.extend(L[i:])
    merged.extend(R[j:])
    return merged
```

to zwróci dokładnie tyle inwersji ile jest, dowód indukcyjny.
W kroku indukcyjnym zauważamy, że jeśli $x \in R$ jest mniejsze od $y \in L$ to $x$ jest w inwersji ze wszystkimi pozostałymi elementami $L$, od $y$ do końca.
Nasz algorytm poprawnie je zliczy.

---

# Zadanie 9

![[Pasted image 20250428090349.png]]



---

# Zadanie 10