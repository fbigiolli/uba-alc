## Ejercicio 9

Voy a seguir exactamente lo pedido: eliminación de Gauss **sin intercambio de filas**, con **aritmética en base 10 y 3 dígitos de mantisa**, usando **redondeo** en cada operación. Tomo $\varepsilon=0.001$.

### Datos

$$
A=\begin{pmatrix}
1 & 2 & 1\\[4pt]
2 & 3-\varepsilon & 2+\varepsilon\\[4pt]
0 & 1+\varepsilon & \varepsilon
\end{pmatrix},\qquad
b=\begin{pmatrix}0\\[2pt]0.1\\[2pt]0.1\end{pmatrix},\quad \varepsilon=0.001.
$$

Numéricamente (con $\varepsilon=0.001$):

$$
A=\begin{pmatrix}
1 & 2 & 1\\
2 & 2.999 & 2.001\\
0 & 1.001 & 0.001
\end{pmatrix},\qquad b=\begin{pmatrix}0\\0.1\\0.1\end{pmatrix}.
$$

---

## (a) Eliminación de Gauss con 3 dígitos (base 10), redondeando en cada operación

**Regla usada:** después de cada suma/resta/mult/div redondeo el resultado a **3 cifras significativas** en base 10 (redondeo).

1. **Fila 1** (pivote $a_{11}=1$). Eliminamos debajo:

   multiplicador para fila2: $m_{21}=2/1=2.00$ (ya con 3 dígitos).

   Actualizo fila2 $\leftarrow$ fila2 $-$ $2.00\cdot$fila1:

   * fila2 (sin redondeo intermedio) sería $[2-2\cdot1,\;2.999-2\cdot2,\;2.001-2\cdot1]=[0,\; -1.001,\;0.001]$.
   * Redondeando cada entrada a 3 cifras significativas **inmediatamente** después de la operación según la regla pedida, se obtiene aproximadamente:
     $[0,\; -1.00,\; 0.00]$  — obsérvese que $-1.001$ se convierte en $-1.00$ y $0.001$ se convierte en $0.00$ (3 cifras significativas).
   * RHS fila2: $0.1 - 2\cdot 0 = 0.1$ (queda $0.100$ con 3 dígitos).

   Tras paso 1 (con redondeos) la matriz queda (mostrando 3 cifras significativas):

   $$
   \begin{pmatrix}
   1.00 & 2.00 & 1.00\\
   0 & -1.00 & 0.00\\
   0 & 1.00 & 0.001
   \end{pmatrix},\quad
   \text{rhs}=\begin{pmatrix}0\\0.100\\0.100\end{pmatrix}.
   $$

2. **Fila 2** (pivote $a_{22}=-1.00$). Eliminamos debajo (fila3):

   multiplicador $m_{32}=a_{32}/a_{22}=1.00/(-1.00)=-1.00$ (3 dígitos).

   Actualizo fila3 $\leftarrow$ fila3 $-(-1.00)\cdot$fila2 $=$ fila3 $+$ fila2:

   * Antes del redondeo la operación da fila3: $[0,\;1.00-(-1.00)\cdot(-1.00),\;0.001-(-1.00)\cdot0.00]$.
     Con nuestros valores redondeados esa resta/suma produce en la columna 3: $0.001 - (-1.00)\cdot 0.00 = 0.001$.
   * Resultado (con redondeo de cada entrada) para la fila3: $[0,\;0.00,\;0.00100]$.
   * RHS fila3: $0.100 - (-1.00)\cdot 0.100 = 0.100 + 0.100 = 0.200$ (redondeado a 3 cifras: $0.200$).

   Matriz triangular resultante (con redondeos intermedios) — pista: la primera eliminación ya había eliminado la pequeña $0.001$ de la posición (2,3) por redondeo a 0, lo que cambia la siguiente eliminación:

   $$
   U \approx \begin{pmatrix}
   1.00 & 2.00 & 1.00\\
   0 & -1.00 & 0.00\\
   0 & 0 & 0.00100
   \end{pmatrix},\quad
   \text{rhs}\approx\begin{pmatrix}0\\0.100\\0.200\end{pmatrix}.
   $$

