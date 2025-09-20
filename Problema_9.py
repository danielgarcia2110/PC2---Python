print("Números perfectos menores que 1000:")
for num in range(2, 1000):
    suma_divisores = 0
    for i in range(1, num):
        if num % i == 0:
            suma_divisores += i
    if suma_divisores == num:
        print(num)