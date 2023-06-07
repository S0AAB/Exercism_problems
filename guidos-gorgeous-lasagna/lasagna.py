


EXPECTED_BAKE_TIME=40
PREPARATION_TIME=10

def bake_time_remaining(elapsed_bake_time):
    """
    Return the time remaining to finishe the coocking
    This function takes the time of cooking and return the time remaining
    """
    return EXPECTED_BAKE_TIME-elapsed_bake_time
  
    pass

def preparation_time_in_minutes(number_of_layers):
    """
    function that takes the number of layers you want to add to the lasagna as an         argument and returns how many minutes you would spend making them. Assume each        layer takes 2 minutes to prepare.
    
    """
    return number_of_layers*2


def elapsed_time_in_minutes(number_of_layers,elapsed_bake_time):
    """
    Return elapsed cooking time.
    This function takes two numbers representing the number of layers & the time          already spent 
    baking and calculates the total elapsed minutes spent cooking the lasagna.
    """
    return preparation_time_in_minutes(number_of_layers)+elapsed_bake_time 
    
    
    