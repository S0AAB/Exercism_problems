
SUBLIST = "SUBLISTA"
SUPERLIST ="SUPERLISTA"
EQUAL = "IGUAL"
UNEQUAL = "NO IGUAL"

def pasarSTR(lista):
    salida=""
    for i in range(0,len(lista)):
        salida=salida+str(lista[i])
        salida=salida+"-"
    return salida

def sublist(list_one, list_two):
    l1=pasarSTR(list_one)
    l2=pasarSTR(list_two)

    if(l1 == l2):
        return EQUAL
    elif(l1 in l2 ):
        return SUBLIST
    elif ( l2 in l1 ):
        return SUPERLIST
    else:
        return UNEQUAL
    pass


