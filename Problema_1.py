# Eliminar elementos duplicados de una lista

lista_original = [1, 1, 2, 3, 4, 4, 5, 1]
lista_procesada = []

# Recorrer cada elemento en la lista original
for elemento in lista_original:
    # Si el elemento no está en la lista procesada, agregarlo
    if elemento not in lista_procesada:
        lista_procesada.append(elemento)

print("Lista original:", lista_original)
print("Lista procesada:", lista_procesada)