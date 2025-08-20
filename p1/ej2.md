## Ejercicio 2

(a) Determinar los valores de k ∈ R para que el siguiente sistema tenga solucion unica, infinitas soluciones, o no tenga solucion:

```
x1 + kx2 − x3 = 1
−x1 + x2 + k2x3 = −1
x1 + kx2 + (k − 2)x3 = 2
```

Matriz ampliada

```
 1 k -1  | 1
-1 1 k^2 | -1
1  k k-2 | 2
```

f2 + f1 -> f2

```
 1  k   -1    | 1
 0 k+1  k^2-1 | 0
 1  k   k-2   | 2
```

f3 - f1 -> f3

```
 1  k   -1    | 1
 0 k+1  k^2-1 | 0
 0  0   k-1   | 1
```

```
 x1 + k*x2     -     x3  = 1
      (k+1)*x2 + (k^2-1)*x3 = 0
                  (k-1)*x3 = 1
```

Para que sea incompatible, `k=1`  
Para que tenga infinitas, `k=-1`, ya que la segunda ecuacion se hace nula, y esto hace por definicion que sea un SCI.
Para que tenga una sola, `|k|≠1` 


