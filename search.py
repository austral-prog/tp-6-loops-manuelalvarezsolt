
def index_of(target, lst):
    """
    Retorna el indice de la primera ocurrencia de target en lst.
    Si no se encuentra, retorna -1.

    Ejemplo: index_of("Black", ["Red", "Green", "Black"]) -> 2
    """
    if target not in lst:
        return -1
    i = 0
    for element in lst:
        if target == element:
            return i
        i = i + 1
    return i



def index_of_by_index(target, lst, start):
    """
    Retorna el indice de la primera ocurrencia de target en lst,
    buscando a partir del indice start (inclusive).
    Si no se encuentra, retorna -1.

    Ejemplo: index_of_by_index("Black", ["Red", "Black", "Green", "Black"], 2) -> 3
    """
    if target not in lst[start: ]:
        return -1
    for i in range(start, len(lst)):
            if lst[i] == target:
                return i


def index_of_empty(lst):
    """
    Retorna el indice del primer string vacio ("") en lst.
    Si no hay ninguno, retorna -1.

    Ejemplo: index_of_empty(["Red", "", "Green"]) -> 1
    """
    if "" not in lst:
        return -1
    for i in range(len(lst)):
        if lst[i] == "":
            return i
