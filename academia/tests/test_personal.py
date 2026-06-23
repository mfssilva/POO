import sys
import os
import unittest

raiz_projeto = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
pasta_src = os.path.join(raiz_projeto, "src")
if pasta_src not in sys.path:
    sys.path.insert(0, pasta_src)

from personal import Personal

class TestPersonal(unittest.TestCase):

    def test_personal_interno_taxa_zero(self):
        p_interno = Personal(
            nome="Moniq Peixoto", idade=25, genero="Feminino", email="moniq@fittrack.com", 
            contato="85999991111", endereco="Endereco Corporativo", cpf="00000000001", 
            especialidade="Musculacao", valor=0.0, cref="CREF-000001", banco="Banco do Brasil", 
            agencia="0001", conta="1000-1", taxa_academia=0.0
        )
        self.assertEqual(p_interno.taxa_academia, 0.0)
        self.assertEqual(p_interno.calcular_mensalidade(), 0.0)

    def test_personal_externo_taxa_fixa(self):
        p_externo = Personal(
            nome="Rodrigo Faro", idade=29, genero="Masculino", email="rodrigo@personal.com", 
            contato="85999997777", endereco="Rua X, 99", cpf="88877766655", 
            especialidade="Crossfit", valor=120.0, cref="CREF-098765", banco="Nubank", 
            agencia="0001", conta="98765-4", taxa_academia=250.0
        )
        self.assertEqual(p_externo.taxa_academia, 250.0)
        self.assertEqual(p_externo.calcular_mensalidade(), 250.0)
        
        p_externo.status = "Suspenso"
        self.assertEqual(p_externo.calcular_mensalidade(), 0.0)

if __name__ == "__main__":
    unittest.main()
    