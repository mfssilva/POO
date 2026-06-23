from abc import ABC, abstractmethod
class Membro(ABC):
    def __init__(self, nome, idade, genero, email, contato, endereco, CPF):
        self.nome = nome
        self.idade = idade
        self.genero = genero
        self.email = email
        self.contato = contato
        self._endereco = endereco
        self._CPF = CPF
    @property
    def endereco(self):
        return self._endereco
    @property
    def CPF(self):
        return self._CPF
    @abstractmethod
    def calcular_mensalidade(self):
        pass