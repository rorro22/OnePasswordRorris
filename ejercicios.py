def primos(maximo):
    """Ejercicio de obtener numeros primos con una funcion generadora del 0 al 100"""
    for numero in range(2,maximo+1):
        for divisor in range(2, numero):
            if numero % divisor == 0:
                break
        else:
            yield numero


print("funcion generadora de primos")
for n in primos(100):
    print(n)


def generar_pares(inicio, fin):
    for n in range(inicio, fin+1):
        if n >=2:
            if n % 2 == 0:
                yield n
                

inicio = 1
fin = 10
print(f"Números pares en el rango [{inicio}, {fin}]:")
for numero in generar_pares(inicio, fin):
    print(numero)