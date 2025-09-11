## Ejercicio 6

### Enunciado

Sean f : R3 → R4 definido por:  
f(x1, x2, x3) = (x1 + x2, x1 + x3, 0, 0). 
y g : R4 → R2  
definido por:
g(x1, x2, x3, x4) = (x1 − x2, 2x1 − x2).  
Calcular el núcleo y la imagen de f, de g y de g ◦ f.
Decidir si son monomorfismos, epimorfismos o isomorfismos.

### Resolucion

#### Nucleo de f

$f(x,y,z) = (0,0,0,0) = (x+y, x+z, 0, 0)$
<=>
x = -y = -z

$ker(f) = {(x, -x, -x)} = {x(1, -1, -1)} = <(1, -1, -1)>$

#### Imagen de f

```
f(x,y,z) = (x+y, x+z, 0, 0) = {x(1, 1, 0, 0) + y(1, 0, 0, 0) + z(0, 1, 0, 0)}
         = <(1,1,0,0), (1,0,0,0), (0,1,0,0)>
```
La base queda $<(1,0,0,0), (0,1,0,0)>$ ya que el otro es comb. lineal de los otros

No es ni isomorfismo ni monomorfismo ya que el Kernel es ≠ 0.  
No es epimorfismo ya que $dim(Im(f)) = 2 ≠ dim(R^4) = 4$

---

#### Nucleo de g
$f(x_1, x_2, x_3, x_4) = (0,0,0) = (x_1 - x_2, 2x_1 - x_2)$

$⟺ x_1 = x_2 ∧ 2x_1 = x_2$ ⟺ $x_1 = 0$

$ker(f) = {(0, 0, x_3, x_4)} = {x_3(0,0,1,0), x_4(0,0,0,1)} = <(0,0,1,0), (0,0,0,1)>$

#### Imagen de g

$<(1,2), (-1,-1)>$

No es monomorfismo ni isomorfismo ya que el Kernel es ≠ 0.  
Es epimorfismo ya que $dim(Im(f)) = 2 = dim(R^2)$


#### g o f 

$g o f = g(f(x_1, x_2, x_3, x_4)) = g(x_1 + x_2, x_1 + x_3, 0, 0) = (x_2 - x_3, x_1 + 2x_2 - x_3, 0, 0)$

de aca en adelante es lo mismo que venimos haciendo...