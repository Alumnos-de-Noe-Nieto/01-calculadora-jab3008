"""
Nivel 1: Análisis Léxico - Alfabeto (Σ = {I, V, X, L, C, D, M})
"""

def validar_simbolos(cadena: str) -> bool:
    cadena_limpia = cadena.strip()

    if cadena_limpia == "":
        return False

    return set(cadena_limpia).issubset("IVXLCDM")
