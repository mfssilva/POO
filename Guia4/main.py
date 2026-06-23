import os
from src.perguntadiscursiva import PerguntaDiscursiva
from src.correcao import Correcao

def main():
    print("=== Iniciando Teste do Sistema de Quiz com LLM (Guia 4) ===")
    
    
    if not os.environ.get("GROQ_API_KEY"):
        print("\n⚠️ AVISO: A variável de ambiente GROQ_API_KEY não foi detectada.")
        print("Defina-a no terminal antes de rodar: set GROQ_API_KEY=sua_chave\n")
    
    
    pergunta = PerguntaDiscursiva()
    pergunta.texto = "Explique o que é Encapsulamento em Programação Orientada a Objetos."
    pergunta.resposta_esperada = "É o mecanismo que esconde os detalhes internos de uma classe e protege os dados usando modificadores de acesso (privado/protegido) e métodos getters/setters."


    resposta_do_aluno = "Serve para esconder os dados do código lá dentro da classe usando private para ninguém mexer direto e usar métodos para acessar."
    
    print(f"\nQuestão: {pergunta.texto}")
    print(f"Resposta do Aluno: '{resposta_do_aluno}'")
    print("\nEnviando para correção na API do Groq (Llama 3)... Aguarde...")
    
    # 4. Executando a correção através da classe utilitária
    resultado = Correcao.corrigir_discursiva(pergunta, resposta_do_aluno)
    
    # 5. Exibindo o veredito da Inteligência Artificial
    print("\n================ RESULTADO DA CORREÇÃO ================")
    print(f"Acertou?      : {resultado.get('correta')}")
    print(f"Pontuação (0-1): {resultado.get('pontuacao')}")
    print(f"Feedback      : {resultado.get('feedback')}")
    print(f"Explicação    : {resultado.get('explicacao')}")
    print("=======================================================")

if __name__ == "__main__":
    main()