def classify(number):
    if(number <=0):
        raise ValueError("Classification is only possible for positive integers.")
    factores=[]

    for i in range (1,number):
            if(number%i==0):
                factores.append(i)
        
    factores=sum(factores)
    if(factores==number):
            return "perfect"
    elif(factores>number):
            return "abundant"
    elif(factores<number):
            return "deficient"


    pass

