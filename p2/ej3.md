## Ejercicio 3

### Enunciado

Ejercicio 3. (a) Probar que existe una unica transformacion lineal f : R2 → R2 tal que
f (1, 1) = (−5, 3) y f (−1, 1) = (5, 2). Para dicha f , determinar f (5, 3) y f (−1, 2).

(b) ¿Existira una transformacion lineal f : R2 → R2 tal que f (1, 1) = (2, 6), f (−1, 1) =
(2, 1) y f (2, 7) = (5, 3)?

(c) Sean f, g : R3 → R3 transformaciones lineales tales que
f (1, 0, 1) = (1, 2, 1), f (2, 1, 0) = (2, 1, 0), f (−1, 0, 0) = (1, 2, 1),
g(1, 1, 1) = (1, 1, 0), g(3, 2, 1) = (0, 0, 1), g(2, 2, −1) = (3, −1, 2).
Determinar si f = g

### Resolucion

### Item a

a)Nosotros tenemos que probar que 
f(1,1) = (-5,3) y
f(-1,1) = (5,2)
son unicas

Primero observo que (1,1) y (-1,1) son linealmente independientes por ende forman una base de R2.

Entonces por definicion sabemos que existe una unica transformacion lineal
que cada uno de los vectores de la base, por ende son unicas. 


Para calcular f(5, 3), primero veamos cuales son las coordenadas de (5,3) en nuestra base. Luego,
por propiedades de las TL podemos usar estas coordenadas y "sacarlas para afuera" multiplicando para obtener en el resultado de la TL aplicado a este vector.

```
1  -1 | 5
1   1 | 3

f2 -> f2 - f1

1 -1 | 5
0  2 | -2
```

b = -1

a = 4

-> (5,3) es (4,-1) en esta base

ahora, en la TL:
```
f(4 * v1 - v2) = 4 * f(v1) - f(v2)
               = 4 * (-5,3) - (5,2)
               = (-25,10)
```

```
1  -1 | -1
1   1 |  2

f2 -> f2 - f1

1 -1 | -1
0  2 |  3
```

b = 3/2
a = 1/2

-> (-1,2) es (1/2, 3/2) en esta base

ahora, en la TL:
```

f(-1,2) =   f(1/2*(-5,3) + 3/2*(5,2)) = 
            1/2*(-5,3) + 3/2*(5,2) =
            (5,9/2)


```

### Item b

Sabemos que (1,1) y (-1,1) son una base, o sea que (2,7) es LD con ellos y por ende se puede escribir como CL. Hagamoslo y veamos si con los coeficientes vale la igualdad pedida
```
1  -1 | 2
1   1 | 7

f2 -> f2 - f1

1 -1 | 2
0  2 | 5
```

b = 5/2
a = 9/2

-> (2,7) es (5/2,9/2) en esta base.

Ahora, en la TL:
```
(5,3) = f(5/2 * v1 + 9/2 * v2)
(5,3) = 5/2 * (2,6) + 9/2 * (2,1)
(5,3) = no voy a hacer la cuenta, es obvio que no vale
```

Luego, como la TL es unica para esa base por el teorema, no existe una TL que satisfaga lo pedido.

### Item C

TODO...