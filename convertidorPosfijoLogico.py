def PDP(dato):
    if(dato=="^" or dato=="v"):
        return 1
    elif(dato=="->" or dato=="<->"):
        return 2
    elif(dato == "¬"):
        return 3
    else:
        return 0

def PFP(dato):
    if(dato=="^" or dato=="v"):
        return 1
    elif(dato=="->" or dato=="<->"):
        return 2
    else:
        return 4
def convertirPostfijo(exp):
    pila = []
    for i in range(len(exp)):
        print(pila)
        if(exp[i] in ["p","q","r"]):
            lista.append(str(exp[i]))
        if(exp[i] in ["¬","^","v","->","<->", "("]):
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

exp = [x.split() for x in open("expresiones.in.txt").readlines()][0]
lista=[]

print("Infijo: ")
print(exp)
print("postfijo: ")
print(convertirPostfijo(exp))

        
