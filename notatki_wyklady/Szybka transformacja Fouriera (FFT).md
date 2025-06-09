# FFT do mnożenia wielomianów

**Dane:** $a_0, \dots, a_{n-1}$ - wsp. wielomiany $A$

**Wynik:** $A(x_0), A(x_1), \dots, A(x_{n-1})$, $x_i$ - pierwiastki n-tego stopnia z $A$

Niech $\omega_n$ - pierwotny pierwiastek n-tego stopnia z $A$
(pierwotny pierwiastek generuje wszystkie inne pierwiastki)

$x_i = \omega_n^i$

**Fakt:**
Zbiór $\{(\omega_n^i)^2: i=0,\dots, n-1\}$ jest równy $\{(\omega_{\frac{n}{2}}^i)^2: i=0,\dots, \frac{n}{2}-1\}$

TODO: rysunek z kołem i pierwiastkami dla n = 8

Zamiast pisania, że mamy wielomian o $n$ istotnych współczynnikach mówimy, że 
wielomian ma stopień $n$.

Na podstawie 
$$
A(x) = a_0 + a_1 x + a_2 x^2 + \dots + a_{n-1}x^{n-1}
$$

Tworzymy dwa wielomiany stopnia $\frac{n}{2}$

parzyste
$$
A^{[p]}(z) = a_0 + a_2 x + a_4 x^2 + \dots + a_{n-2}x^{\frac{n-2}{2}}
$$

nieparzyste
$$
A^{[np]}(z) = a_1 + a_3 x + a_5 x^2 + \dots + a_{n-1}x^{\frac{n-2}{2}}
$$

Widać, że $A(x) = A^{[p]}(x^2) + x\cdot A^{[np]}(x^2)$

Chcemy policzyć:
$A(\omega_n^0) = A^{[p]}((\omega_n^0)^2) + (\omega_n^0)\cdot A^{[np]}((\omega_n^0)^2)$
$A(\omega_n^1) = A^{[p]}((\omega_n^1)^2) + (\omega_n^1)\cdot A^{[np]}((\omega_n^1)^2)$
$\vdots$
$A(\omega_n^{n-1}) = A^{[p]}((\omega_n^{n-1})^2) + (\omega_n^{n-1})\cdot A^{[np]}((\omega_n^{n-1})^2)$

To jest przepis na redukcję, bo punktów $\omega_n^{i}$ jest $\frac{n}{2}$

Czyli zredukowaliśmy problem rozmiaru $n$ do dwóch problemów rozmiaru $\frac{n}{2}$

Algorytm fft:
```
def FFT(A):
    if(n == 1) return A
    w_n <- exp((2 pi i)/n) // n-ty pierwiastek pierwotny z x
    w <- 1
    A_p <- [a_0, a_2, a_4, ..., a_n-2]
    A_np <- [a_1, a_3, a_5, ..., a_n-1]
    y_0 <- FFT(A_p)
    y_1 <- FFT(A_np)
    for k <- 0...n/2 - 1:
        y_k <- y_0[k] + w * y_1[k]
        y_{k+n\2} <- y_0[k] - w * y_1[k]
        w <- w * w_n
```

omega ^ k + n/2 = - omega ^ k

w pętli for liczymy wynik $y_i = A(\omega_{n}^{i})$

Co zrobiliśmy?

Dla danych $a_i$ obliczyliśmy $y_i = A(\omega_n^i)$

$A$ - wektor $a_i$
$Y$ - wektor $y_i$

Tym algorytmem zrobiliśmy przekształcenie: $Y = V_n \cdot A$
$$
V_n = 
\begin{bmatrix}
1 & (w_n^0)^1 & (w_n^0)^2 & \dots & (w_n^0)^{n-1} \\
1 & (w_n^1)^1 & (w_n^1)^2 & \dots & (w_n^1)^{n-1} \\
&  & \;\; \vdots \\
1 & (w_n^{n-1})^1 & (w_n^{n-1})^2 & \dots & (w_n^{n-1})^{n-1} \\
\end{bmatrix}
$$

$V_n$ ma na pozycji $(i,j)$ wartość $w_n^{i \cdot j}$

To jest macierz Vandermora (?), ma macierz odwrotną.
$V_n^{-1}$ ma na pozycji $(i,j)$ wartość: 
$$
\frac{w_n^{-ij}}{n}
$$

To obliczenie da się zrobić korzystając z tej samej procedury.

**Fakt:** Niech $n$ i $w$ będą potęgami liczby 2 (różnymi od 1)

