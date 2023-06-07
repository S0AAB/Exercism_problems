def convert(number):
    salida=""
    if(number%3==0):
        salida=salida+"Pling"
    if(number%5==0):
        salida=salida+"Plang"
    if(number%7==0):
        salida=salida+"Plong"

    if(number%3!=0 and number%5!=0 and number%7!=0):
        salida=str(number)
    
    return salida
    pass