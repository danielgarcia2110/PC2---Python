meses = [
    "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
    "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
]

fecha = input("Ingrese una fecha (MM/DD/AAAA o Mes DD, AAAA): ").strip()

# Formato MM/DD/AAAA
if "/" in fecha:
    partes = fecha.split("/")
    if len(partes) == 3:
        mes, dia, anio = partes
        print(f"{anio}-{int(mes):02d}-{int(dia):02d}")
    else:
        print("Formato de fecha inválido")
else:
    encontrado = False
    for i, mes_nombre in enumerate(meses, start=1):
        if fecha.startswith(mes_nombre):
            resto = fecha[len(mes_nombre):].strip()
            if "," in resto:
                dia, anio = resto.split(",")
                dia = dia.strip()
                anio = anio.strip()
                print(f"{anio}-{i:02d}-{int(dia):02d}")
                encontrado = True
                break
    if not encontrado:
        print("Formato de fecha inválido")