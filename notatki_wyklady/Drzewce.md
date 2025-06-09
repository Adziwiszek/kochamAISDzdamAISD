Po angielsku Treap (tree + heap)

# Definicja

- drzewo BST
- w wierzchołkach pamiętamy pary $<k,p>$ (klucz, priotytet)
- wzg. kluczy - porządek BST
- wzg. priorytetów - porządek kopcowy

# Przykład

Klucze:     a, b,  c, d, f, g, r
Priorytety: 7, 10, 4, 2, 9, 3, 6 
dopytac sie jak powstawal ten rysunek

todo rysunek 

**Fakt** Dla każdego zestawu $<k_i, p_i>$ istnieje dzrzewiec (który...) dopytać się 

**Spostrzeżenie** Jeśli $\forall i \neq j \; (p_i \neq p_j) \wedge (k_i \neq k_j)$ to ten drzewiec jest unikalny.

# Operacje 

## Find(k)

Szukanie klucza jak w drzewie BST po kluczu

## Insert(k, p)

Wstawiamy jak w BST. 
Rotacjami przesuwamy wierzchołek z $k$, aż ojciec(k) ma priorytet większy od k.

## Delete(k)

- Najpierw robimy find(k)
- rotacjami k przesuwamy na dół
- gdy jest liściem odcinamy

Rotujemy w dół z synem, który ma większy priorytet.

# Jak przydzielać priorytety?

losowo

Założenia:
- wylosowane priorytety są różne
- każda permutacja kluczy otrzymana przez posortowanie ich względem 
    priorytetów jest jednakowo prawdopodobna.
- klucze są różne

# Analiza delete

n kluczy od 1 do n.

Rozważamy operację delete(m). Pokażemy, że $\forall m$ oczekiwany czas delete(m) to $O(log\;n)$.

1) Przejście ścieżki od korzenia do $m$ (nazywamy ją A)
2) ilość rotacji, żeby przenieść $m$ do liścia (suma długości maks. prawej 
    ścieżki w lewym poddrzewie i maks. lewej ścieżki w prawym poddrzewie)

**Oznaczenie**
$m_{\leq} = \{ 1,...,m \}$
$m_{\geq} = \{ m,m+1,...,n \}$

Chcemy oszacować oczekiwaną długość A.

$$
|A| = |A \cap m_{\leq}| + |A \cap m_{\geq}| - 2
$$

Niech $\sigma$ to permutacja kluczy według priorytetów

$m = 8$

$\sigma$: 4, 2, 3, 6, 1, 9, 7, 8, 12, 5, 11

Na ścieżce z korzenia do m będą $4,6,7,8$

klucz k z $m_{\leq}$ należy do a (oznaczymy go v), jeśli
1) k jest przed m w $\sigma$
2) oraz ke jest max prefixowym w $\sigma'$ (gdzie $\sigma'$ powstaje przez usunięcie z $\sigma$ kluczy z $m_{\geq}$)

Możemy obliczyć oczekiwaną wartość $|A \cap m_{\leq}|$

Niech $X_m$ to zmienna losowa równa liczba oznaczonych kluczy (kluczy, które są 
mniejsze od m na ścieżce od korzenia do m)
