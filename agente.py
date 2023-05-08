import threading
import random

class Agente:
    def __init__(self):
        self.ingredientes = []
        self.sem = threading.Semaphore(1)

    def poner_ingredientes(self):
        self.sem.acquire()
        ing1, ing2, ing3, ing4 = self.generar_ingredientes()
        self.ingredientes.append(ing1)
        self.ingredientes.append(ing2)
        self.ingredientes.append(ing3)
        self.ingredientes.append(ing4)
        print(f'Agente ha puesto los ingredientes: {ing1}, {ing2}, {ing3} y {ing4}.')
        self.sem.release()

    def generar_ingredientes(self):
        ing1 = random.choice(['tabaco', 'papel', 'cerillas', 'filtros', 'green'])
        ing2 = random.choice(['tabaco', 'papel', 'cerillas', 'filtros', 'green'])
        ing3 = random.choice(['tabaco', 'papel', 'cerillas', 'filtros', 'green'])
        ing4 = random.choice(['tabaco', 'papel', 'cerillas', 'filtros', 'green'])
        #asegurate de que cada ing sea distinto de lo anterior y que no se repita
        while ing1 == ing2 or ing1 == ing3 or ing1 == ing4:
            ing1 = random.choice(['tabaco', 'papel', 'cerillas', 'filtros', 'green'])
        while ing2 == ing3 or ing2 == ing4:
            ing2 = random.choice(['tabaco', 'papel', 'cerillas', 'filtros', 'green'])
        while ing3 == ing4:
            ing3 = random.choice(['tabaco', 'papel', 'cerillas', 'filtros', 'green'])
        return ing1, ing2, ing3, ing4