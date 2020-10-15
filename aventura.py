global vida
def mostrar_aventura():
    global vida
    while True:
        if(vida == 0):
            print("Te moriste!")
            break
        print("Caminos disponibles")
        print("1- Bosque")
        print("2- Lago")
        print("3- Cueva")
        print(f"Tenes {vida} vidas!")
        camino = int(input("Para donde vas a ir? "))
        if(camino == 1):
            print("Te cruzaste con un animal salvaje que te atacó, entonces perdiste una vida...")
            vida = vida -1
        if(camino == 2):
            print("Estás avanzando por el lago... parece que podes seguir caminando... pero el siguiente camino todavia no está terminado!")
        if(camino == 3):
            opcion = 0
            while(opcion != 1):
                opcion = int(input("No hay nada en la cueva... queres volver? (0=no, 1=si): "))


print("Bienvenido a Aventura Solida!\n-------------------")
nombre = input("Cuál es tu nombre? ")
nombre = nombre[0].upper() + nombre[1:].lower()
print("Hola " + nombre + "!")
dif = 0
while(1):
    dif = input("Elija la dificultad Facil(1), Medio(2), Dificil(3): ")
    try:
        dif = int(dif)
    except:
        print("Sólo se admite un núm. del 1 al 3!")
        continue
    if(dif == 1):
        vida = 3
    if(dif == 2):
        vida = 2
    if(dif == 3):
        vida = 1
    else:
        print("Ingrese un numero valido")
    if(dif >= 1 and dif <= 3):
        break

mostrar_aventura()
