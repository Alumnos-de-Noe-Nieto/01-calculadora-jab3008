"""
Nivel 8: Orquestación del Pipeline Completo
"""

from calculadora.conversor import romano_a_entero
from calculadora.error import ExpresionInvalida
from calculadora.parser import evaluar_expresion as parsear_expresion


def evaluar(expresion: str) -> int:
    # 1. Obtener los tokens.
    tokens_brutos = parsear_expresion(expresion)

    # 2. VALIDACIÓN: Si la expresión está vacía o solo tiene espacios.
    # El test 'test_nivel_8_13_expresion_solo_espacios' espera ExpresionInvalida.
    if not tokens_brutos or not expresion.strip():
        # Ajustamos el mensaje para que coincida con la estructura esperada por los tests
        raise ExpresionInvalida(f'La expresión "{expresion}" tiene una estructura inválida')

    # 3. Filtrar tokens de tipo 'ESPACIO'
    tokens = [t for t in tokens_brutos if t.tipo != 'ESPACIO']

    # 4. Cálculo del resultado
    # El primer token siempre es un ROMANO según la estructura validada en Nivel 7
    resultado = romano_a_entero(tokens[0].valor)

    for i in range(1, len(tokens), 2):
        operador = tokens[i].tipo
        # El siguiente valor numérico está en la posición i+1
        valor_siguiente = romano_a_entero(tokens[i+1].valor)

        if operador == 'SUMA':
            resultado += valor_siguiente
        elif operador == 'RESTA':
            resultado -= valor_siguiente

    # 5. Validación de resultado positivo (Crucial para el test 'V - X')
    if resultado <= 0:
        raise ExpresionInvalida(f"Resultado inválido ({resultado}). El resultado debe ser mayor a cero.")

    return resultado
