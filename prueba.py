lista1=[1,2,5]
lista2=[0, 1, 2, 3, 1, 2, 5, 6]

def pasarSTR(lista):
    salida=""
    for i in range(0,len(lista)):
        salida=salida+str(lista[i])
    return salida

l1=pasarSTR(lista1)
l2=pasarSTR(lista2)
    
if l1 in l2:
    print ("SISTA")
else:
    print ("NOSTA")