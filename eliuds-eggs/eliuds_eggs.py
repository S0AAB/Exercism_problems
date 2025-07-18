def egg_count(display_value):
    resultado=[]

    while display_value !=0:
        resto= display_value % 2
        display_value= display_value // 2
        resultado.append(resto)

    resultado.reverse()
    return resultado.count(1)
    


