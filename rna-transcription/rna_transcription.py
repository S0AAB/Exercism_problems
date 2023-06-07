def to_rna( dna_strand):
    salida=""
 
    for i in range(0,len(dna_strand)):
        if(dna_strand[i]=="G"):
            salida+="C"
        if(dna_strand[i]=="C"):
            salida+="G"
        if(dna_strand[i]=="T"):
            salida+="A"
        if(dna_strand[i]=="A"):
            salida+="U"
        
    return salida
    pass


