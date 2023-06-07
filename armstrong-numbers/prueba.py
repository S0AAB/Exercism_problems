def is_armstrong_number(number):
    xd= str(number)
    a=0
    largo=len(xd)
    for i in range (0,largo):
        
        a=a+(int(xd[i])**largo)
    if(a==number):
        return True
    else:
        return False
    pass

print (is_armstrong_number(153))