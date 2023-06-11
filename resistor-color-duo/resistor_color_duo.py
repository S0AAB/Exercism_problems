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



