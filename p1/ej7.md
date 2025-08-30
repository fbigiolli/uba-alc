## Ejercicio 7

### Enunciado

 Ejercicio 7. Hallar un sistema de generadores para S ∩ T y para S + T como subespacios de V , y determinar si la suma es directa en cada uno de los siguientes casos:

(a) V = R3, S = {(x, y, z) : 3x − 2y + z = 0} y T = {(x, y, z) : x + z = 0}.

(b) V = R3, S = {(x, y, z) : 3x − 2y + z = 0, x − y = 0} y T = ⟨(1, 1, 0), (5, 7, 3)⟩.

(c) V = R3, S = ⟨(1, 1, 3), (1, 3, 5), (6, 12, 24)⟩ T = ⟨(1, 1, 0), (3, 2, 1)⟩.

(d) V = R3×3, S = {(xij ) / xij = xji ∀ i, j} T = {(xij ) / x11 + x12 + x13 = 0}.

(e) V = C3, S = ⟨(i, 1, 3 − i), (4, 1 − i, 0)⟩ T = {x ∈ C3 : (1 − i)x1 − 4x2 + x3 = 0}.

### Resolucion

(a) V = R3, S = {(x, y, z) : 3x − 2y + z = 0} y T = {(x, y, z) : x + z = 0}.
```
Para obtener S ∩ T despejamos de T el valor de x, que es x = -z y lo 
reemplazamos en la ecuacion de S.

S ∩ T = {(x, y, z) : -2z − 2y = 0}
= {(x, y, z) : -2z = 2y}
= {(x, y, z) : y = -z}

Entonces, tenemos que (x,y,z) = (-z, -z, z) por ende una base es <(-1, -1, 1)>

Para la suma armamos bases de S y T

Primero armemos la base de S, para eso pongamos Z en funcion de X e Y

z = -3x + 2y
(x,y,-3x + 2y)
x*(1,0,-3), y *(0,1,2)
S = <(1,0,-3), (0,1,2)>


Armamos la base de T
tenemos que x = -z, entonces:
(-z, y, z)

z(-1,0,1), y(0,1,0)

T = <(-1,0,1), (0,1,0)>

Entonces ahora: 
S+T = <(1,0,-3), (0,1,2), (-1,0,1), (0,1,0)>

Buscamos los que son LD usando la matriz
 1  0  -3
 0  1   2
-1  0   1
 0  1   0

F3 -> F1 + F3
 1  0  -3
 0  1   2
 0  0  -2
 0  1   0

F3 -> F3 + F2
 1  0  -3
 0  1   2
 0  1   0
 0  1   0

F3 -> F3 - F4 
 1  0  -3
 0  1   2
 0  0   0
 0  1   0

Como F3 nos queda todos 0, se puede escribir como combinacion de otros vectores y por ende es LD

S+T = <(1,0,-3), (0,1,2), (0,1,0)>
```

La suma **NO** es directa porque la interseccion de ambos subespacios no es vacia.


(b) V = R3, S = {(x, y, z) : 3x − 2y + z = 0, x − y = 0} y T = ⟨(1, 1, 0), (5, 7, 3)⟩.

```
Como t = ⟨(1, 1, 0), (5, 7, 3)⟩

S ∩ T = {(x, y, z) : }

(a + 5b,a + 7b, 3b)

x = a + 5b
y = a + 7b
z = 3b

de la 1ra
a = x -5b

en la 2da
y = x + 2b 
b = (y-x) / 2

en la 3ra
z = 3/2(y-x)
2z = 3y - 3x

3x - 3y + 2z = 0

------------------
Calculamos vectores generadores de S

Por la segunda ec. de S tenemos que x = y
En la primera:
y + z = 0
z = -y

Entonces los vectores de S son de la forma
(y, y, -y) -> <(1,1,-1)>

Para que un vector pertenezca a la interseccion tiene que darse que

v = a * s1 = b * t1 + c * t2


a * s1 - b * t1 - c * t2 = 0

1  -1 -5 | 0
1  -1 -7 | 0
-1  0 -3 | 0

F3 -> F3 + F2

1  -1 -5  | 0
1  -1 -7  | 0
0  -1 -10 | 0

F2 -> F2 - F1

1  -1 -5  | 0
0   0 -2  | 0
0  -1 -10 | 0

swap F2 F3

1  -1 -5  | 0
0  -1 -10 | 0
0   0 -2  | 0

La unica solucion es la trivial, entonces la interseccion es vacia.

Luego, la suma sera directa

S + T = <(1,1-1), (1,1,0), (5,7,10)>
```

(c) V = R3, S = ⟨(1, 1, 3), (1, 3, 5), (6, 12, 24)⟩ T = ⟨(1, 1, 0), (3, 2, 1)⟩.

```

v = a*(1, 1, 3) + b*(1, 3, 5) + c*(6, 12, 24) = d*(1,1,0) + e*(3,2,1)

1 1 6  -1 -3 | 0
1 3 12 -1 -2 | 0
3 5 24  0 -1 | 0

F2 -> F2 - F1

1 1 6  -1 -3 | 0
0 2 6   0  1 | 0
3 5 24  0 -1 | 0

F3 -> F3 - 3F1

1 1 6  -1 -3 | 0
0 2 6   0  1 | 0
0 2 6   3  8 | 0

F3 -> F3 - F2 

1 1 6  -1 -3 | 0
0 2 6   0  1 | 0
0 0 0   3  7 | 0

De la 3er ecuacion tenemos que 

3d = -7e
-3/7d  = e

en la segunda

2b + 6c -3/7d = 0
2b = 3/7d - 6c
b = 3/14d - 3c

en la primera

a + 3/14d -3c + 6c - d -3*(-3/7d) = 0
a + 3c + (1/2)*d = 0
a = -3c - (1/2)*d

```
