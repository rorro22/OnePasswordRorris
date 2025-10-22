numeros = [1,2,3,4,5,6,7,8,9,10]

pares = list(filter(lambda numero : numero % 2 == 0, numeros))
print(pares)



incrementados = list(map(lambda n : n + 10, numeros))
print(incrementados)


def filtrar_pares(nu):
    return list(filter(lambda n : n % 2 == 0, nu))

print(filtrar_pares(numeros))

u = "uriel"
f = u="beto"
print(f)