import time

class Fumador:
    def __init__(self, id, ing1, agente):
        self.id = id
        self.ing1 = ing1
        self.agente = agente

    def esperar_ingrediente(self):
        while True:
            if self.ing1 not in self.agente.ingredientes and len(self.agente.ingredientes) == 2:
                self.agente.sem.acquire()
                print(f'Fumador {self.id} con todos los ingredientes está fumando...')
                self.agente.ingredientes.clear()
                time.sleep(2)
                print(f'Fumador {self.id} ha terminado de fumar.')
                self.agente.sem.release()