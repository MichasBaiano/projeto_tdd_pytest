class CalculadoraService:
    
    # Método Somar
    def somar(self, a, b):
        return a + b
    
    # Método Subtrair
    def subtrair(self, a, b):
        return a - b
    
    # Método Multiplicar
    def multiplicar(self, a, b):
        return a * b
    
    # Método Dividir
    def dividir(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Não é possível dividir por zero")
        return a / b
    
    # Método IsPar
    def isPar(self, numero):
        return numero % 2 == 0