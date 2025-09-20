def factorial(n):
    
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

n = int(input("Ingrese un número para calcular su factorial: "))
if n < 0:
    print("El factorial no está definido para números negativos.")
else:   
    print(f"Factorial de {n} es: {factorial(n)}")