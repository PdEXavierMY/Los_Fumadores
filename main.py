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