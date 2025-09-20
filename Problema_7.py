suma_primos = 0
for i in range(2, 100):
    es_primo = True
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            es_primo = False
            break
    if es_primo:
        suma_primos += i

print("La suma de todos los números primos menores que 100 es:", suma_primos)