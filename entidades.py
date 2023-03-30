from asyncio.windows_events import NULL
import random
import math
from tkinter import SW
from unicodedata import numeric



class Fila:


    def __init__(self,probDeA, probDeB, probDeC, tiempoA, tiempoB, tiempoC, probDesperfecto, probDemora, tiempoDemora):
        
        self.probDeA = probDeA
        self.probDeB = probDeB
        self.probDeC = probDeC
        self.tiempoA = tiempoA
        self.tiempoB = tiempoB
        self.tiempoC = tiempoC
        self.probDesperfecto = probDesperfecto
        self.probDemora = probDemora
        self.tiempoDemora = tiempoDemora

        self.reloj = 0.0
        self.nroFila = 0
        self.rndLlegada = random.random()
        self.tiempoLlegada = self.getTiempoLlegada()
        self.rndDemora = random.random()
        self.existeDemora = self.getExisteDemora()
        self.rndDesperfecto = random.random()
        self.existeDesperfecto = self.getExisteDesperfecto()
        self.proxLlegada = self.getProxLlegada()
        self.acBuses = 0
        self.promEspera = False

        
        


    def proximaFila(self):
        if self.existeDesperfecto == False:
            self.acBuses += 1
        self.reloj = self.proxLlegada
        self.rndLlegada = random.random()
        self.tiempoLlegada = self.getTiempoLlegada()
        self.nroFila += 1
        self.rndDemora = random.random()
        self.existeDemora = self.getExisteDemora()
        self.rndDesperfecto = random.random()
        self.existeDesperfecto = self.getExisteDesperfecto()
        self.proxLlegada = self.getProxLlegada()
        if self.acBuses > 0:
            self.promEspera = (self.reloj / self.acBuses)
        else:
            self.promEspera = False
        self.existeDesperfecto = self.getExisteDesperfecto()

        return self

    def getTiempoLlegada(self):
        if  self.rndLlegada < (self.probDeA/100):
            return self.tiempoA

        elif self.rndLlegada < ((self.probDeB + self.probDeA )/100):
            return self.tiempoB
        else:
            return self.tiempoC
    
    def getExisteDemora(self):
        if self.rndDemora < (self.probDemora/100):
            return True
        else:
            return False
    
    def getExisteDesperfecto(self):
        if self.rndDesperfecto < (self.probDesperfecto / 100):
            return True
        else:
            return False
    
    def getProxLlegada(self):
        if self.existeDemora == True:
            x = self.reloj + self.tiempoLlegada + self.tiempoDemora
        else:
            x = self.reloj + self.tiempoLlegada
        return x    

    def convertirBoolean(self,x):
        if x == True:
            return "Si"
        else:
            return "No"

    def calcPromEspera(self):
        if (self.promEspera == False):
            return "N/A"
        else:
            return round(float(self.promEspera),2)

    def mostrarFila(self):
        return [self.nroFila, int(self.reloj), round(self.rndLlegada,2), int(self.tiempoLlegada), round(self.rndDemora,2), self.convertirBoolean(self.existeDemora),
                round(self.rndDesperfecto, 2), self.convertirBoolean(self.existeDesperfecto), int(self.proxLlegada), self.acBuses, self.calcPromEspera()]
        

