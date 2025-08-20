from row_echelon import row_echelon
import numpy as np

terminos_independientes_sistema_homogeneo = np.array([0,0,0])

# Punto A
punto_a_matriz_ampliada = np.array([
    [1, 1, -2, 1],
    [3, -2, 1, 5],
    [1, -1, 1, 2]
])
punto_a_terminos_independientes = np.array([-2,3,2])

punto_a = np.c_[punto_a_matriz_ampliada, punto_a_terminos_independientes]
print("Matriz escalonada punto A: \n", row_echelon(punto_a))

# No es posible buscar una unica solucion porque la matriz no es cuadrada, tiene infinitas soluciones
# solucion = np.linalg.solve(punto_a_matriz_ampliada, punto_a_terminos_independientes)
# print("Solucion: ", solucion)

# Punto B
punto_b_matriz_ampliada = np.array([
    [1,1,1,-2,1],
    [1,-3,1,1,1],
    [3,-5,3,0,3]
])
punto_b_terminos_independientes = np.array([1,0,0])

punto_b = np.c_[punto_b_matriz_ampliada, punto_b_terminos_independientes]
print("Matriz escalonada punto B: \n", row_echelon(punto_b))