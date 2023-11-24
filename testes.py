class MinhaClasse:
    def metodo1(self):
        # Faça algo no método1
        self.resultado = 0.00
        self.metodo2()

    def metodo2(self):
        # Faça algo no método2 com o valor armazenado em resultado
        print(f'O valor recebido em metodo2 é: {self.resultado}')

# Uso da classe
objeto = MinhaClasse()
objeto.metodo1()