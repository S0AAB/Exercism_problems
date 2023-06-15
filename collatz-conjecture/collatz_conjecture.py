def steps(number):
    cont=0
    if(number<1):
        raise ValueError("Only positive integers are allowed")
    else:
        while(number!=1):
            if(number%2==0):
                number=number//2
                print(number)
                cont+=1
            else:
                number=(number*3)+1
                print(number)
                cont+=1
        return cont
    
     
    pass

