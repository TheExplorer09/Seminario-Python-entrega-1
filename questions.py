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
    "sidney",
    "zurich",
    "lima",
    "santiago",
    "brasilia"
]

categories = {"comida": foods,
              "deportes": sports,
              "paises": countries,
              "ciudades" : cities
             }


#lol

print("¡Bienvenido al Ahorcado!")
print()

print("")

for elem in categories:
    print(elem," ")
while True:
    C = input("ingrese que categoria desea jugar: ")
    if C in categories:
        break
    print("categoria invalida")

rounds = 0
words = random.sample(categories[C], len(categories[C]))

while rounds<len(words):
    word = words[rounds]
    guessed = []
    attempts = 6
    points = 0
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
    R = int(input("ingrese 1 para salir o 2 para iniciar otra ronda: "))
    if (R == 1):
        break
    rounds += 1
if (rounds == len(words)):
    print("ya has jugado todas las palabras, gracias por jugar")
else:
    print("saliste del juego")