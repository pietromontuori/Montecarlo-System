import copy
from math import sqrt
import entidades as entity



def empezarSimulacion(probDeA, probDeB, probDeC, tiempoA, tiempoB, tiempoC, probDesperfecto, probDemora, tiempoDemora):
    global fila
    fila = entity.Fila(probDeA, probDeB, probDeC, tiempoA, tiempoB, tiempoC, probDesperfecto, probDemora, tiempoDemora)
    salida = mostrarFila(fila.mostrarFila())
    return salida

def mostrarFila(v):
     temp = copy.deepcopy(v)
     return temp
    

def calcularSiguienteFila():
    global fila
    fila = fila.proximaFila()
    temp = mostrarFila(fila.mostrarFila())
   
    return temp
