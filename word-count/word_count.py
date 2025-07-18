import re

def count_words(sentence):
    salida=dict()
    cleanString = re.sub(r"[^a-zA-ZáéíóúÁÉÍÓÚñÑ0-9' ]",' ', sentence ) #Problemas con las comillas cuando son de una 'frase'

    cleanString =cleanString.lower()
    for word in cleanString.split():
        while(word.startswith("'") or word.endswith("'")):
            word=word.removeprefix("'")
            word=word.removesuffix("'")

        if (word==""):
            continue   
        if word not in salida.keys()  :
            salida[word]=1
        else:
            salida[word]=salida[word]+1
    return salida


    pass    

print(count_words("''hey''"))