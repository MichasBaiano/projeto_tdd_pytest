import pytest
from calculadora_service import CalculadoraService

class TestCalculadora:
    
    # Setup executado antes de cada teste
    def setup_method(self):
        self.calc = CalculadoraService()

    # Cenário 1: Soma de dois números positivos 
    def test_somar_dois_positivos(self):
        resultado = self.calc.somar(2, 3)
        assert resultado == 5

    # Cenário 2: Soma de positivo e negativo 
    def test_somar_positivo_e_negativo(self):
        resultado = self.calc.somar(5, -3)
        assert resultado == 2

    # Cenário 3: Soma de dois zeros 
    def test_somar_dois_zeros(self):
        resultado = self.calc.somar(0, 0)
        assert resultado == 0