import threading
import random
import time

ings_fumadores=[]

class Fumador(threading.Thread):
    def __init__(self,nombre,agente):
        self.agente = agente
        threading.Thread.__init__(self)
        self.nombre=nombre
        self.ings=[]
        ing=random.choice(self.agente.utensilios)
        while ing in ings_fumadores:
            ing=random.choice(self.agente.utensilios)
        else:
            ings_fumadores.append(ing)
            self.ing=ing
            self.ings.append(self.ing)
    def actuar(self):
        for ing in self.agente.mesa:
            if ing.sem.locked()==False:
                if ing not in self.ings:
                    print(f'el fumador {self.nombre} va a coger algo de la mesa')
                    print(f'el fumador {self.nombre} ha cogido {ing.nombre}')
                    self.ings.append(ing)
                    self.ingredientes()
                    ing.coger()
                    time.sleep(1)
                else:
                    pass
            else:
                pass
    def ingredientes(self):
        print(f'Ings {self.nombre}:')
        print('-------')
        for ing in self.ings:
            print(f'{ing.nombre}')
        print('-------')
    def run(self):
        while len(self.ings)<5:
            self.actuar()
        else:
            pass