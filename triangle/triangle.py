from calendar import c
from pickle import TRUE

def triangle(sides):
    a,b,c=sides
    if(a>0 and b>0 and c>0 and a + b >= c and b + c >= a and a + c >= b):
        return True
    else:
        return False

def equilateral(sides):
    a,b,c= sides
    if(a==b and b==c and c==a and triangle(sides)==True ):
        return True
    else:
        return False
    pass


def isosceles(sides):
    a,b,c= sides
    if( ((a==b and c!=a and c!=b)or (b==c and a!=b and a!=c) or (a==c and b!=a and b!=c) or(a==b and b==c and c==a) )and triangle(sides)):
        return True
    else:
        return False
    pass


def scalene(sides):
    a,b,c= sides
    if(a!=b!=c and triangle(sides)==True):
        return True
    else:
        return False
    pass
