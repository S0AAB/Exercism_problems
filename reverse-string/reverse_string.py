def reverse(text):
    texto=""
    for i in range (1,len(text)+1):
        texto=texto+text[-i]
    return texto
    passs