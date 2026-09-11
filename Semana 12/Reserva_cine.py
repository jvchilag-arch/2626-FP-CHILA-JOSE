# 1. Crear matriz asientos [3][4] con todos los vcalores en 0
asientos =[[0 for _ in range(4)] for _ in range(3)]

# 2. Pedir al usuario la fila y la columna del asiento
f = int(input("ingrese fila (0 a 2) "))
c = int(input("ingrese columna (0 a 3): "))

# 3. Marcar el asiento como reservado (1)
asientos[f][c] = 1

# 4. Mostrar la matriz completa en formato de tabla
print("\nEstadode la sal (0=libres, 1=reservado):")
print("    0 1 2 3")
print("    ---------")
for i in range(3):
    print(i, "|", end=" ")
    for j in range (4):
        print(asientos[i][j], end=" ")
    print()