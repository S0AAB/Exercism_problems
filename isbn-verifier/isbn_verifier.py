def is_valid(isbn):
    numeros= isbn.replace("-","")
    salida=False
    largo=len(numeros)
    try:
        if(largo<10 or largo>=11):
            return False
        elif("X"in numeros):
            numeros=numeros.replace("X","")
            
            if((int(numeros[0])*10+int(numeros[1])*9+int(numeros[2])*8+int(numeros[3])*7+int(numeros[4])*6+int(numeros[5])*5+int(numeros[6])*4+int(numeros[7])*3+int(numeros[8])*2+10*1)%11==0):
                return True
            else:
                return False
        elif("X" not in numeros):
            if((int(numeros[0])*10+int(numeros[1])*9+int(numeros[2])*8+int(numeros[3])*7+int(numeros[4])*6+int(numeros[5])*5+int(numeros[6])*4+int(numeros[7])*3+int(numeros[8])*2+int(numeros[9])*1)%11==0):
                return True
            else:
                return False
        else:
            return False
    except:
        return False
   
    
    pass

print(is_valid("3598215078X"))
