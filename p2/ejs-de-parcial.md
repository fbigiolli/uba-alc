# 1  
### Item a
Sea M ∈ Rn×n una matriz tal que existe una norma (subordinada a una norma vectorial) que cumple que ∥M∥ < 1.
Probar que I_n − M es inversible, siendo I_n la matriz identidad de orden n.

I − M es inversible
sii
det(I-M) != 0
sii
Nul(I-M) = 0
sii
(I-M)x = 0 solo con x = 0

Con norma ||.||_1
tenemos que eixtse fila x_i en M tq $0 \leq \sum_j |x_{ij}| < 1$  

Como siempre en las normas tomamos valores positivos (por módulos o por potencia)

Si es inversible, entonces  $Nu(I_n - M) = <(0,0,0,...,0)>$, para que eso pase:

$$
(I_n - M)x_0 = 0 \iff x_0=0\\
\iff \\
I_nx_0 - Mx_0 = 0 \\
\iff \\
x_0 - Mx_0 = 0 \\
\iff \\
x_0 = Mx_0
$$

Si probamos que $x=0$, entonces probamos que es inversible.  
Por la condicion de la norma que nos dan, sabemos que $∀i,j 0 ≤ |K_{ij}| ≤ 1 $.

Supongamos que $x≠0$ y veamos que no se preserva la igualdad de $x_0 = Mx_0$

Por definicion de la norma subordinada a una norma vectorial, tenemos que:  

$$
\|M\|_{m,n} = \max_{0 \neq x \in K^n} \left\{ \frac{\|Mx\|_m}{\|x\|_n} \right\} 
= \max_{\substack{x \in K^n , \|x\|_n = 1}} \{ \|Mx\|_m \}
$$

como dijimos que $x_0 \neq 0$

$$
\frac{\|Mx_0\|}{\|x_0\|} \leq \|M\| < 1 \\
\iff \\
\frac{\|Mx_0\|}{\|x_0\|} < 1 \\
⟺ \\ 
(\text{por ser division y porque } Mx_0 = x_0) \\
\|Mx_0\| = \|x_0\| < \|x_0\|\ \ \text{Absurdo papá}
$$

Luego es mentira que $x \neq 0 \Rightarrow x = 0$

---
### Item b

#### Inciso I
Sabemos que lo que hace la transformacion lineal es trasponer el input y multiplicarlo por un escalar $> 0$.

$$
||f(A)||_1 =  || γ * A^t||_1 = γ * ||A^t||_1 = y * || A ||_∞ = γ * a 
$$

#### Inciso II

--- 

# 2

$$
\text{Sean } \alpha > 0 \text{ y } A(\alpha) \in \mathbb{R}^{4 \times 4} \text{ un conjunto de matrices que dependen de } \alpha, \text{ dadas por:}
$$

$$
A(\alpha) =
\begin{pmatrix}
1 & 2 & 0 & 1 \\
\alpha & \alpha^2 + 2\alpha & \alpha & 2\alpha \\
1 & 2 & \alpha^2 - 1 & 1 \\
1 & 2 & 0 & 2
\end{pmatrix}
$$

**a)** Encontrar los valores de $\alpha$ para los cuales $A(\alpha)$ no es inversible.  
```
1     2       0      1 
a a^2 + 2a    a      2a   
1     2     a^2-1    1
1     2       0      2

f3 -> f3 - f1

1     2       0      1 
a a^2 + 2a    a      2a   
0     0     a^2-1    0
1     2       0      2

f4 -> f4 - f1

1     2       0      1 
a a^2 + 2a    a      2a   
0     0     a^2-1    0
0     0       0      1

f2 -> f2 - a * f1

1     2       0      1 | 0
0    a^2      a      a | 0  
0     0     a^2-1    0 | 0
0     0       0      1 | 0

```

Una vez llegado aca, el determinante de una matriz triangular superior es la multiplicacion de los elementos de la diagonal.

Luego, como $a≠0$ podemos dividir la ecuacion por $a$:

$$
a^4 - a^2 = 0 \\
a^2 - 1 = 0 \\ 

a^2 - 1 = 0 ⟺ a = 1 ∨ -1
$$

Entonces, si $a = 1 ∨ a = -1$ la matriz **NO** es inversible.

**b)** Probar que $\text{cond}_{\infty}(A(\alpha)) \xrightarrow[\alpha \to 1]{} +\infty.$  

$$
\text{cond}(A) \geq \sup_{\substack{B \text{ singular}}} \left\{ \frac{\|A\|}{\|A-B\|} \right\}
$$




**c)** ¿Qué puede decir de $\lim_{\alpha \to 1} \text{cond}_2(A(\alpha))$?
