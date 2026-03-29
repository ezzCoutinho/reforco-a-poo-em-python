# __dict__ e vars para atributos de instância, retorna um dicionário com os atributos(chave-valor) da instância.


class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return self.ano_atual - self.idade


dados = {"nome": "João", "idade": 35}  # Pegando o dict do vars
p1 = Pessoa(**dados)  # desempacotando o dict para o construtor da classe
# print(p1.__dict__)
# print(vars(p1))
# p1.__dict__["outro"] = "coisa"
# print(p1.__dict__)
# print(vars(p1))
# p1.__dict__["nome"] = "João da Silva"
print(vars(p1))
print(p1.nome)
print(p1.idade)
