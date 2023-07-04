resistors={"black":0,"brown":1,"red":2,"orange":3,"yellow":4,"green":5,"blue":6,"violet":7,"grey":8,"white":9}
tolerance={"grey":0.05,"violet":0.1,"blue":0.25,"green":0.5,"brown":1,"red":2,"gold":5,"silver":10}


def value(colors):
    salida=""
    if len(colors)==4:
        for i in range(0,2):
            salida+=str(resistors.get(colors[i]))
    if len(colors)==5:
        for i in range(0,3):
            salida+=str(resistors.get(colors[i]))

    salida=salida[0:len(colors)-1]
    return int(salida)
    pass


def label(colors):
    if len(colors) ==5:
        numCeros=resistors.get(colors[3])
    else:
        numCeros=resistors.get(colors[2])
    valor=value(colors)
   
    
    valor=valor*10**numCeros

    prefix=""

    if(valor/(10**9)<=100 and valor/(10**9)>1):
    
        valor=valor/10**9
        prefix="giga"
    elif(valor/(10**6)<=100 and valor/(10**6)>1):
       
        valor=valor/10**6
        prefix="mega"
    elif(valor/(10**3)<=100 and valor/(10**3)>1):
        
        valor=valor/10**3
        prefix="kilo"
    
    x=str(valor).split(".")
    try:
        if (int(x[1])==0):
            valor=int(valor)
    except:
        valor=valor

    
    salida=str(valor)+" "+prefix+"ohms"
    return salida

    pass


def resistor_label(colors):
    if(len(colors)<4):
        return "0 ohms"
    if len(colors)==5:
        tolerancia=tolerance.get(colors[4])
    else:
        tolerancia=tolerance.get(colors[3])
    valor=label(colors)
    valor+=" ±"+str(tolerancia)+"%"
    return valor
    
    pass

