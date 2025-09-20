vocales = "aeiouAEIOU"
entrada = input("Ingrese una cadena de texto: ")
resultado = ""
for c in entrada:
    if c not in vocales:
        resultado += c
print("Texto sin vocales:", resultado)
