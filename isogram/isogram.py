def is_isogram(jaja):
    string=jaja.replace(" ","")
    string=string.replace("-","")
    string=string.lower()
    x=False
    for i in range (0,len(string)):
        if(string.count(string[i])>1):
             x=False
             break
        else:
            x=True
    if(x==True or len(jaja)==0):
        return True
    else:
        return False
    pass


print (is_isogram("lumberjacks"))
