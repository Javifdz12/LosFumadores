import threading

class Ingrediente:
    def __init__(self,nombre):
        self.nombre = nombre
        self.sem=threading.Lock()
    def coger(self):
        self.sem.acquire()
    def soltar(self):
        self.sem.release()
