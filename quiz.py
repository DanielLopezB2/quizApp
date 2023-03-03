print()
print("Bienvenido a QuizApp!")
print()

jugar = input("Quieres jugar? ")
print()

if jugar.lower() != "si":
    quit()

print("Empecemos :D")
print()

puntos = 0

##1
respuesta = input(f"¿Quién es el autor de la novela ''Cien años de soledad''? ")
print()


if respuesta.lower() == "gabriel garcía márquez" or respuesta.lower() == "gabriel garcia marquez":
    print("La respuesta es correcta!")
    puntos += 100
    print()
    print("+",puntos,"pts")
    print()

else:

    print("La respuesta es incorrecta!")
    puntos += 0
    print()
    print("+",puntos,"pts")
    print()

##2
respuesta = input(f"¿Cuál es el río más largo del mundo? ")
print()

if respuesta.lower() == "rio nilo" or respuesta.lower() == "nilo" or respuesta.lower() == "el nilo":
    print("La respuesta es correcta!")
    puntos += 100
    print()
    print("+",puntos,"pts")
    print()

else:

    print("La respuesta es incorrecta!")
    puntos += 0
    print()
    print("+",puntos,"pts")
    print()

##3
respuesta = input(f"¿Quién escribió la obra de teatro 'Hamlet'? ")
print()

if respuesta.lower() == "william shakespeare" or respuesta.lower() == "shakespeare":
    print("La respuesta es correcta!")
    puntos += 100
    print()
    print("+",puntos,"pts")
    print()

else:

    print("La respuesta es incorrecta!")
    puntos += 0
    print()
    print("+",puntos,"pts")
    print()

##4
respuesta = input(f"¿Cuál es la capital de Australia? ")
print()

if respuesta.lower() == "canberra":
    print("La respuesta es correcta!")
    puntos += 100
    print()
    print("+",puntos,"pts")
    print()

else:

    print("La respuesta es incorrecta!")
    puntos += 0
    print()
    print("+",puntos,"pts")
    print()

##5
respuesta = input(f"¿Quién pintó 'La noche estrellada'? ")
print()

if respuesta.lower() == "vincent van gogh" or respuesta.lower() == "van gogh":
    print("La respuesta es correcta!")
    puntos += 100
    print()
    print("+",puntos,"pts")
    print()

else:

    print("La respuesta es incorrecta!")
    puntos += 0
    print()
    print("+",puntos,"pts")
    print()

##6
respuesta = input(f"¿Qué país tiene la bandera cuadrada? ")
print()

if respuesta.lower() == "suiza":
    print("La respuesta es correcta!")
    puntos += 100
    print()
    print("+",puntos,"pts")
    print()

else:

    print("La respuesta es incorrecta!")
    puntos += 0
    print()
    print("+",puntos,"pts")
    print()

##7
respuesta = input(f"¿Cuál es el océano más grande del mundo? ")
print()

if respuesta.lower() == "océano pacífico" or respuesta.lower() == "oceano pacifico" or respuesta.lower() == "pacifico":
    print("La respuesta es correcta!")
    puntos += 100
    print()
    print("+",puntos,"pts")
    print()

else:

    print("La respuesta es incorrecta!")
    puntos += 0
    print()
    print("+",puntos,"pts")
    print()

##8
respuesta = input(f"¿En qué año se celebraron los Juegos Olímpicos de Londres? ")
print()

if respuesta.lower() == "2012":
    print("La respuesta es correcta!")
    puntos += 100
    print()
    print("+",puntos,"pts")
    print()

else:

    print("La respuesta es incorrecta!")
    puntos += 0
    print()
    print("+",puntos,"pts")
    print()

##9
respuesta = input(f"¿En qué país se encuentra el Monte Kilimanjaro? ")
print()

if respuesta.lower() == "tanzania":
    print("La respuesta es correcta!")
    puntos += 100
    print()
    print("+",puntos,"pts")
    print()

else:

    print("La respuesta es incorrecta!")
    puntos += 0
    print()
    print("+",puntos,"pts")
    print()

##10
respuesta = input(f"¿Cuál es el nombre completo del actor que interpretó a Harry Potter en las películas? ")
print()

if respuesta.lower() == "daniel radcliffe":
    print("La respuesta es correcta!")
    puntos += 100
    print()
    print("+",puntos,"pts")
    print()

else:

    print("La respuesta es incorrecta!")
    puntos += 0
    print()
    print("+",puntos,"pts")
    print()

print("Tu puntación final es: ",puntos)