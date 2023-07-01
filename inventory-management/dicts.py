def create_inventory(items):

    salida = {}
    for i in range(len(items)):
        salida[items[i]] = items.count(items[i])
    return salida


def add_items(inventory, items):

    for i in range(len(items)):

        if (items[i] in inventory):
            inventory[items[i]] += 1
        else:
            inventory[items[i]] = 1
    return inventory


def decrement_items(inventory, items):
    for i in range(len(items)):
        if (items[i] in inventory and inventory[items[i]] != 0):
            inventory[items[i]] -= 1
    return inventory


def remove_item(inventory, item):
    for i in range(len(item)):
        try:
            del inventory[item]
        except:
            pass
    return inventory


def list_inventory(inventory):
    salida = []
    for clave, valor in inventory.items():
        if (valor != 0):
            salida.append((clave, valor))
    return salida
