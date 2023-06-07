"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
    """Return coordinate value from a tuple containing the treasure name, and treasure coordinate.

    :param record: tuple - with a (treasure, coordinate) pair.
    :return: str - the extracted map coordinate.
    """

    cordenada= record[1]
    return cordenada

    pass


def convert_coordinate(coordinate):
    """Split the given coordinate into tuple containing its individual components.

    :param coordinate: str - a string map coordinate
    :return: tuple - the string coordinate split into its individual components.
    """
    
    tupla=(coordinate[0],coordinate[1])
    return tupla
    pass


def compare_records(azara_record, rui_record):
    """Compare two record types and determine if their coordinates match.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, tuple(coordinate_1, coordinate_2), quadrant) trio.
    :return: bool - do the coordinates match?
    """
    coorrui=rui_record[1][0]+rui_record[1][1]
    if(azara_record[1]==coorrui):
        return True
    else:
        return False

    pass


def create_record(azara_record, rui_record):
    """Combine the two record types (if possible) and create a combined record group.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return: tuple or str - the combined record (if compatible), or the string "not a match" (if incompatible).
    """
    if(compare_records(azara_record,rui_record)==True):
        return azara_record+rui_record
    else:
        return "not a match"
    pass


def clean_up(combined_record_group):
    """Clean up a combined record group into a multi-line string of single records.

    :param combined_record_group: tuple - everything from both participants.
    :return: str - everything "cleaned", excess coordinates and information are removed.

    The return statement should be a multi-lined string with items separated by newlines.

    (see HINTS.md for an example).
    """
    nueva=[]

    for j in range (0, len(combined_record_group)):
        nueva.append((combined_record_group[j][0],combined_record_group[j][2],combined_record_group[j][3],combined_record_group[j][4])) 
    
        

    salida=""""""
    for i in range (0,len(nueva)):
        salida+= str((nueva[i]))+"\n"
        
    return salida
    pass