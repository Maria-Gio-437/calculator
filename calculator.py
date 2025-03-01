class Calculadora:
    def __init__(self):
        pass

    def soma(self, num1, num2):
        """Realiza a soma de dois números."""
        return num1 + num2

    def subtracao(self, num1, num2):
        """Realiza a subtração de dois números."""
        return num1 - num2

    def multiplicacao(self, num1, num2):
        """Realiza a multiplicação de dois números."""
        return num1 * num2

    def divisao(self, num1, num2):
        """Realiza a divisão de dois números."""
        if num2 == 0:
            raise ZeroDivisionError("Não é possível dividir por zero.")
        return num1 / num2

def main():
    calculadora = Calculadora()
    
    while True:
        print("\nCalculadora Simples")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
            except ValueError:
                print("Por favor, insira um número válido.")
                continue
            
            if escolha == '1':
                print(f"{num1} + {num2} = {calculadora.soma(num1, num2)}")
            elif escolha == '2':
                print(f"{num1} - {num2} = {calculadora.subtracao(num1, num2)}")
            elif escolha == '3':
                print(f"{num1} * {num2} = {calculadora.multiplicacao(num1, num2)}")
            elif escolha == '4':
                try:
                    print(f"{num1} / {num2} = {calculadora.divisao(num1, num2)}")
                except ZeroDivisionError as e:
                    print(e)
        elif escolha == '5':
            print("Saindo da calculadora.")
            break
        else:
            print("Opção inválida. Por favor, escolha novamente.")

if __name__ == "__main__":
    main()
