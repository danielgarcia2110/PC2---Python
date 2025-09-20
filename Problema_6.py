# Sistema para registrar alumnos y sus calificaciones
alumnos = []
n = int(input("¿Cuántos alumnos desea ingresar? "))
for i in range(n):
    nombre = input(f"Ingrese el nombre del alumno #{i+1}: ")
    notas = []
    for j in range(3):
        nota = float(input(f"Ingrese la nota #{j+1} para {nombre}: "))
        notas.append(nota)
    alumno = {
        "Alumno": nombre,
        "Notas": notas
    }
    alumnos.append(alumno)

print("\nListado de alumnos y sus notas:")
for alumno in alumnos:
    print(f"Alumno: {alumno['Alumno']} / Notas: {alumno['Notas']}")
