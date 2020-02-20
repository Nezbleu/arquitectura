def contarVariables(expresion):
    contador=[]
    for letra in expresion:
        if (letra in ["p","q","r"]) and (letra not in contador):
            contador.append(letra)
    return len(contador)

def crearBaseTablasVerdad(expresion):
    tablas=[]
    if(contarVariables(expresion) == 1):
        tablas = [["True","False"]]
    elif(contarVariables(expresion) == 2):
        tablas = [["True","True","False","False"],["True","False","True","False"]]
    elif(contarVariables(expresion) == 3):
        tablas = [["True","True","True","True","False","False","False","False"],
         ["True","True","False","False","True","True","False","False"],
         ["True","False","True","False","True","False","True","False"]]
    return (tablas)

def remplazarExpresion(expresion, remplazo, cantVar):
    for i in range(len(expresion)):
        if (expresion[i] == "p"):
            expresion[i] = remplazo[0]
        elif (expresion[i] == "q"):
            expresion[i] = remplazo[1]
        elif (expresion[i] == "r"):
            expresion[i] = remplazo[2]
    return expresion

def crearTablasParametricamente(expresion):
    resultado = []
    tablas = crearBaseTablasVerdad(expresion)
    cantVar = contarVariables(expresion)
    print(tablas)
    
    for i in range(2**(cantVar)):
        if cantVar==1:
            resultado.append( remplazarExpresion(expresion, [tablas[0][i]], cantVar) )
        elif cantVar==2:
            resultado.append( remplazarExpresion(expresion, [tablas[0][i], tablas[1][i]], cantVar) )            
        elif cantVar==3:
            resultado.append( remplazarExpresion(expresion, [tablas[0][i], tablas[1][i], tablas[2][i]], cantVar) )
        
def crearTablas():
    resultado = []
    tablas = crearBaseTablasVerdad([x.split() for x in open("expresiones.in.txt").readlines()][0])
    cantVar = contarVariables([x.split() for x in open("expresiones.in.txt").readlines()][0])
    print(tablas)
    
    for i in range(2**(cantVar)):
        if cantVar==1:
            resultado.append( remplazarExpresion([x.split() for x in open("expresiones.in.txt").readlines()][0], [tablas[0][i]], cantVar) )
        elif cantVar==2:
            resultado.append( remplazarExpresion([x.split() for x in open("expresiones.in.txt").readlines()][0], [tablas[0][i], tablas[1][i]], cantVar) )            
        elif cantVar==3:
            resultado.append( remplazarExpresion([x.split() for x in open("expresiones.in.txt").readlines()][0], [tablas[0][i], tablas[1][i], tablas[2][i]], cantVar) )
    return resultado

print(crearTablas())

