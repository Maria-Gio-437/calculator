import tkinter as tk
from tkinter import messagebox

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

class CalculadoraGUI:
    def __init__(self):
        self.calculadora = Calculadora()
        self.janela = tk.Tk()
        self.janela.title("Calculadora Simples")

        # Criando campos para entrada dos números
        self.label_num1 = tk.Label(self.janela, text="Número 1:")
        self.label_num1.grid(row=0, column=0, padx=5, pady=5)
        self.entry_num1 = tk.Entry(self.janela, width=20)
        self.entry_num1.grid(row=0, column=1, padx=5, pady=5)

        self.label_num2 = tk.Label(self.janela, text="Número 2:")
        self.label_num2.grid(row=1, column=0, padx=5, pady=5)
        self.entry_num2 = tk.Entry(self.janela, width=20)
        self.entry_num2.grid(row=1, column=1, padx=5, pady=5)

        # Criando botões para as operações
        self.botao_soma = tk.Button(self.janela, text="+", command=self.somar)
        self.botao_soma.grid(row=2, column=0, padx=5, pady=5)

        self.botao_subtracao = tk.Button(self.janela, text="-", command=self.subtrair)
        self.botao_subtracao.grid(row=2, column=1, padx=5, pady=5)

        self.botao_multiplicacao = tk.Button(self.janela, text="*", command=self.multiplicar)
        self.botao_multiplicacao.grid(row=3, column=0, padx=5, pady=5)

        self.botao_divisao = tk.Button(self.janela, text="/", command=self.dividir)
        self.botao_divisao.grid(row=3, column=1, padx=5, pady=5)

        # Campo para exibir o resultado
        self.label_resultado = tk.Label(self.janela, text="Resultado:")
        self.label_resultado.grid(row=4, column=0, padx=5, pady=5)
        self.resultado = tk.Label(self.janela, text="")
        self.resultado.grid(row=4, column=1, padx=5, pady=5)

        # Botão para sair
        self.botao_sair = tk.Button(self.janela, text="Sair", command=self.janela.destroy)
        self.botao_sair.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

    def somar(self):
        try:
            num1 = float(self.entry_num1.get())
            num2 = float(self.entry_num2.get())
            resultado = self.calculadora.soma(num1, num2)
            self.resultado.config(text=str(resultado))
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira números válidos.")

    def subtrair(self):
        try:
            num1 = float(self.entry_num1.get())
            num2 = float(self.entry_num2.get())
            resultado = self.calculadora.subtracao(num1, num2)
            self.resultado.config(text=str(resultado))
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira números válidos.")

    def multiplicar(self):
        try:
            num1 = float(self.entry_num1.get())
            num2 = float(self.entry_num2.get())
            resultado = self.calculadora.multiplicacao(num1, num2)
            self.resultado.config(text=str(resultado))
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira números válidos.")

    def dividir(self):
        try:
            num1 = float(self.entry_num1.get())
            num2 = float(self.entry_num2.get())
            resultado = self.calculadora.divisao(num1, num2)
            self.resultado.config(text=str(resultado))
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira números válidos.")
        except ZeroDivisionError:
            messagebox.showerror("Erro", "Não é possível dividir por zero.")

    def run(self):
        self.janela.mainloop()

if __name__ == "__main__":
    calculadora_gui = CalculadoraGUI()
    calculadora_gui.run()
