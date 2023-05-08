import threading
import random

class Agente:
    def __init__(self):
        self.ingredientes = []
        self.sem = threading.Semaphore(1)

    def poner_ingredientes(self):
        self.sem.acquire()
        ing1, ing2 = self.generar_ingredientes()
        self.ingredientes.append(ing1)
        self.ingredientes.append(ing2)
        print(f'Agente ha puesto los ingredientes: {ing1} y {ing2}')
        self.sem.release()

    def generar_ingredientes(self):
        ing1 = random.choice(['tabaco', 'papel', 'cerillas'])
        ing2 = random.choice(['tabaco', 'papel', 'cerillas'])
        while ing1 == ing2:
            ing2 = random.choice(['tabaco', 'papel', 'cerillas'])
        return ing1, ing2