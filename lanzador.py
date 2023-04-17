from Ingrediente import Ingrediente
from Fumador import *
from Agente import Agente

def lanzar():
    ing1=Ingrediente('tabaco')
    ing2=Ingrediente('papel')
    ing3=Ingrediente('filtros')
    ing4=Ingrediente('cerillas')
    ing5=Ingrediente('green')
    utensilios=[ing1,ing2,ing3,ing4,ing5]

    agente=Agente(utensilios)
    fumador1=Fumador('javi',agente)
    fumador2=Fumador('pepe',agente)
    fumador3=Fumador('alonso',agente)
    fumador4=Fumador('santiago',agente)
    fumador5=Fumador('alfonso',agente)
    fumadores=[fumador1,fumador2,fumador3,fumador4,fumador5]

    agente.start()
    time.sleep(1)
    for fumador in fumadores:
        fumador.start()
    agente.join()



