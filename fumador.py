import time

class Fumador:
    def __init__(self, id, ing1, agente, fumado=False):
        self.id = id
        self.ing1 = ing1
        self.agente = agente

    def esperar_ingrediente(self):
        while True:
            if self.ing1 not in self.agente.ingredientes:
                self.agente.sem.acquire()
                print(f'Fumador {self.id} con {self.ing1}, {self.agente.ingredientes[0]} y {self.agente.ingredientes[1]} está fumando...')
                self.agente.ingredientes.remove(self.agente.ingredientes[0])
                self.agente.ingredientes.remove(self.agente.ingredientes[0])
                time.sleep(2)
                self.agente.sem.release()
                print(f'Fumador {self.id} ha terminado de fumar.')
                self.fumado = True
                return self.fumado