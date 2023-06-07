def square_of_sum(number):
    x=0
    for i in range (0,number+1):
        x=x+i;
    
    salida=x**2
    return salida
    pass



def sum_of_squares(number):
    x=0
    for i in range (0,number+1):
        x=x+(i**2)

    return x
    pass
   


def difference_of_squares(number):

    return (square_of_sum(number)-sum_of_squares(number))
    pass
