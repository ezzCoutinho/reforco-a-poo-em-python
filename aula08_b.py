import json
from aula08_a import Pessoa, CAMINHO_ARQUIVO


with open(CAMINHO_ARQUIVO, "r", encoding="utf8") as arquivo:
    pessoas = json.load(arquivo)
    for pessoa in pessoas:
        p = Pessoa(**pessoa)
        print(p.nome, p.idade)
