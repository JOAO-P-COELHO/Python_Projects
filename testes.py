class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentacao(self):
        print(f"{self.nome} tem: {self.idade}")


pessoa1 = Pessoa("João", 30)
pessoa1.apresentacao()
