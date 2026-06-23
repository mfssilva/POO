from src.pergunta import Pergunta

class PerguntaDiscursiva(Pergunta):
    def __init__(self, texto: str, pontuacao: float = 0.0, resposta_correta: str = ""):
        super().__init__(texto, pontuacao)
        self.resposta_correta = resposta_correta