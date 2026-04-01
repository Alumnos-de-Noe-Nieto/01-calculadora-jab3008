"""
Nivel 3: Validación de repeticiones V/L/D.

Los símbolos V, L y D NO pueden repetirse.
Ejemplos válidos: V, L, D, MCMXCIV
Ejemplos inválidos: VV, LL, DD
"""

SIMBOLOS_UNICOS = ['V', 'L', 'D']
MAX_REPETICIONES = 1

def validar_repeticiones_vld(cadena: str) -> bool:
    for simbolo in SIMBOLOS_UNICOS:
        patron_invalido = simbolo * (MAX_REPETICIONES + 1)
        if patron_invalido in cadena:
            return False

    return True
