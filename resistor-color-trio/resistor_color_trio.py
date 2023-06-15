resistors={"black":0,"brown":1,"red":2,"orange":3,"yellow":4,"green":5,"blue":6,"violet":7,"grey":8,"white":9}

def color_code(color):
    colorValue=resistors.get(color)
    return colorValue
    pass

def value(colors):
    salida=""
    for i in range(0,len(colors)):
        salida+=str(color_code(colors[i]))

    salida=salida[0:2]
    return int(salida)
    pass


def label(colors):
    numCeros=resistors.get(colors[2])
    valor=value(colors)
    valor2=value(colors)
    
    for i in range(numCeros):
        valor=valor*10

    prefix=""

    if(valor%(10**9)==0 and valor!=0):
        valor=valor//10**9
        prefix="giga"
    elif(valor%(10**6)==0 and valor!=0):
        valor=valor//10**6
        prefix="mega"
    elif(valor%(10**3)==0 and valor!=0):
         valor=valor//10**3
         prefix="kilo"
    salida=str(valor)+" "+prefix+"ohms"
    return salida

    pass

print(label(["yellow", "violet", "yellow"]))