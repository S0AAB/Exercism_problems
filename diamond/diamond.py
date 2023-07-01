def rows(letter):
    if(letter=="A"):return ["A"]
    abc="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letras=abc[0:abc.index(letter)+1]
    
    n=abc.index(letter)
    h=0
    ch=" "
    cuerpo=[]
    for letra in letras:
        if(h==0):
            cuerpo.append(ch*n+letra+n*ch)
        else:
            cuerpo.append(ch*n+letra+((h*2)-1)*ch+letra+n*ch)
        h+=1
        n-=1
    h=abc.index(letter)
    n=1
    for letra in letras[-2::-1]:
        if(letra=="A"):
            cuerpo.append(ch*n+letra+n*ch)
        else:
            cuerpo.append(ch*n+letra+((h*2)-3)*ch+letra+n*ch)
        h-=1
        n+=1
        
    return cuerpo
    pass

