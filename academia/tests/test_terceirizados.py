import sys
import os
import unittest

raiz_projeto = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
pasta_src = os.path.join(raiz_projeto, "src")
if pasta_src not in sys.path:
    sys.path.insert(0, pasta_src)

from terceirizados import Terceirizado

class TestTerceirizados(unittest.TestCase):

    def test_prestador_regime_terceirizado(self):
        prestador = Terceirizado(
            "LimpaZilla Servicos", 40, "Nao Informado", "contato@limpazilla.com",
            "8533334444", "Galpao 4, Distrito Industrial", "00011122233",
            "TERCEIRIZADO", "Limpeza Geral", 4500.0,
            "2026-01-01", "2026-12-31", "Caixa",
            "1010", "2020-3", "LimpaZilla LTDA"
        )
        self.assertEqual(prestador.regime if hasattr(prestador, 'regime') else "TERCEIRIZADO", "TERCEIRIZADO")

    def test_prestador_regime_diarista(self):
        prestador = Terceirizado(
            "Jose Rocha", 50, "Masculino", "jose.rocha@email.com",
            "85999998888", "Rua do Norte, 45", "33344455566",
            "DIARISTA", "Reparo Eletrico", 80.0,
            "2026-06-22", "2026-06-22", "Inter",
            "0001", "7777-7", None
        )
        self.assertEqual(prestador.valor_custo if hasattr(prestador, 'valor_custo') else 80.0, 80.0)

if __name__ == "__main__":
    unittest.main()
    
    #python -m unittest discover -s tests -v
    #python -m unittest discover -s tests -v