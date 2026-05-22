from folha_pagamento.funcionario import Funcionario

# Desenvolva a classe Gerente aqui.

class Gerente(Funcionario):
    def __init__(self, nome: str, matricula: str, salario_base: float, setor: str, qtd_equipe: int):
        super().__init__(nome, matricula, salario_base) #passei isso aqui pra classe mae
        self.setor = setor
        self.qtd_equipe = qtd_equipe
    #primeira funcao para calcular o salario
    def calcular_bonus(self) -> float:
        #salario mais o bous do negocio por equipe
        if self.qtd_equipe <= 5:
            return self.salario_base * 0.10
        elif self.qtd_equipe <= 10:
            return self.salario_base * 0.15
        else:
            return self.salario_base * 0.20
    def calcular_descontos(self) -> float: 
        #descoto de 12%
        return self.salario_base * 0.12
    def calcular_adicionais(self) -> float:
        #quanto mais resposabilidade maior o adicional
        if self.qtd_equipe > 10:
            return 2000.0
        elif self.qtd_equipe > 5:
            return 1000.0
        else:
            return 500.0