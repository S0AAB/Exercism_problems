# Score categories.
# Change the values as you see fit.
from itertools import count
from sre_constants import CATEGORY
from tkinter import E


YACHT = "YACHT"
ONES = "ONES"
TWOS = "TWOS"
THREES = "THREES"
FOURS = "FOURS"
FIVES = "FIVES"
SIXES = "SIXES"
FULL_HOUSE = "FULL_HOUSE"
FOUR_OF_A_KIND = "FOUR_OF_A_KIND"
LITTLE_STRAIGHT = "LITTLE_STRAIGHT"
BIG_STRAIGHT = "BIG_STRAIGHT"
CHOICE ="CHOICE"

def isFullHouse(dice):

    a=0
   
    x1=1
    for x1 in range(1,7):
        if(dice.count(x1)==3):
            a=x1
        else:
            x1+=1

    x2=1
    b=0
    for x2 in range(1,7):
        if(dice.count(x2)==2):
            b=x2
        else:
            x2+=1


    if(dice.count(a)==3 and dice.count(b)==2):
        return True
    else:
        return False  



    
    

def score(dice, category):
    contador=0
    
    a,b,c,d,e=dice

    
    if(category==YACHT):
        print("ENTRE AL YACHT")
        if(a==b==c==d==e):
            return int(50)
        else:
            return 0

    elif(category==ONES):
        print("ENTRE AL UNO")
        for i in dice:
            if(i==1):
                contador+=1
            else:
                contador+=0
        return contador
       

    elif(category==TWOS):
        print("ENTRE AL DOS")
        for i in dice:
            if(i==2):
                contador+=2
            else:
                contador+=0
        return contador


    elif(category==THREES):
        print("ENTRE AL TRES")
        for i in dice:
            if(i==3):
                contador+=3
            else:
                contador+=0
        return contador


    elif(category==FOURS):
        print("ENTRE AL CUATRO")
        for i in dice:
            if(i==4):
                contador+=4
            else:
                contador+=0
        return contador


    elif(category==FIVES):
        print("ENTRE AL CINCO")
        for i in dice:
            if(i==5):
                contador+=5
            else:
                contador+=0
        return contador

    elif(category==SIXES):
        print("ENTRE AL 6")
        for i in dice:
            if(i==6):
                contador+=6
            else:
                contador+=0
        return contador


    elif (category==BIG_STRAIGHT):
        print("ENTRE AL BIG STR")
        if(a+b+c+d+e==20):
            return int(30)
        else:
            return 0


    elif (category==LITTLE_STRAIGHT):
        print("ENTRE AL LITTLE STR")
        if(a+b+c+d+e==15):
            return int(30)
        else:
            return 0
    elif(category==CHOICE):
        print("ENTRE AL CHOICE")
        return int(a+b+c+d+e)

    elif (category==FULL_HOUSE):
        if (isFullHouse(dice)==True):
            return int(a+b+c+d+e)
        else:
            return 0

    elif(category==FOUR_OF_A_KIND):
        a=0
    
        x1=1
        for x1 in range(1,7):
            if(dice.count(x1)>=4):
                a=x1
            else:
                x1+=1

        x2=1
        b=0
        for x2 in range(1,7):
            if(dice.count(x2)==1):
                b=x2
            else:
                x2+=1
        print("EL QUE SE REPITE 4 VECES ES o MAS :",a)
        print("EL QUE SE REPITE 1 VECES ES :",b)
        
        if(dice.count(a)==4 and dice.count(b)==1 or dice.count(a)==5):
            return a*4
        else:
            return 0  

    
    

    pass





