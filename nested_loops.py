# Replace the "ANSWER HERE" for your answer

def flatten(matrix):
    """
    Dada una lista de listas (matriz), retorna una unica lista
    con todos los elementos en orden.

    Ejemplo: flatten([[1, 2], [3, 4], [5, 6]]) -> [1, 2, 3, 4, 5, 6]
    """
    lista = []
    for listas in matrix:
        for i in range(len(listas)):
            lista.append(listas[i])
    return lista



def row_sums(matrix):
    """
    Dada una matriz (lista de listas de numeros), retorna una lista
    donde cada elemento es la suma de la fila correspondiente.

    Ejemplo: row_sums([[1, 2, 3], [4, 5, 6]]) -> [6, 15]
    """
    lista = []
    for listas in matrix:
        n = 0
        for elem in listas:
            n = n + elem
        lista.append(n)
    return lista

def col_sums(matrix):
    """
    Dada una matriz (lista de listas de numeros), retorna una lista
    donde cada elemento es la suma de la columna correspondiente.
    Se asume que todas las filas tienen la misma longitud.

    Ejemplo: col_sums([[1, 2, 3], [4, 5, 6]]) -> [5, 7, 9]
    """
    lista = []
    for i in range(len(matrix[0])):
        n = 0
        for listas in matrix:
            n = n + listas[i]
        lista.append(n)
    return lista

