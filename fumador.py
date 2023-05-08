import time

class Fumador:
    def __init__(self, id, ing1, agente):
        self.id = id
        self.ing1 = ing1
        self.agente = agente

    def esperar_ingrediente(self):
        while True:
            self.agente.poner_ingredientes()
            print(self.agente.ingredientes)
            if self.ing1 not in self.agente.ingredientes:
                self.agente.sem.acquire()
                print(f'Fumador {self.id} con {self.ing1}, {self.agente.ingredientes[0]} y {self.agente.ingredientes[1]} está fumando...')
                self.agente.ingredientes.remove(self.ing1)
                self.agente.ingredientes.remove(self.ing2)
                time.sleep(2)
                self.agente.sem.release()