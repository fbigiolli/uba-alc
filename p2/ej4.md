## Ejercicio 4.

### Enunciado

Hallar todos los a ∈ R para los cuales exista una transformaci´on lineal f :
R3 → R3 que satisfaga que f (1, −1, 1) = (2, a, −1), f (1, −1, 2) = (a2, −1, 1) y f (1, −1, −2) =
(5, −1, −7).

### Resolucion

```
1 -1  1
1 -1  2
1 -1 -2

f2 -> f2 - f1

1 -1  1
0  0  1
1 -1 -2

f3 -> f3 - f1

1 -1  1
0  0  1
0  0 -3

son LD.
```

Como son LD, tiene que necesariamente existir una combinacion lineal de los 3 vectores que de como resultado el (0,0,0) y NO sea la trivial.

En este caso, los coeficientes 4, -3, -1. Como la TL esta definida sobre TODO R3, podemos aplicar la funcion a ambos lados de la igualdad.
```
4v1​−3v2​−v3​=(0,0,0)

f(4v1​−3v2​−v3​)=f((0,0,0))=(0,0,0) 
```
Vale que f(0,0,0) = (0,0,0) porque una TL solamente permite sumar, restar las coordenadas del vector que entra multiplicadas por un escalar, entonces en el (0,0,0) no hay TL que nos permita sumar algo distinto de 0. 

Luego, llegamos a a esta igualdad y despejamos coordenada a coordenada
```
4 * (2,a,-1) - 3 * (a^2, -1, 1) - (5,-1,-7) = (0,0,0)
```

Coordenada a coordenada nos queda:
```
3a^2 + 3 = 0
4a + 4 = 0
0 = 0 ✓
```

de la segunda, tenemos a = -1, que tambien satisface la primera. Luego, el unico a para el que vale es el -1 ∴ 
