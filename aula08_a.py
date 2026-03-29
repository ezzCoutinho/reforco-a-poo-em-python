# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
import json

CAMINHO_ARQUIVO = "aula08exercicio.json"


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


p1 = Pessoa("João", 35)
p2 = Pessoa("Maria", 25)
p3 = Pessoa("Pedro", 40)
bd = [vars(p1), vars(p2), vars(p3)]


def fazer_dump():
    print("Fazendo dump")
    with open(CAMINHO_ARQUIVO, "w", encoding="utf8") as arquivo:
        json.dump(bd, arquivo, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    print("Executando o arquivo diretamente")
    fazer_dump()
