
from membro import Membro

class Funcionario(Membro):
    def __init__(self, nome, idade, genero, email, contato, endereco, CPF, cargo, salario_base, 
                 carteira_trabalho, tipo_contrato, data_contratacao, horario_entrada, horario_saida,
                 banco, agencia, conta, nome_responsavel = None, contato_responsavel = None,
                 nome_social = None, necessidades_especiais = None):
        
        if idade < 14 or (tipo_contrato.upper() == "ESTAGIARIO" and idade < 18):
            if not nome_responsavel or not contato_responsavel:
                raise ValueError(f"CONTRATAÇÃO NEGADA: O funcionário {nome} é menor de idade para o contrato {tipo_contrato}. É OBRIGATÓRIO informar o Nome e o Contato do responsável legal no ato do cadastro!")

        super().__init__(nome, idade, genero, email, contato, endereco, CPF)
        self.cargo = cargo
        self.salario_base = salario_base
        self.carteira_trabalho = carteira_trabalho
        self.tipo_contrato = tipo_contrato.upper()
        self.data_contratacao = data_contratacao
        self.horario_entrada = horario_entrada
        self.horario_saida = horario_saida
        self.horas_acumuladas = 0
        self.banco_folgas = 0
        self.sobre_aviso = False
        self.nome_social = nome_social
        self.necessidades_especiais = necessidades_especiais
     
        self._banco = banco
        self._agencia = agencia
        self._conta = conta
        
        self.nome_responsavel = nome_responsavel
        self.contato_responsavel = contato_responsavel
        
        self.treino_gratis = True
        self.beneficios_adicionais = "Vale Transporte + Vale Alimentação" if self.tipo_contrato == "CLT" else "Nenhum"
        
        self.status = "Ativo"

    @property
    def banco(self):
        return self._banco

    @property
    def agencia(self):
        return self._agencia

    @property
    def conta(self):
        return self._conta

    def calcular_mensalidade(self):
        if self.status == "Demitido":
            return 0.0
        return self.salario_base

    def exibir(self):
        print("--" * 20)
        print("   INFORMAÇÕES DO FUNCIONÁRIO   ")
        print("--" * 20)
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Cargo: {self.cargo} | Contrato: {self.tipo_contrato}")
        print(f"CTPS: {self.carteira_trabalho} | Admissão: {self.data_contratacao}")
        print(f"Horário: {self.horario_entrada} às {self.horario_saida}")
        
        conta_oculta = f"***{self._conta[-4:]}" if len(self._conta) > 4 else "****"
        print(f"Dados Bancários: Banco {self._banco} | Ag: {self._agencia} | Conta: {conta_oculta}")
        
        print(f"Horas no Banco: {self.horas_acumuladas} | Folgas a Tirar: {self.banco_folgas}")
        print(f"Sobre-aviso: {'Sim' if self.sobre_aviso else 'Não'}")
        print(f"Treinar Grátis: {'Sim (Benefício Ativo)' if self.treino_gratis else 'Não'}")
        print(f"Benefícios de Contrato: {self.beneficios_adicionais}")
        print(f"Status: {self.status}")
        print(f"Salário Líquido a Receber: R$ {self.calcular_mensalidade():.2f}")
        
        if self.idade < 18 and self.nome_responsavel:
            print(f"Responsável Legal: {self.nome_responsavel} - Contato: {self.contato_responsavel}")
            
        print("--" * 20)

