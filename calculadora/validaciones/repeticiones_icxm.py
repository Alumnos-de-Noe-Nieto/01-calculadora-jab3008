"""
Nivel 2: Validación de repeticiones I/X/C/M.

Los símbolos I, X, C y M pueden repetirse hasta 3 veces consecutivas.
Ejemplos válidos: III, XXX, CCC, MMM
Ejemplos inválidos: IIII, XXXX, CCCC, MMMM
"""

SIMBOLOS_REPETIBLES = ['I', 'X', 'C', 'M']
MAX_REPETICIONES = 3

def validar_repeticiones_icxm(cadena: str) -> bool:
    for simbolo in SIMBOLOS_REPETIBLES:
        patron_invalido = simbolo * (MAX_REPETICIONES + 1)
        if patron_invalido in cadena:
            return False

    return True
