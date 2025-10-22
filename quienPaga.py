import random

friends = []

print("Esta es la ruleta amigos, elegira al azar una persona de los nombre introducidos por usted a continuacion y esa persona sera la designada a pagar")

n = int(input("Cuantas personas son las que participaran ?\n"))

for p in range(n):
    nombre = input(f"Nombre del jugador {p+1}: ")
    friends.append(nombre)

print(friends, "estan participando por ver quien pagara la cuenta esta noche!")
elegido = random.choice(friends)
print(f"El ganador es: {elegido}")