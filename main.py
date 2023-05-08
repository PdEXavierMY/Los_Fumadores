import threading
import time
from agente import Agente
from fumador import Fumador

class Simulacion:
    def __init__(self):
        self.agente = Agente()
        self.fumadores = [Fumador('1', 'tabaco', self.agente), Fumador('2', 'papel', self.agente), Fumador('3', 'cerillas', self.agente)]
        self.num_cigarros = {fumador.id: 0 for fumador in self.fumadores}

    def iniciar(self):
        for fumador in self.fumadores:
            threading.Thread(target=fumador.esperar_ingrediente).start()

        while (num < 10 for num in self.num_cigarros.values()):
            self.agente.poner_ingredientes()
            time.sleep(2)
            self.num_cigarros[fumador.id] += 1

        time.sleep(2)
        print("Todos los fumadores han fumado 10 veces. La simulación ha terminado.")

simulacion = Simulacion()
simulacion.iniciar()