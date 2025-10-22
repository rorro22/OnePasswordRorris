import random

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
simbolos = [' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
numeros = [str(n) for n in range(0,100)]

passw = int(input("Que tan extensa quieres que sea tu contraseña, de cuantos caracteres ?"))

let = int(input("Cuantas letras quieres que contenga?"))
sim = int(input("Cuantos simbolos quieres que contenga ??"))
num = int(input("Cuantos numeros ??"))

secure = []
for n in random.sample(numeros,num):
    secure.append(n)

for l in random.sample(letras,let):
    secure.append(l)

for s in random.sample(simbolos,sim):
    secure.append(s)

random.shuffle(secure)
bestPass = ''.join(secure)
print(bestPass)
