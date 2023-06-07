


def palindromo (numero):
    numero =str (numero)
    numero2=numero[::-1]
    
    if(numero == numero2):
        return True
    else:
        return False
            
    pass

def smallest(min_factor, max_factor):
    if(min_factor>max_factor ):
        raise ValueError("min must be <= max")
    else:
        lista= []
        salida=[]
        multiplos=[]
        for i in range (min_factor,max_factor+1):
            lista.append(i)
        for i in range (0,len(lista)):
            for j in range (0,len(lista)):
                xd=lista[i]*lista[j]
                if(palindromo(xd)==True):
                    if(xd not in salida):
                        multiplos.append([lista[i],lista[j]])
                        salida.append(xd)
        if(len(salida) >=1 ):
            return salida[0],multiplos[0]
        
            

    pass



def largest(min_factor, max_factor):
    if(min_factor>max_factor or min_factor==max_factor):
        raise ValueError("min must be <= max")
    else:
        lista= []
        salida=[]
        multiplos=[]
        for i in range (min_factor,max_factor+1):
            lista.append(i)
        for i in range (0,len(lista)):
            for j in range (0,len(lista)):
                xd=lista[i]*lista[j]
                if(palindromo(xd)==True):
                    if(xd not in salida):
                        multiplos.append([lista[i],lista[j]])
                        salida.append(xd)
        if(len(salida)>=1 ):         
            return salida[-1],multiplos[-1]
        else:
            return salida.clear(),multiplos.clear()
       
        

    pass




