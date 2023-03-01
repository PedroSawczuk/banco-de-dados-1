"""
Claudinei de Oliveira - encode: UTF8 - pt-br - data: 28-02-2023
scripts_json.py


# 6 -  Trabalhando com JSON 

import json

retorno = json.dumps(['Produtos', {'Notebook Dell': ('2TB', 'Novo', '110', 8450)}])
print(type(retorno))
print(retorno)


# 7 -  Trabalhando com JSON

import json

class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca

ravena = Gato('Ravena', 'Ashera')

print(ravena.__dict__)

retorno = json.dumps(ravena.__dict__)

print(type(retorno))
print(retorno)

"""

