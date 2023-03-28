import random
listaMiast = ["Warszawa", "Sopot", "Wroclaw", "Lodz", "Lublin",
              "Gdansk", "Gdynia", "Krakow", "Poznan", "Bialystok"]

index = random.randint(0, len(listaMiast) - 1)
print("Miasto docelowe to " + str(listaMiast[index]))