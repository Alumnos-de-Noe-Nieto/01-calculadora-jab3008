"""
Nivel 6: Generación de Código - Conversión de Romano a Entero
"""

from calculadora.error import ExpresionInvalida
from calculadora.validaciones.alfabeto import validar_simbolos
from calculadora.validaciones.orden_descendente import validar_orden_descendente
from calculadora.validaciones.repeticiones_icxm import validar_repeticiones_icxm
from calculadora.validaciones.repeticiones_vld import validar_repeticiones_vld
from calculadora.validaciones.restas import validar_restas

# Diccionario de valores según la especificación
VALORES = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}


def romano_a_entero(cadena: str) -> int:
    """
    Convierte una cadena de números romanos válida a su valor entero correspondiente.
    """
    # 1. Validaciones (Niveles 1-5).
    if not validar_simbolos(cadena):
        raise ExpresionInvalida(f"La cadena '{cadena}' contiene símbolos inválidos")

    if not validar_repeticiones_icxm(cadena):
        raise ExpresionInvalida(
            f"La cadena '{cadena}' tiene repeticiones inválidas de I/X/C/M"
        )

    if not validar_repeticiones_vld(cadena):
        raise ExpresionInvalida(
            f"La cadena '{cadena}' tiene repeticiones inválidas de V/L/D"
        )

    if not validar_orden_descendente(cadena):
        raise ExpresionInvalida(
            f"La cadena '{cadena}' no sigue un orden descendente válido"
        )

    if not validar_restas(cadena):
        raise ExpresionInvalida(
            f"La cadena '{cadena}' contiene restas semánticamente inválidas"
        )

    # 2. Algoritmo de conversión
    total = 0
    valor_previo = 0

    for simbolo in reversed(cadena):
        valor_actual = VALORES[simbolo]

        if valor_actual < valor_previo:
            total -= valor_actual
        else:
            total += valor_actual

        valor_previo = valor_actual

    return total
