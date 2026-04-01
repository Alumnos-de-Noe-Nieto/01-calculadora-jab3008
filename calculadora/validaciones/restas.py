"""
Nivel 5: Validación de restas válidas (Análisis Semántico).

Solamente 6 pares específicos de símbolos son permitidos para restar:
IV (4), IX (9), XL (40), XC (90), CD (400), CM (900)

Ejemplos válidos: IV, IX, XL, XC, CD, CM, XIV (X + IV)
Ejemplos inválidos: IL (49), IC (99), XD (490), XM (990), VX (5), LC (50)
"""

VALORES = {
    'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
}

SUSTRACCIONES_VALIDAS = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']

def validar_restas(cadena: str) -> bool:
    """
    Valida que las restas (sustracciones) sean válidas.

    Nivel 5: Análisis Semántico - Restas válidas

    💡 PISTA: Para detectar una sustracción (valor actual < valor siguiente):
    💡 PISTA: Ejemplo: "IV" → I(1) < V(5) → par "IV" está en SUSTRACCIONES_VALIDAS → True
    💡 PISTA: Ejemplo: "IL" → I(1) < L(50) → par "IL" NO está en SUSTRACCIONES_VALIDAS → False
    💡 PISTA: Ejemplo: "XIV" → X >= I, luego I < V → par "IV" está en SUSTRACCIONES_VALIDAS → True
    💡 PISTA: Ejemplo: "IIX" → I repetido antes de IX → False
    """
    i = 0
    while i < len(cadena) - 1:
        valor_actual = VALORES[cadena[i]]
        valor_siguiente = VALORES[cadena[i+1]]

        # Detectamos una sustracción cuando el valor actual < valor siguiente
        if valor_actual < valor_siguiente:
            par = cadena[i:i+2]

            # 1. Verificar si el par es una de las 6 restas oficiales
            if par not in SUSTRACCIONES_VALIDAS:
                return False

            # 2. Verificar que no haya repetición antes de la resta (ej: IIX)
            if i > 0 and cadena[i-1] == cadena[i]:
                return False

            # Si es válida, saltamos ambos caracteres
            i += 2
        else:
            # Si no es resta, avanzamos uno por uno
            i += 1

    return True
