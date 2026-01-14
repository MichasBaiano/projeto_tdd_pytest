import os
from calculadora_service import CalculadoraService

# Limpa a tela
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Faz a calculadora receber números e aplicar operações
def main():
    service = CalculadoraService()
    
    while True:
        limpar_tela()
        print("="*30)
        print("   CALCULADORA TDD - DEMO")
        print("="*30)
        print("1. Somar")
        print("2. Subtrair")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Verificar se é Par")
        print("6. Validar Positivo")
        print("0. Sair")
        print("-" * 30)
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '0':
            print("Saindo...")
            break
            
        try:
            # Captura inputs baseado na operação
            if opcao in ['1', '2', '3', '4']:
                a = float(input("Digite o 1º número: "))
                b = float(input("Digite o 2º número: "))
                
                if opcao == '1': res = service.somar(a, b)
                elif opcao == '2': res = service.subtrair(a, b)
                elif opcao == '3': res = service.multiplicar(a, b)
                elif opcao == '4': res = service.dividir(a, b)
                
                print(f"\n>> RESULTADO: {res}")

            elif opcao in ['5', '6']:
                num = float(input("Digite o número: "))
                
                if opcao == '5':
                    res = service.isPar(num)
                    print(f"\n>> É PAR? {'SIM' if res else 'NÃO'}")
                elif opcao == '6':
                    res = service.validarNumeroPositivo(num)
                    print(f"\n>> É POSITIVO? {'SIM' if res else 'NÃO'}")
            
            else:
                print("\nOpção inválida!")

        except ValueError as e:
            print(f"\n❌ ERRO DE VALIDAÇÃO: {e}")
        except Exception as e:
            print(f"\n❌ ERRO INESPERADO: {e}")
            
        input("\nPressione ENTER para continuar...")

# Chama o main
if __name__ == "__main__":
    main()