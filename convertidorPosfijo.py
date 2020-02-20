def PDP(dato):
    if(dato=="+" or dato=="-"):
        return 1
    elif(dato=="*" or dato=="/"):
        return 2
    elif(dato == "^"):
        return 3
    else:
        return 0

def PFP(dato):
    if(dato=="+" or dato=="-"):
        return 1
    elif(dato=="*" or dato=="/"):
        return 2
    else:
        return 4

pila = []
exp = [x.split() for x in open("expresiones.in.txt").readlines()][0]
lista=[]

print("Infijo: ")
print(exp)
print("postfijo: ")
def convertirPostfijo(exp):
    for i in range(len(exp)):
        if(exp[i].isdigit()):
            lista.append(str(exp[i]))
        if(exp[i] in "+-*/^("):
            if(pila):
                dato = pila.pop()
                while (pila and PDP(dato) >= PFP(exp[i])):
                    lista.append(str(dato))
                    dato = pila.pop()
                
                pila.append(dato)
                pila.append(exp[i])
            else:
                pila.append(exp[i])
        if (exp[i] == ")"):
           if (pila):
               dato = pila.pop()
               while(pila and dato != "("):
                   lista.append(str(dato))
                   dato = pila.pop()
    
    while pila:
        lista.append(str(pila.pop()))
    return (lista)    
        




