import os
import json
from typing import Dict, Any
import requests

class LLMService:
    def __init__(self, api_key: str = None, model: str = "llama-3.3-70b-versatile"):
    
        self.api_key = api_key or os.environ.get("GROQ_API_KEY", "")
        self.model = model
        self.base_url = "https://api.groq.com/openai/v1/chat/completions"

    def corrigir_resposta(self, pergunta, resposta_aluno: str) -> Dict[str, Any]:
        
        from src.correcao import Correcao
        prompt = Correcao.criar_prompt_correcao(pergunta, resposta_aluno)
        
        try:
            return json.loads(self._fazer_chamada_api(prompt))
        except Exception as e:
            
            self._tratar_erro(e)
            return {
                "correta": False,
                "pontuacao": 0.0,
                "feedback": "Erro temporário na comunicação com o avaliador de IA.",
                "explicacao": "A requisição falhou ou retornou um formato inválido."
            }

    def _fazer_chamada_api(self, prompt: str) -> str:
        if not self.api_key:
            raise ValueError("Chave de API GROQ_API_KEY não configurada no ambiente.")

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": self.model,
            "messages": [
                {
                    "role": "system",
                    "content": "Você é um professor avaliador rigoroso. Você DEVE responder exclusivamente em formato JSON com as chaves: 'correta' (boolean), 'pontuacao' (float de 0.0 a 1.0), 'feedback' (string) e 'explicacao' (string)."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "response_format": {"type": "json_object"},
            "temperature": 0.0
        }

        response = requests.post(self.base_url, headers=headers, json=payload, timeout=10)
        
        if response.status_code != 200:
            raise RuntimeError(f"Erro na API Groq ({response.status_code}): {response.text}")
            
        dados = response.json()
        return dados["choices"][0]["message"]["content"]

    def _tratar_erro(self, e: Exception) -> None:
       
        print(f"[LLMService Error]: {str(e)}")