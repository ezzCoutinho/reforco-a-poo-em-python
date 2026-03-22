# escopo da classe e de métodos da classe


class Animal:
    def __init__(self, nome):
        self.nome = nome

        variavel = "valor"
        print(variavel)

    def comendo(self, alimento):
        return print(f"{self.nome} está comendo {alimento}")

    def executar(self, *args, **kwargs):
        self.comendo(*args, **kwargs)


leao = Animal("Leão")
print(leao.nome)
leao.executar("maçã")

baliea = Animal("Baleia")
print(baliea.nome)
baliea.executar("peixe")
