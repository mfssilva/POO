from folha_pagamento.funcionario import Funcionario

class Desenvolvedor(Funcionario):
    def __init__(self, nome: str, matricula: str, salario_base: float, linguagem: str, senioridade: str):
        super().__init__(nome, matricula, salario_base)
        self.linguagem = linguagem
        self.senioridade = senioridade

    def calcular_bonus(self) -> float:
        if self.senioridade == "junior":
            return self.salario_base * 0.05
        elif self.senioridade == "pleno":
            return self.salario_base * 0.10
        elif self.senioridade == "senior":
            return self.salario_base * 0.15
        return 0.0

    def calcular_descontos(self) -> float:
        return self.salario_base * 0.08

    def calcular_adicionais(self) -> float:
        if self.linguagem == "Python":
            return 500.0
        elif self.linguagem == "Java":
            return 400.0
        elif self.linguagem == "JavaScript":
            return 350.0
        else:
            return 200.0