from math import sqrt


def score(x, y):
   
    punto=(sqrt((x**2)+(y**2)))
    print(punto)

    if(punto<=1):
        return 10
    elif(punto>1 and punto<=5):
        return 5
    elif(punto>5 and punto<=10):
        return 1
    else:
        return 0
    pass

    

