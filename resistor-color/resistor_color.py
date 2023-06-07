resistors={"black":0,"brown":1,"red":2,"orange":3,"yellow":4,"green":5,"blue":6,"violet":7,"grey":7,"white":9}

def color_code(color):
    colorValue=resistors.get(color)
    return colorValue
    pass


def colors():
    lista=[]
    for k, v in resistors.items():
        lista.append(k)
    return lista

print(colors())
