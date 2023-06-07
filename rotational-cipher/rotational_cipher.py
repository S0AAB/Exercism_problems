def rotate(text, key):
    salida=""
    abc= "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    


    for i in range(0,len(text)):
        if(text[i].isalpha()==True):
            if(text[i]==" "):
                salida=salida+" "
                continue
            esMayus=False
            if(text[i].isupper()==True):
                esMayus=True
                
            aux=text.lower()

            salida=salida+abc[abc.index(aux[i])+key]
            if(esMayus==True):
                salida=salida.replace(salida[i],salida[i].upper())
            print(salida)
        else:
            salida=salida+text[i]
            print(salida)

    return salida
    pass


