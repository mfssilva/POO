from typing import Dict, Any, Optional
from src.perguntadiscursiva import PerguntaDiscursiva

class Correcao:
    @staticmethod
    def criar_prompt_correcao(pergunta: PerguntaDiscursiva, resposta_aluno: str) -> str:
        resposta_esperada = getattr(pergunta, "resposta_esperada", 'não informada')
        return (
            f"Enunciado da Questão: {pergunta.texto}\n"
            f"Gabarito/Resposta Esperada: {resposta_esperada}\n"
            f"Resposta submetida pelo Aluno: {resposta_aluno}\n\n"
            f"Avalie se a resposta do aluno é conceitualmente equivalente ao gabarito. "
            f"Determine a pontuação (de 0.0 a 1.0), se está correta (True/False) e gere um feedback estruturado."
        )

    @staticmethod
    def corrigir_discursiva(pergunta: PerguntaDiscursiva, resposta_aluno: str, service=None) -> Dict[str, Any]:
        if service is None:
            from src.llmservice import LLMService
            service = LLMService()
            
        return service.corrigir_resposta(pergunta, resposta_aluno)