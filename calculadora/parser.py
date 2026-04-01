"""
Nivel 7: Parsing de Expresiones
Este módulo contiene las funciones para parsear expresiones aritméticas con números romanos.
"""

from dataclasses import dataclass
from calculadora.error import ExpresionInvalida


@dataclass
class Token:
    tipo: str
    valor: str
    posicion: int


def evaluar_expresion(expresion: str) -> list[Token]:
    """
    Tokeniza y valida una expresión aritmética de números romanos.
    """
    if not expresion.strip():
        return []

    try:
        tokens = tokenizar_expresion(expresion)
        if not validar_estructura_tokens(tokens):
            raise ExpresionInvalida(
                f'La expresión "{expresion}" tiene una estructura inválida'
            )
        return tokens
    except ExpresionInvalida as e:
        raise e


def tokenizar_expresion(expresion: str) -> list[Token]:
    """
    Convierte el texto en una lista de objetos Token (Romano, Suma, Resta, Espacio).
    """
    tokens = []
    i = 0
    alfabeto_romano = "IVXLCDM"

    while i < len(expresion):
        caracter = expresion[i]

        if caracter == ' ':
            tokens.append(Token("ESPACIO", " ", i))
            i += 1
        elif caracter == '+':
            tokens.append(Token("SUMA", "+", i))
            i += 1
        elif caracter == '-':
            tokens.append(Token("RESTA", "-", i))
            i += 1
        elif caracter in alfabeto_romano:
            inicio = i
            while i < len(expresion) and expresion[i] in alfabeto_romano:
                i += 1
            # Posición correcta: inicio del número
            tokens.append(Token("ROMANO", expresion[inicio:i], inicio))
        else:
            raise ExpresionInvalida(f"Carácter inválido '{caracter}' en posición {i}")

    return tokens


def validar_estructura_tokens(tokens: list[Token]) -> bool:
    """
    Valida la alternancia correcta: ROMANO -> OPERADOR -> ROMANO.
    """
    # Filtramos los espacios para validar la lógica pura
    tokens_filtrados = [t for t in tokens if t.tipo != 'ESPACIO']

    # CORRECCIÓN PARA EL TEST 7.7:
    # El test espera que un solo número (X) sea False.
    # Por tanto, la longitud mínima debe ser 3 (Romano, Operador, Romano).
    if len(tokens_filtrados) < 3 or len(tokens_filtrados) % 2 == 0:
        return False

    for i, token in enumerate(tokens_filtrados):
        # Posiciones pares (0, 2, 4...): DEBEN ser números romanos
        if i % 2 == 0:
            if token.tipo != "ROMANO":
                return False
        # Posiciones impares (1, 3, 5...): DEBEN ser operadores
        else:
            if token.tipo not in ["SUMA", "RESTA"]:
                return False

    return True
