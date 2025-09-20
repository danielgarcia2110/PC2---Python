lista = []
for i in range(1500, 2700 + 1):
    if i % 5 == 0 and i % 7 == 0:
        lista.append(i)
print("Los numeros que pueden ser divididos entre 5 y 7 son:", lista)