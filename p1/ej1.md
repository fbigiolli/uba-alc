# Ejercicio 1

Paso 1. Construimos la matriz ampliada

Triangulamos la matriz realizando operaciones de filas. Las operaciones permitidas (que no
afectan las soluciones del sistema) son:
sumarle o restarle a una fila un múltiplo de otra fila,
intercambiar dos filas entre si.
multiplicar una fila por un escalar distinto de 0
```
1 1 -2 1 | -2
3 -2 1 5 | 3
1 -1 1 2 | 2
```
-> rotamos f3 y f2
```
1 1 -2 1 | -2
1 -1 1 2 | 2
3 -2 1 5 | 3
```
f2 - f1 -> f2
```
1 1 -2 1 | -2
0 -2 3 1 | 4
3 -2 1 5 | 3
```
f3 - 3 * f1 -> f3
```
1 1 -2 1  | -2
0 -2 3 1  | 4
0 -5 7 2 | 9
```
2 * f3 - 5 * f2  -> f3
```
1  1 -2  1  | -2
0 -2  3  1  | 4
0  0  -1 -1 | -2
```
```
1* x1 +  1 * x2 - 2 * x3 +  1 * x4 = -2
        -2 * x2 + 3 * x3 +  1 * x4 =  4
                 -1 * x3 -  1 * x4 = -2
```
```
Solucion general 
x1 = 1 - 2 * t
x2 = 1 - t
x3 = 2 - t
x4 = t
```

Algoritmo devuelve:
```
Matriz escalonada: 
 [[ 1.   1.  -2.   1.  -2. ]
 [ 0.   1.  -1.4 -0.4 -1.8]
 [ 0.   0.   1.   1.   2. ]]
```

b) 

Algoritmo devuelve:
```
Matriz escalonada punto B: 
 [[ 1.    1.    1.   -2.    1.    1.  ]
 [ 0.    1.   -0.   -0.75 -0.    0.25]
 [ 0.    0.    0.    0.    0.    1.  ]]
 ```
 No hay soluciones.

c)
```
i*x1 − (1 + i)*x2 = −1
  x1 − 2*x2 + x3 = 0
  x1 + 2i*x2 − x3 = 2i
```

```
i -(1+i) 0 | -1
1   -2   1 | 0
1   2i  -1 | 2i
```
f3 - f2 -> f3
```
i -(1+i)   0 | -1
1   -2     1 | 0
0   2i+2  -2 | 2i
```
f2 + i*f1 -> f2
```
i -(1+i)       0 | -1
0   -i - 1     1 | -i
0   2i+2      -2 | 2i
```
f3 - 2*f2 -> f3
```
i -(1+i)       0 | -1
0   -i-1     1 | -i
0   0         -4 | 0
```

```
i*x1 - (1+i)*x2 = -1
(-i-1)*x2 + x3  = -i
-4*x3           =  0
```
-> x3 = 0 

resolvemos x2 con el resultado de x3
```
(-i-1)*x2 = -i
x2 = -i / (-1-i)
```
-> x2 = 1/2 + 1/2i

resolvemos x1 con los resultados de x2 y x3
```
i*x1 - (1+i)*(1/2 + (1/2)*i) = -1
i*x1 - i = -1
i*(x1 - 1) = -1
(x1 - 1) = -1/i
x1 = -1/i + 1
```
-> x1 = i + 1

```
resultado final = {
    x1 : i+1
    x2 : 1/2 + 1/2i
    x3 : 0
}
```

d) TODO...




