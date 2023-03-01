"""
Claudinei de Oliveira - Pt-br - utf-8 - 28-02-2023
pickle


class Animal:
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def comer(self):
        print(f'{self.__nome} está comendo...')


class Gato(Animal):
    def __init__(self, nome):
         super().__init__(nome)

    def mia(self):
        print(f'{self.nome} está miando...')

class Cachorro(Animal):
    def __init__(self, nome):
         super().__init__(nome)

    def late(self):
        print(f'{self.nome} está latindo...')


"""
# Fazer a leitura em arquivos de dados em arquivos pickle
import pickle


try:
    with open('animais.pickle', 'rb') as arquivo:
        gato = pickle.load(arquivo)
        print(f'O gato chama-se {gato.nome}')
        gato.mia()
        print(f'E o tipo do ganoto é {type(gato)}')

        # print(f'O cachorro chama-se {cachorro.nome}')
        # cachorro.late()
        # print(f'E o tipo do cachorro é {type(cachorro)}')

except FileNotFoundError:
    with open('animais.pickle', 'w') as arquivo:
        pass










