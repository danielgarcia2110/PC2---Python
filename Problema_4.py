# Programa para imprimir el patrón solicitado

n = int(input("Ingrese el número máximo de asteriscos en la fila central: "))  # Número máximo de asteriscos en la fila central

# Parte superior del patrón
for i in range(1, n + 1):
    print('* ' * i)

# Parte inferior del patrón
for i in range(n - 1, 0, -1):
    print('* ' * i)