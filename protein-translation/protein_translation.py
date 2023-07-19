c_p={"AUG":"Methionine","UUU":"Phenylalanine","UUC":"Phenylalanine","UUA":"Leucine","UUG":"Leucine","UCU":"Serine","UCC":"Serine","UCA":"Serine","UCG":"Serine","UAU":"Tyrosine","UAC":"Tyrosine","UGU":"Cysteine","UGC":"Cysteine","UGG":"Tryptophan","UAA":"STOP","UAG":"STOP","UGA":"STOP"    }
def proteins(strand):
    salida=[]
    a=0
    b=3
    bandera=False
    for i in range (0,len(strand),3):
        if(bandera==True):
            break
        vec=strand[a:b] 
      
        for k,v in c_p.items():
            
            if k in vec:
                if(v!="STOP"):
                    salida.append(v)
                else:
                    bandera=True
                    break
        a+=3
        b+=3    

    return salida
    pass

