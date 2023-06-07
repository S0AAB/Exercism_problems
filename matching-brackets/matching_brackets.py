def sonPares(input_string):
    cont1=input_string.count("{") + input_string.count("}")
    cont2=input_string.count("(") + input_string.count(")")
    cont3=input_string.count("[") + input_string.count("]")

    if((cont1 == 0 or cont1%2 ==0) and (cont2 == 0 or cont2%2 ==0) and (cont3 == 0 or cont3%2 ==0)):
        return True
    else:
        return False

def siCierra(input_string):
    
    if(len(input_string)>=2):
        if(len(input_string)==0):
            return True
        elif(input_string[0]== "(" and input_string[1]==")"):
            salida=input_string[2:len(input_string)]
            return salida
        elif((input_string[0]== "(" and input_string[len(input_string)-1]==")") and len(input_string)>2):
            salida=input_string[1:len(input_string)-1]
            return salida

        elif(input_string[0]== "[" and input_string[1]=="]"):
            salida=input_string[2:len(input_string)]
            return salida
        elif((input_string[0]== "[" and input_string[len(input_string)-1]=="]") and len(input_string)>2):
            salida=input_string[1:len(input_string)-1]
            return salida    


        elif(input_string[0]== "{" and input_string[1]=="}"):
            salida=input_string[2:len(input_string)]
            return salida
        elif((input_string[0]== "{" and input_string[len(input_string)-1]=="}") and len(input_string)>2):
            salida=input_string[1:len(input_string)-1]
            return salida
        
        
        else:
            return False
    else:
        return False
def limpiar(entrada):
    salida=""
    characters = "(){}[]"

    for x in range(0,len(entrada)):
        if(entrada[x] in characters):
            salida=salida+entrada[x]

    salida=salida.replace(" ", "")
    return salida
    
def is_paired(input_string):
    xd=limpiar(input_string)
    alv=True
    
    
    while(len(xd)!=0 ):
        
        xd=siCierra(xd)
        if(xd==False ):
            alv=False
            break
           
        else:
            alv=True
            
           
                    
  

    if(sonPares(input_string)==True and alv==True or input_string==""):
        return True
    else:
        return False
      

   
    pass
