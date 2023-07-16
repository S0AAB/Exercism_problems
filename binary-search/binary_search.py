def find(search_list, value):
    izq=0
    der=len(search_list)-1
    if(value not in search_list):
       raise ValueError("value not in array")
    
    while izq<=der:
        medio=(izq+der)//2

        if(search_list[medio]==value):
            return medio
        if(search_list[medio]>value):
            der=medio-1
        if(search_list[medio]<value):
            izq=medio+1

    pass


