"""
Nivel 4: Análisis Sintáctico III - Orden Descendente
"""

VALORES = {
    'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1
}

SUSTRACCIONES_VALIDAS = {'IV', 'IX', 'XL', 'XC', 'CD', 'CM'}

def validar_orden_descendente(cadena: str) -> bool:
    i = 0
    while i < len(cadena) - 1:
        v_actual = VALORES[cadena[i]]
        v_siguiente = VALORES[cadena[i+1]]
        par = cadena[i:i+2]

        # CASO 1: Es una sustracción (Ej: IV, IX...)
        if v_actual < v_siguiente:
            if par not in SUSTRACCIONES_VALIDAS:
                return False

            # No puede haber repeticiones antes de la resta (Ej: IIV es inválido)
            if i > 0 and cadena[i-1] == cadena[i]:
                return False

            # Tras una resta, lo que sigue debe ser menor al símbolo restado
            if i + 2 < len(cadena) and VALORES[cadena[i+2]] >= v_actual:
                return False

            i += 2  # Saltamos el par de la resta
            continue

        # CASO 2: Orden normal o inicio de una resta posterior
        # CORRECCIÓN SIM102: Combinamos los 'if' anidados en una sola condición
        if (i + 2 < len(cadena) and
            v_siguiente < VALORES[cadena[i+2]] and
            v_actual <= VALORES[cadena[i+2]] and
            cadena[i] != cadena[i+2]):
            return False

        # Validación estándar de orden descendente
        if v_actual < v_siguiente:
            return False

        i += 1

    return True
