import sys
import os
import unittest

raiz_projeto = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
pasta_src = os.path.join(raiz_projeto, "src")
if pasta_src not in sys.path:
    sys.path.insert(0, pasta_src)

from aluno import Aluno

class TestAluno(unittest.TestCase):

    def test_matricula_aluno_maior_idade(self):
        aluno = Aluno(
            nome="Carlos Silva", idade=25, genero="Masculino", email="carlos@email.com",
            contato="85999991111", endereco="Rua A, 123", CPF="11122233344",
            tipo_aluno="MENSALISTA", personal="Moniq Peixoto", autorizacao_responsavel=False,
            plano="Premium", forma_pagamento="Pix"
        )
        self.assertEqual(aluno.tipo_aluno, "MENSALISTA")
        self.assertEqual(aluno.personal, "Moniq Peixoto")
        self.assertIsNone(aluno.nome_responsavel)

    def test_matricula_aluno_menor_idade_com_responsavel(self):
        aluno = Aluno(
            nome="Lucas Souza", idade=16, genero="Masculino", email="lucas@email.com",
            contato="85999992222", endereco="Rua B, 456", CPF="55566677788",
            tipo_aluno="MENSALISTA", personal="David Wytalo", autorizacao_responsavel=True,
            nome_responsavel="Marcos Souza", contato_responsavel="85988883333",
            plano="Basic", forma_pagamento="Cartao"
        )
        self.assertTrue(aluno.autorizacao_responsavel)
        self.assertEqual(aluno.nome_responsavel, "Marcos Souza")

if __name__ == "__main__":
    unittest.main()