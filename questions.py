import random

foods = [
    "pizza",
    "hamburguesa",
    "asado",
    "milanesa",
    "pancho",
    "fideos",
]

sports = [
    "futbol",
    "tenis",
    "voley",
    "rugby",
    "basket",
    "boxeo",
]

countries = [
    "japon",
    "mexico",
    "australia",
    "argentina",
    "alemania",
    "italia"
]

cities = [
    "londres",
    "Sidney",
    "Zurich",
    "Lima",
    "Santiago",
    "Brasilia"
]

categories = {"comida": foods,
              "deportes": sports,
              "paises": countries,
              "ciudades" : cities
             }


guessed = []
attempts = 6
points = 0

print("¡Bienvenido al Ahorcado!")
print()

print("")

for elem in categories:
    print(elem," ")
while True:
    C = input("ingrese que categoria desea jugar: ")
    if C in categories:
        word = random.choice(categories[C])
        break
    print("categoria invalida")

while attempts > 0:
    # Mostrar progreso: letras adivinadas y guiones para las que faltan
    progress = ""
    for letter in word:
        if letter in guessed:
            progress += letter + " "
        else:
            progress += "_ "
    print(progress)
    # Verificar si el jugador ya adivinó la palabra completa
    if "_" not in progress:
        points += 6
        print("puntaje: ",points)
        print("¡Ganaste!")
        break

    print(f"Intentos restantes: {attempts}")
    print(f"Letras usadas: {', '.join(guessed)}")

    letter = input("Ingresá una letra: ")

    if len(letter) != 1 or not letter.isalpha():
        print("entrada no valida")
        continue
    elif letter in guessed:
        print("Ya usaste esa letra.")
    elif letter in word:
        guessed.append(letter)
        print("¡Bien! Esa letra está en la palabra.")
    else:
        guessed.append(letter)
        attempts -= 1
        points -= 1
        print("Esa letra no está en la palabra.")

    print()
else:
    points = 0
    print("puntaje: ",points)
    print(f"¡Perdiste! La palabra era: {word}")