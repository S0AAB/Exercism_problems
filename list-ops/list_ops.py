def append(list1, list2):
    salida = list1+list2
    return salida

def concat(lists):
    salida = []
    i=0
    while(len(lists)!=0):
        salida += append(lists[i], lists[i+1])
        lists.pop(0)
        lists.pop(0)
    return salida



def filter(function, list):
    salida = []
    for i in list:
        if (function(i) == True):
            salida.append(i)
    return salida


def length(list):
    return len(list)


def map(function, list):
    salida = []
    for i in list:
        salida.append(function(i))
    return salida

def foldl(function, list, initial):
    variable=initial
    for i in list:
        variable=function(variable,i)
    return (variable)
      

def foldr(function, list, initial):
    variable=initial
    for i in list[::-1]:
        variable=function(variable,i)
    return (variable)
    pass

def reverse(list):
    return list[::-1]
    pass
