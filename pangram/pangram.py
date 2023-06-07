def is_pangram(sentence):
    
    abc= 'abcdefghijklmnopqrstuvwxyz'
    a=sentence.replace(" ","")
    a=a.lower()
    largo=len(a)
    
    
    for i in range (0,largo):
        
        if(a[i] in abc):
            abc=abc.replace(a[i],"")
            print(abc)
    if(len(abc)==0):
        return True 
    else:
        return False
    pass


