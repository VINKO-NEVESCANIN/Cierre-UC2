with open ("calificaciones.txt", "w") as archivo:
    for i in range(3):
        nombre = input("Alumno: ")
        calif = input("Calificacion: ")
        archivo.write(f"{nombre}, {calif}\n")
        
with open ("calificaciones.txt", "r") as archivo:
    for linea in archivo:
        nombre,calif = linea.strip().split(",")
        print(f"Alumno: {nombre}, Calificacion: {calif}")
        
        
n = int(input("Ingresa un numero Entero:"))

for i in range(1, n +1):
    if i % 2 == 0:
        print(i, "Es un numero par")
    else:
        print(i, "Es un numpero impar")                   