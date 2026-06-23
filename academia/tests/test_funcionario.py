import sys
import os
import unittest

raiz_projeto = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
pasta_src = os.path.join(raiz_projeto, "src")
if pasta_src not in sys.path:
    sys.path.insert(0, pasta_src)

from funcionario import Funcionario

class TestFuncionario(unittest.TestCase):

    def test_cadastro_clt_valido(self):
        func = Funcionario(
            nome="Roberto Alves", idade=35, genero="Masculino", email="roberto@fittrack.com",
            contato="85999995555", endereco="Av Central, 10", CPF="44455566622",
            cargo="Recepcionista", salario_base=1500.0, ctps="12345", tipo_contrato="CLT",
            data_admissao="2026-01-01", horario_entrada="06:00", horario_saida="14:00",
            banco="Itau", agencia="0001", conta="12345-6"
        )
        self.assertEqual(func.tipo_contrato, "CLT")
        self.assertEqual(func.salario_base=1500.0)

    def test_cadastro_estagiario_e_promocao(self):
        func = Funcionario(
            nome="Amanda Lima", idade=20, genero="Feminino", email="amanda@fittrack.com",
            contato="85999996666", endereco="Av Perimetral, 20", CPF="77788899911",
            cargo="Estagiario de Musculacao", salario_base=800.0, ctps="54321", tipo_contrato="ESTAGIARIO",
            data_admissao="2026-02-01", horario_entrada="14:00", horario_saida="18:00",
            banco="Bradesco", agencia="0002", conta="65432-1"
        )
        self.assertEqual(func.tipo_contrato, "ESTAGIARIO")
        
        func.tipo_contrato = "CLT"
        func.salario_base = 2500.0
        self.assertEqual(func.tipo_contrato, "CLT")

if __name__ == "__main__":
    unittest.main()