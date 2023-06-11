def commands(binary_str):
    salida=[]
    if(binary_str[4]=="1"):
        salida.append("wink")
    if(binary_str[3]=="1"):
        salida.append("double blink")
    if(binary_str[2]=="1"):
        salida.append("close your eyes")
    if(binary_str[1]=="1"):
        salida.append("jump")
    if(binary_str[0]=="1"):
        salida.reverse()
    
    return salida

    pass
