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