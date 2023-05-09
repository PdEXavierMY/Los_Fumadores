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