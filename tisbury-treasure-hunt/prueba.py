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

print(clean_up((('Brass Spyglass', '4B', 'Abandoned Lighthouse', ('4', 'B'), 'Blue'), ('Vintage Pirate Hat', '7E', 'Quiet Inlet (Island of Mystery)', ('7', 'E'), 'Orange'), ('Crystal Crab', '6A', 'Old Schooner', ('6', 'A'), 'Purple'))))


