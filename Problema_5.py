lista = []
lista_pares = []
lista_impares = []

agregar_numeros = input("¿Desea agregar un número a la lista? (SI/NO): ")

while agregar_numeros == "SI":
    numero = int(input("Ingrese un número: "))
    if numero%2 == 0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)
    lista.append(numero)
    agregar_numeros = input("¿Desea agregar otro número a la lista? (SI/NO): ")


print("Numeros ingresados:", lista)
print("Cantidad de numeros pares:", len(lista_pares))
print("Cantidad de numeros impares:", len(lista_impares))
