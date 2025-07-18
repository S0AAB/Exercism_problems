def add_item(current_cart:dict, items_to_add):
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """
    for item in items_to_add:
        if(item in current_cart):
            current_cart[item]+=1
        else:
            current_cart[item]=1
    
    return current_cart



def read_notes(notes):
    salida=dict()
    for item in notes:
        if(item not in salida):
            salida[item]=notes.count(item)
        else:
            salida[item]+=1

    return salida
    

def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: dict - dictionary with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """
    merged=  ideas | dict(recipe_updates)
    

    return merged



def sort_entries(cart):
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """
    return  dict(sorted(cart.items()))




def send_to_store(cart, aisle_mapping:dict):
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """
    for item in(cart):
     
        if(item in aisle_mapping.keys()):   
            value=cart[item]
            cart[item]=(aisle_mapping[item])
            cart[item].insert(0,value)
    return dict(sorted(cart.items(),reverse=True))



def update_store_inventory(fulfillment_cart, store_inventory):

  
    for item in store_inventory:
        if(item in fulfillment_cart):
                if(store_inventory[item][0]-fulfillment_cart[item][0]==0):
                    store_inventory[item][0]="Out of Stock"
                else:
                    store_inventory[item][0]=store_inventory[item][0]-fulfillment_cart[item][0]

    return store_inventory

