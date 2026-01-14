from typing import Union

# Define um tipo personalizado para facilitar a leitura (int ou float)
Numero = Union[int, float]

class CalculadoraService:
    """
    Classe responsável por realizar operações matemáticas básicas e validações
    para demonstrar a aplicação de TDD.
    """

    def somar(self, a: Numero, b: Numero) -> Numero:
        """Retorna a soma de dois números."""
        return a + b

    def subtrair(self, a: Numero, b: Numero) -> Numero:
        """Retorna a subtração de a por b."""
        return a - b

    def multiplicar(self, a: Numero, b: Numero) -> Numero:
        """Retorna a multiplicação de dois números."""
        return a * b

    def dividir(self, a: Numero, b: Numero) -> float:
        """
        Retorna a divisão de a por b.
        Lança ZeroDivisionError se b for zero.
        """
        if b == 0:
            raise ZeroDivisionError("Não é possível dividir por zero")
        return a / b

    def isPar(self, numero: int) -> bool:
        """
        Retorna True se o número for par, caso contrário False.
        Lança ValueError se receber um número decimal
        """
        if isinstance(numero, float) and not numero.is_integer():
            raise ValueError("O conceito de par/ímpar aplica-se apenas a números inteiros.")
        
        return numero % 2 == 0

    def validarNumeroPositivo(self, numero: Numero) -> bool:
        """
        Verifica se o número é positivo.
        Considera Zero como não positivo (False).
        """
        return numero > 0