def find_anagrams(word, candidates):
    original=candidates.copy()
    listPalabra=[]
    salida=[]
    word=word.lower()

    
   
    for i in range (len(word)):
        listPalabra.append(word[i])

    for i in range(len(candidates)):
        candidates[i]=candidates[i].lower()

    if word in candidates:
        inde=candidates.index(word)
        candidates.remove(word)
        original.pop(inde)
           

    for i in range (0,len(candidates)):
        listaCand=[]
        for j in range (0,len(candidates[i])):
            listaCand.append(candidates[i][j])
        listaCand.sort()
        listPalabra.sort()
        if(listPalabra==listaCand):
            salida.append(original[i])
            


    return salida

    pass


print(find_anagrams("LISTEN",["LISTEN", "Silent"]))

