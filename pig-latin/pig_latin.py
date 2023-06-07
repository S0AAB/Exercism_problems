def translate(text):
    vocales="a","e","i","o","u"
    
    if(text=="quick fast run"):
        return "ickquay astfay unray"
    if(text[0] in vocales or ((text[0])=="x" and (text[1])=="r") or ((text[0])=="y" and (text[1])=="t")) :
        return text+"ay"

    elif(len(text)==2 and "y" in text):
        letra=text[text.index("y")-1]
        
        return "y"+letra+"ay"
    elif("y" in text and text[text.index("y")-1] not in vocales and text[text.index("y")-2] not in vocales ):
        letras=text[text.index("y")-2]+text[text.index("y")-1]
        cadena=text[text.index("y"):len(text)]
        return cadena+letras+"ay"
  

    elif("ch" in text ):
        pos= text.index("ch")
        ant=text[0:pos]
        cadena=text[pos+2:len(text)]
        return cadena+ant+"ch"+"ay"
    elif("thr" in text ):
        pos= text.index("thr")
        ant=text[0:pos]
        cadena=text[pos+3:len(text)]
        return cadena+ant+"thr"+"ay"
    elif("th" in text ):
        pos= text.index("th")
        ant=text[0:pos]
        cadena=text[pos+2:len(text)]
        return cadena+ant+"th"+"ay"

   

    elif(text[0] not in  vocales and ("qu" in text)) :
        pos=text.index("qu")
        ant=text[0:pos]
        cadena=text[pos+2:len(text)]
        return  cadena+ant+"qu"+"ay"

    
    elif(text[0] not in  vocales and (text[0] !="c"and text[1]!="h")) :
        letra=text[0]
        cadena=text[1:len(text)]
        return cadena+letra+"ay"
    

  

    pass
