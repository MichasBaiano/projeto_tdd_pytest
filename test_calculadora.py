import pytest
from calculadora_service import CalculadoraService

class TestCalculadora:
    
    # Setup executado antes de cada teste
    def setup_method(self):
        self.calc = CalculadoraService()


    # --- SOMAR ---

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
        
        
    # --- SUBTRAIR ---

    # Cenário 1: Subtração simples
    def test_subtrair_correto(self):
        resultado = self.calc.subtrair(10, 5)
        assert resultado == 5

    # Cenário 2: Resultado negativo
    def test_subtrair_resultado_negativo(self):
        resultado = self.calc.subtrair(3, 5)
        assert resultado == -2

    # Cenário 3: Valores iguais (deve dar zero)
    def test_subtrair_valores_iguais(self):
        resultado = self.calc.subtrair(10, 10)
        assert resultado == 0
        
        
    # --- Multiplicar ---
    
    # Cenário 1: Multiplicação de dois positivos
    def test_multiplicar_positivos(self):
        resultado = self.calc.multiplicar(3, 4)
        assert resultado == 12

    # Cenário 2: Retornar zero quando um dos valores for zero
    def test_multiplicar_com_zero(self):
        resultado = self.calc.multiplicar(5, 0)
        assert resultado == 0

    # Cenário 3: Funcionar com números negativos
    def test_multiplicar_negativo(self):
        resultado = self.calc.multiplicar(3, -2)
        assert resultado == -6
        
        
    # --- Divisão ---
    
    # Cenário 1: Retornar o quociente correto
    def test_dividir_correto(self):
        resultado = self.calc.dividir(10, 2)
        assert resultado == 5

    # Cenário 2: Funcionar com números decimais  
    def test_dividir_decimais(self):
        resultado = self.calc.dividir(10, 4)
        assert resultado == 2.5

    # Cenário 3:Lançar exceção ao dividir por zero
    def test_dividir_por_zero(self):
        # O teste passa se o código lançar o erro ZeroDivisionError
        with pytest.raises(ZeroDivisionError):
            self.calc.dividir(10, 0)
    
    
    # --- IsPar ---       
         
    # Cenário 1: Retornar True para números pares
    def test_is_par_verdadeiro(self):
        assert self.calc.isPar(4) is True        # 4 é par -> True

    # Cenário 2: Retornar False para números ímpares
    def test_is_par_falso(self):
        assert self.calc.isPar(5) is False       # 5 é ímpar -> False

    # Cenário 3: Funcionar corretamente com zero (que é par)
    def test_is_par_zero(self):
        assert self.calc.isPar(0) is True        # 0 é par -> True
        
    
    # --- validarNumeroPositivo(numero) ---       

    # Cenário 1: Retornar verdadeiro para números positivos
    def test_validar_positivo_verdadeiro(self):
        assert self.calc.validarNumeroPositivo(5) is True    # 5 é positivo -> True

    # Cenário 2: Retornar falso para números negativos
    def test_validar_positivo_falso_negativo(self):
        assert self.calc.validarNumeroPositivo(-5) is False  # -5 não é positivo -> False

    # Cenário 3: Lançar exceção ou retornar falso para zero
    def test_validar_positivo_falso_zero(self):
        assert self.calc.validarNumeroPositivo(0) is False   # 0 não é positivo (regra escolhida) -> False