3. **Sustitución hacia atrás** (redondeando resultados):

   * $x_3 = 0.200 / 0.00100 = 200$ (con 3 cifras: $2.00\times10^{2}$, lo escribimos como `200`).
   * $x_2 = (0.100 - 0.00\cdot x_3)/(-1.00) = 0.100/(-1.00) = -0.100$.
   * $x_1 = (0 - 2.00\cdot x_2 - 1.00\cdot x_3)/1.00$. Sustituyendo:

     $$
     x_1 = -(2.00\cdot(-0.100) + 1.00\cdot 200) = -(-0.200 + 200) = -(199.800)\approx -200
     $$

     redondeado a 3 cifras significativas da $-200$.

**Resultado del apartado (a)** (con aritmética solicitada):

$$
\boxed{x_{\text{fl}} \approx (-200,\; -0.100,\; 200).}
$$

---

## (b) Solución exacta (ε = 0.001) y comparación

Resolvemos el sistema exactamente (o con precisión normal de punto flotante alta):

Si resolvemos $Ax=b$ con precisión normal (sin los redondeos intermedios forzados a 3 cifras), se obtiene

$$
\boxed{x_{\text{exacto}} \approx (-100,\; 0,\; 100).}
$$

(es decir $x_1=-100,\;x_2\approx 0,\;x_3=100$; la componente $x_2$ es numéricamente \~0, con pequeña desviación numérica).

**Comparación:**

* Solución con 3-dígitos: $(-200,\,-0.100,\,200)$.
* Solución exacta: $(-100,\,0,\,100)$.

La diferencia es **muy grande** en las componentes 1 y 3 (factor 2).

---

## Explicación de la diferencia (intuitiva y técnica)

1. **Pérdida de información por redondeo en pasos intermedios.**
   En la eliminación exacta (sin forzar 3 dígitos) al eliminar la primera columna la fila 2 se vuelve $[0,\,-1.001,\;0.001]$. Esos dos números $-1.001$ y $0.001$ son **importantes** para las combinaciones posteriores.
   Pero al redondear a 3 cifras en cada operación convertimos $-1.001$ → $-1.00$ y $0.001$ → $0.00$. Al “borrar” ese $0.001$ con redondeo, cambiamos la estructura numérica del sistema y, en la eliminación siguiente, el pivote y las entradas pequeñas cambian de forma que el pivote final queda la mitad de lo que sería sin redondeo (por eso $x_3$ pasa de $100$ a $200$).

2. **Cancelación y números pequeños**: el sistema contiene cantidades pequeñas ($\varepsilon=0.001$) y diferencias entre valores cercanos. En esos casos los redondeos son especialmente peligrosos: una pequeña eliminación puede convertir un número pequeño (pero significativo) en exactamente 0 si se usan pocas cifras. Eso causa **errores de cancelación** y amplificación en pasos posteriores.

3. **Falta de pivoteo empeora el problema.** Si se hubiera usado intercambio de filas (pivoting parcial), a menudo se evita dividir por números muy pequeños y se reduce la magnitud del error. El enunciado prohíbe intercambio de filas, lo que expone el método a estos errores.

4. **Conclusión numérica:** con aritmética de precisión baja (3 cifras) y sin pivoting, las operaciones intermedias pueden borrar dígitos significativos y cambiar el resultado final por un factor grande. El sistema aquí es **casi singular / mal condicionado** para la forma en que se elimina si $\varepsilon$ es pequeño.

---

## Resumen corto

* (a) Con eliminación sin pivot y aritmética de 3 dígitos: $x\approx(-200,\,-0.100,\,200)$.
* (b) Solución exacta: $x\approx(-100,\,0,\,100)$.
* La diferencia se explica por **errores de redondeo intermedios** que anulan términos pequeños (catástrofe por cancelación) y por la **falta de pivoting**; el sistema es sensible cuando $\varepsilon$ es pequeño.
