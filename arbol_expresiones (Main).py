from pila import *
from arbol import *
import os

def convertir(lista, pila):
    if lista != []:
        if (lista[0] in ["^","v","->","<->"]):
            nodo_der = pila.desapilar()
            nodo_izq = pila.desapilar()
            pila.apilar(Nodo(lista[0],nodo_izq,nodo_der))
        elif (lista[0] in ["¬"]):
            
            nodo_izq = pila.desapilar()
            pila.apilar(Nodo(lista[0],nodo_izq))
            
        else:
            pila.apilar(Nodo(lista[0]))
        return convertir(lista[1:],pila)
            

def evaluar(arbol):
    if arbol.valor == "^":
        return evaluar(arbol.izq) and evaluar(arbol.der)
    if arbol.valor == "^":
        return evaluar(arbol.izq) and evaluar(arbol.der)
    if arbol.valor == "v":
        return evaluar(arbol.izq) or evaluar(arbol.der)
    if arbol.valor == "->":
        return not(evaluar(arbol.izq)) or evaluar(arbol.der)
    if arbol.valor == "<->":
        return (not(evaluar(arbol.izq)) or evaluar(arbol.der)) and (not(evaluar(arbol.der)) or evaluar(arbol.izq))
    if arbol.valor == "¬":
        return not(evaluar(arbol.izq))
    return eval(arbol.valor)

def leerArchivo():
    return[x.split() for x in open("expresiones.in.txt").readlines()]
    
lista = leerArchivo()

file = open("expresiones.out.txt", "w")

for i in range(0, len(lista)):
    pila = Pila()
    convertir(lista[i], pila)
    salida=str(evaluar(pila.desapilar()))
    file.write(salida + os.linesep)
    
file.close()


