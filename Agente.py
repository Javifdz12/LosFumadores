import threading
import random

class Agente(threading.Thread):
    sem=threading.Lock()
    def __init__(self,utensilios):
        self.utensilios = utensilios
        threading.Thread.__init__(self)
        self.mesa=[]
    def desbloquear_ings(self):
        for ing in self.utensilios:
            if ing.sem.locked()==True:
                ing.soltar()
    def cambiar_mesa(self):
        self.desbloquear_ings()
        self.mesa=[]
        x=random.choice(self.utensilios)
        for i in self.utensilios:
            if i!=x:
                self.mesa.append(i)
        print(f'Mesa cambiada:{self.mesa}')
    def comp_mesa(self):
        x=0
        for i in self.utensilios:
            if i.sem.locked()==True:
                x+=1
            else:pass
        return x
    def bloquear_ings(self):
        for i in self.utensilios:
            i.coger()
    def run(self):
        self.bloquear_ings()
        while True:
            if self.comp_mesa()>=len(self.mesa):
                self.cambiar_mesa()