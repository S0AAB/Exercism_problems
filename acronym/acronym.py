def abbreviate(words):
    words=words.replace("-"," ")
    words=words.replace("´s","")
    words=words.replace("-"," ")
    words=words.replace("_"," ")

    words=words.split()
    salida=[]
    for i in range(len(words)):
        salida.append(words[i][0])

    return "".join(salida).upper()
    
    
    pass
