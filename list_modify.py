# Replace the "ANSWER HERE" for your answer

def put(value, lst):
    """
    Coloca value en el primer lugar vacio ("") que encuentre en lst
    y retorna el indice donde lo coloco.
    Si no hay ningun lugar vacio, retorna -1.
    IMPORTANTE: esta funcion modifica la lista original.

    Ejemplo:
        colors = ["Red", "", "Green"]
        put("Blue", colors) -> 1
        # colors ahora es ["Red", "Blue", "Green"]
    """
    if "" in lst:
        m = lst.index("")
        lst[m] = value
        return m
    else:
        return -1




def remove(value, lst):
        """
        Busca todas las ocurrencias de value en lst, las reemplaza por ""
        y retorna la cantidad de eliminaciones realizadas.
        IMPORTANTE: esta funcion modifica la lista original.

        Ejemplo:
            colors = ["Red", "Green", "Red", "Blue"]
            remove("Red", colors) -> 2
            # colors ahora es ["", "Green", "", "Blue"]
        """
        m = 0
        for element in range(len(lst)):
            if value == lst[element]:
                lst[element] = ""
                m = m + 1
        return m

