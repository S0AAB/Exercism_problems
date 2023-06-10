def flatten(iterable):
    salida=[]
    result=funcion(iterable,salida)
    return result


    pass

def funcion(entrada,salida):
    for i in range (0,len(entrada)):
        if(entrada[i]!=None):
            if(isinstance(entrada[i],list)or isinstance(entrada[i],tuple)):
                funcion(entrada[i],salida)
            else:
                salida.append(entrada[i])
    return salida




