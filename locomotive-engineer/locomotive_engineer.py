
def get_list_of_wagons(*args):
    salida=[]
    for i in range(len(args)):
        salida.append(args[i])
    return salida
  


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    a,b,*resto=each_wagons_id
    each_wagons_id.append(a)
    each_wagons_id.append(b)
    each_wagons_id=each_wagons_id[2:len(each_wagons_id)]
    for i in missing_wagons[::-1]:
        each_wagons_id.insert(each_wagons_id.index(1)+1,i)

    return each_wagons_id




def add_missing_stops(a,**kwargs):
    dicRuta,dicDestino,=a,kwargs
    array=[]
    for k,v in dicDestino.items():
        array.append(v)
    dicRuta["stops"]=array

    return dicRuta
    pass

def extend_route_information(route, more_route_information):
    for k,v in more_route_information.items():
        route[k]=v
    return route
    pass


def fix_wagon_depot(wagons_rows):
    c1,c2,c3=wagons_rows
    salida=[[],[],[]]
    for i in range (3):
        salida[i]=[c1[i],c2[i],c3[i]]

    return salida

    pass

