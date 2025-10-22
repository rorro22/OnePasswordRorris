import random
import os

os.system('cls')
print("Bienvenido a la Isla del tesoro\nTu misión es encontrar el tesoro.")
print("Estas caminando por la isla del tesoro y todo parece sacado de una fantasia, no entiendes que esta pasando pero tienes la sensación de que algo grande está por llegar.\nPero te encuentras con una desicion que tomar, el camino se divide y tu tienes que seguir tu intuición para cambiar tu vida con lo que puedes encontrar.")
decision = input("Izquierda o Derecha?\n:").lower()
if decision == "izquierda": 
    print("Despues de ir por el camino de la izquierda, tu estas muy emocionado porque empiezas a ver minerales y criaturas que no son del mundo real, pero parecen ser todos inofensivos y amigables\n de pronto llegas a un rio gigante y recuerdas que venias con un acompañante, pero, lo perdiste de vista...\n Puedes esperar a que llegue tu acompañante y entre los dos buscar la manera de cruzar o puedes comenzar a nadar o hacer cualquier cosa en el momento para intentar cruzar, que eliges? ")
    wait = input("nadar o esperar!\n:").lower()
    if wait == "esperar":
        print("Decides esperar y tu acomapañante aparece despues de 10 min, tiempo suficiente para que te sientas mas descansado, tu acompañante recuerda que tiene una balza inflable en su mochila y una bomba\n entre los dos comienzan a inflarla hasta que parece muy resistente, asi es que con unas ramas gruesas como remo\n comienzan a remar al otro lado del rio para aclamar eso que su intuicion les gritaba.\n Al poco tiempo, se encontraron con lo que parecia ser lo mas impresionante del lugar... 3 puertas inmensamente grandes frente a ti, una roja, una azul, y una amarilla, pero tu compañero encuentra una nota:\n 'Felicidades, estan a punto de encontrar el teso mas importante de toda esta isla, jamas nadie lo habia logrado encontrar ni superar las anteriores pruebas..\n Para esto debes superar la ultima prueba, debes seguir tu intuicion y elegir la puerta que sientas que mas te conviene, estas no se abriran amenos que griten el color de la puerta que desean al mismo tiempo y una fuerza extraña los jalara hacia adentro de esta para ver su contenido.'\n Asi es que terminando de leer la carta, deciden que diran al mismo tiempo que puerta abriran, pues, no necesariamente necesitan entrar juntos... puede ser que solo uno obtenga el premio.")
        yellow = input("Roja o Azul o Amarilla??\n:").lower()
        acompañante = random.choice(["roja", "azul", "amarilla"])
        print(f"Tu compañero eligio: {acompañante}")
        if yellow == "amarilla":
            print("Felicidades, lograste obtener todo el botin, tu intuicion es muy fuerte y buena, deberias confiar mas en ella")
        else:
            print(f"La puerta {yellow} no es la correcta, trabaja mas tu intuicion, estas muy cerca.")
    else:
        ("Al intentar nadar fuiste atacado por un grupo de serpientes nadadoras y uno que otro tiburón")
else:
    print("Haz muerto, deberias trabajar mas en tu intuicion.")