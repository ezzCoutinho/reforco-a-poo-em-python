# entendo self em classes Python
# classe - molde (geralmente sem dados)
# instância da class (objeto) - tem os dados
# uma classe pode gerar várias instâncias
# na classe o self é a propria instância


class Carro:
    def __init__(
        eu_mesmo, nome
    ):  # self pode ser qualquer nome, mas por convenção usamos self.
        eu_mesmo.nome = nome

    def acelerar(eu_mesmo):
        print(f"{eu_mesmo.nome} está acelerando...")


fusca = Carro("Fusca")
Carro.acelerar(fusca)
fusca.acelerar()
# print(fusca.nome)

celta = Carro("Celta")
Carro.acelerar(celta)
celta.acelerar()
# print(celta.nome)
