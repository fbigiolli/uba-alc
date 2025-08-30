## Ejercicio 8

### Enunciado 
Ejercicio 8. Determinar todos los k ∈ R para los cuales:
(a) ⟨(−2, 1, 6), (3, 0, −8)⟩ = ⟨(1, k, 2k), (−1, −1, k2 − 2), (1, 1, k)⟩.

(b) S ∩ T = ⟨(0, 1, 1)⟩ siendo S = {x ∈ R : x1 + x2 − x3 = 0} y T = ⟨(1, k, 2), (−1, 2, k)⟩.

### Resolucion
```
Queremos que (0,1,1) pertenezca a T, por ende: 

0 = a - b
1 = a*k + 2b
1 = 2a + kb

de la primera:
a = b

en la segunda: 

1 = a*k + 2a
1 = a*(k+2)
1/k+2 = a

Entonces, k ≠ 2

en la tercera es la mismsa igualdad, no hace falta chequear.


Ahora hay que asegurar que la intersección no sea mayor que la recta ⟨(0,1,1)⟩
La única forma de que la intersección fuera más grande (dimensión 2) es que T⊆S
T⊆S, es decir que ambos generadores de T
T satisfagan la ecuación de S y sean LI:

Para (1,k,2) la ecuacion de S da 1 + k - 2 = 0 ⟹ k = 1
Para (-1,2,k) la ecuacion de S da -1 + 2 - k = 0 ⟹ k = 1

(1,1,2)
(-1,2,1)

Para k = 1 ambos vectores pertenecen a la interseccion con S, entonces si K = 1 no hay forma de que sea equivalente a <(0,1,1)> ya que ademas son LI.

```