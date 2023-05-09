# Los_Fumadores

Pincha [aquí](https://github.com/Xavitheforce/Los_Fumadores) para dirigirte a mi repositorio.

En esta entrega se resuelve en python el problema de los fumadores cuyo enunciado es:

'El caso de los fumadores consiste en un grupo de fumadores que para fumar necesitan los ingredientes que les faltan para hacer un cigarrillo y fumárselo, poseen un ingrediente en cantidades ilimitadas pero les faltan otros cuatro.

El agente posee cantidades ilimitadas de todos los ingredientes que son papel, tabaco, filtros, green y cerillas pero solo deja en una mesa un número determinado de estos ingredientes a la vez. Cada fumador posee un ingrediente distinto de los cinco necesarios y según los ingredientes que deje el agente uno de los fumadores podrá fumar con los cuatro ingredientes que el agente deja.

El agente y los fumadores representan en la realidad a procesos y los ingredientes a los recursos de un sistema. La dificultad radica en sincronizar los agentes y fumadores para que el agente cuando deje ingredientes en la mesa el fumador correcto fume.'

Esta entrega consta de 3 archivos de python que son: el que maneja el comportamiento del agente, el que reproduce el comportamiento de los fumadores y el main.

El código realizado para el agente es:

```python
import threading
import random

class Agente:
    def __init__(self):
        self.ingredientes = []
        self.sem = threading.Semaphore(1)

    def poner_ingredientes(self):
        self.sem.acquire() # Para que el agente no ponga los ingredientes mientras el fumador está fumando
        ing1, ing2, ing3, ing4 = self.generar_ingredientes()
        self.ingredientes.append(ing1)
        self.ingredientes.append(ing2)
        self.ingredientes.append(ing3)
        self.ingredientes.append(ing4)
        print(f'Agente ha puesto los ingredientes: {ing1}, {ing2}, {ing3} y {ing4}.')
        self.sem.release()

    def generar_ingredientes(self):
        lista = ['tabaco', 'papel', 'cerillas', 'filtros', 'green']
        elementos_aleatorios = random.sample(lista, k=4) # k=4 y sample para que no se repitan los elementos
        ing1 = elementos_aleatorios[0]
        ing2 = elementos_aleatorios[1]
        ing3 = elementos_aleatorios[2]
        ing4 = elementos_aleatorios[3]
        return ing1, ing2, ing3, ing4     
```

El código realizado para los fumadores es:

```python
import time

class Fumador:
    def __init__(self, id, ing1, agente):
        self.id = id
        self.ing1 = ing1
        self.agente = agente

    def esperar_ingrediente(self):
        while True: # El fumador está esperando a que el agente ponga los ingredientes
            if self.ing1 not in self.agente.ingredientes and len(self.agente.ingredientes) == 4: # Si el fumador no tiene el ingrediente que le falta y el agente ha puesto los 4 ingredientes
                self.agente.sem.acquire()
                print(f'Fumador {self.id} con todos los ingredientes está fumando...')
                self.agente.ingredientes.clear()
                time.sleep(2)
                print(f'Fumador {self.id} ha terminado de fumar.')
                self.agente.sem.release()   
```

Finalmente el main que controla la simulación del problema es:

```python
import threading
import time
from agente import Agente
from fumador import Fumador

class Simulacion:
    def __init__(self):
        self.agente = Agente()
        self.fumadores = [Fumador('1', 'tabaco', self.agente), Fumador('2', 'papel', self.agente), Fumador('3', 'cerillas', self.agente), Fumador('4', 'filtros', self.agente), Fumador('5', 'green', self.agente)]

    def iniciar(self):
        for fumador in self.fumadores:
            threading.Thread(target=fumador.esperar_ingrediente).start()

        while True:
            self.agente.poner_ingredientes()
            time.sleep(2)

if __name__ == '__main__':
    simulacion = Simulacion()
    simulacion.iniciar()
```

Ahora vamos a ver la salida por terminal del main:

![Output](https://user-images.githubusercontent.com/91721699/237041583-d3745a7b-f061-4a0e-9e19-797d98ade417.png)

Este proceso de fumar seguiría constante describiendo como debería comportarse cada fumador según los ingredientes disponibles y los depositados por el agente.
