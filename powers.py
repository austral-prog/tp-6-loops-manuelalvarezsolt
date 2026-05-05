
def power(base, exp):
    """
    Retorna base elevado a exp usando un bucle for.
    exp es siempre >= 0.

    Ejemplo: power(2, 3) -> 8  (2*2*2)
    """
    power = base
    if exp == 0:
        return 1
    for i in range(1, exp):
        power = power * base
    return power

def sum_of_powers(base, max_exp):
    """
    Retorna la suma de base^0 + base^1 + ... + base^max_exp.
    Debe USAR la funcion power.

    Ejemplo: sum_of_powers(2, 3) -> 15  (1+2+4+8)
    """
    suma = 0
    for i in range(max_exp + 1):
        suma = power(base, i) + suma
    return suma

