# class - classe é um molde para criar objetos
# as classes geram novos objetos (instâncias) que podem ter seus próprios atributos e métodos.
# os objetos gerados pela classe podem usar seus dados internos para realizar varias ações
# por conveção, usamos PascalCase para nomes de classes.
# STRING = "Luiz"
# print(STRING.upper())
# print(isinstance(STRING, str))
# self referencia o objeto que está sendo manipulado.
class Pessoa:
    def __init__(self, nome, sobrenome):  # método de inicialização
        self.nome = nome
        self.sobrenome = sobrenome


p1 = Pessoa("Luiz", "Miranda")  # instância da classe Pessoa
p2 = Pessoa("Maria", "Joana")  # instância da classe Pessoa2
print(p1.nome)
print(p1.sobrenome)
print(p2.nome)
print(p2.sobrenome)
