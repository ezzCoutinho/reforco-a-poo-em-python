# class - classe é um molde para criar objetos
# as classes geram novos objetos (instâncias) que podem ter seus próprios atributos e métodos.
# os objetos gerados pela classe podem usar seus dados internos para realizar varias ações
# por conveção, usamos PascalCase para nomes de classes.
# STRING = "Luiz"
# print(STRING.upper())
# print(isinstance(STRING, str))
class Pessoa1:
    nome = "Luiz"
    sobrenome = "Miranda"
    idade = 30

    def falar(self):
        print(
            f"Olá, meu nome é {self.nome} {self.sobrenome} e eu tenho {self.idade} anos."
        )


class Pessoa2:
    nome = "Maria"
    sobrenome = "Joana"
    idade = 25

    def falar(self):
        print(
            f"Olá, meu nome é {self.nome} {self.sobrenome} e eu tenho {self.idade} anos."
        )


p1 = Pessoa1()
p2 = Pessoa2()
p1.falar()
p2.falar()
