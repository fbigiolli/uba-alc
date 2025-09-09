## Ejercicio 5

### Enunciado
Calcular bases del nucleo y de la imagen para cada tranformacion lineal de los
ejercicios 2 y 3. Decidir, en cada caso, si f es epimorfismo, monomorfismo o isomorfismo. En
el caso que sea isomorfismo, calcular f −1

### Resolucion

2a)
```
1 0 | 0
0 0 | 0
```
La base del kernel es <(0,1)>
y la de la imagen: <(1,0)>

Como dim(ker(f)) = 1 ⟹ no es inyectiva y por ende no es isomorfismo

2b)

```
1  0 | 0
0 -1 | 0
```

para que f(x,y) = (0,0) tanto x como y tienen que ser 0
La base del kernel es <(0,0)>


La base de la imagen es <(1,0),(0,-1)>

dim(ker(f)) = 0 ⟹ es inyectiva
dim(im(f)) = 2 ⟹ es sobreyectiva


entonces es isomorfismo. la inversa se puede calcular: 

$$
A X = I,
$$

```
1  0 | 1 0
0 -1 | 0 1

F2 -> F2 * -1

1 0 | 1  0
0 1 | 0 -1
```

La inversa entonces es $f^{-1} = (x,-y)$

