abc="abcdefghijklmnopqrstuvwxyz"
cipher="zyxwvutsrqponmlkjihgfedcba"

def encode(plain_text):
   
    encode=""
    plain_text=plain_text.lower()
    plain_text=plain_text.replace(" ","")
    plain_text=plain_text.replace(",","")
    plain_text=plain_text.replace(".","")
    for i in range (0,len(plain_text)):
        if(plain_text[i].isnumeric()==True):
            encode+=plain_text[i]
        else:
            encode+=cipher[abc.index(plain_text[i])]
    salida=""
    bandera=1
    for i in range (0,len(encode)):
        
        salida+=encode[i]
        if(bandera%5==0):
            salida+=" "
            bandera=0
        bandera+=1
    if(salida.endswith(" ")):
        salida=salida[0:len(salida)-1]
    return salida
    pass



def decode(ciphered_text):
    ciphered_text=ciphered_text.replace(" ","")
    decode=""
    for i in range (0,len(ciphered_text)):
        if(ciphered_text[i].isnumeric()==True):
            decode+=ciphered_text[i]
        else:
            decode+=abc[cipher.index(ciphered_text[i])]
    return decode
    pass


