import threading
import time
from agente import Agente
from fumador import Fumador

class Simulacion:
    def __init__(self):
        self.agente = Agente()
        self.fumadores = [Fumador('1', 'tabaco', self.agente), Fumador('2', 'papel', self.agente), Fumador('3', 'cerillas', self.agente)]

    def iniciar(self):
        self.agente.poner_ingredientes()
        for fumador in self.fumadores:
            threading.Thread(target=fumador.esperar_ingrediente).start()
        while True:
            time.sleep(2)
            self.agente.poner_ingredientes()

simulacion = Simulacion()
simulacion.iniciar()