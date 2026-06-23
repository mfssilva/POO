from abc import ABC, abstractmethod

class Pergunta(ABC):
    def __init__(self, texto: str, pontuacao: float = 0.0):
        self.texto = texto
        self.pontuacao = pontuacao