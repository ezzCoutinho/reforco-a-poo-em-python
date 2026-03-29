# atributos de classe

import datetime


class Pessoa:
    ano_atual = int(
        datetime.date.today().year
    )  # é nada mais que uma variável de classe, que pode ser acessada por todas as instâncias da classe.

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.ano_atual = 2021  # A gente pode ter um atributo de instancia, que so existe para a instância.

    def get_ano_nascimento(self):
        return (
            Pessoa.ano_atual - self.idade
        )  # e chamarmos ele pelo nome da classe, ele vai buscar o atributo de classe.


p1 = Pessoa("João", 39)
p2 = Pessoa("Helena", 16)
print(Pessoa.ano_atual)  # inclusive sem a necessidade de criar uma instância da classe.
Pessoa.ano_atual = 2021  # como é um atributo publico, ele pode ser alterado facilmente.
print(Pessoa.ano_atual)
print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())
