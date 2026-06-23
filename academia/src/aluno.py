from membro import Membro
from datetime import datetime

class Aluno(Membro):
    def __init__(self, nome, idade, genero, email, contato, endereco, CPF,
                 tipo_aluno, personal=None,
                 autorizacao_responsavel=False, nome_responsavel=None, contato_responsavel=None,
                 nome_social=None, necessidades_especiais=None, forma_pagamento=None,
                 auto_declaracao_saude=False, objective=None, plano=None,
                 numero_cartao=None, titular_cartao=None, validade_cartao=None, cvv=None,
                 dia_vencimento=10, data_matricula=None):

        # Validação para menor de 18 anos
        if idade < 18:
            if not nome_responsavel or not contato_responsavel:
                raise ValueError("CADASTRO NEGADO: dados do responsável obrigatórios para menores de 18 anos")
            if not autorizacao_responsavel:
                raise ValueError("CADASTRO NEGADO: autorização do responsável obrigatória")

        super().__init__(nome, idade, genero, email, contato, endereco, CPF)

        self.tipo_aluno = tipo_aluno
        self.personal = personal
        self.autorizacao_responsavel = autorizacao_responsavel
        self.nome_responsavel = nome_responsavel
        self.contato_responsavel = contato_responsavel

        self.nome_social = nome_social
        self.necessidades_especiais = necessidades_especiais
        self.forma_pagamento = forma_pagamento
        self.auto_declaracao_saude = auto_declaracao_saude
        self.objetivo = objective
        self.plano = plano
        self.dia_vencimento = dia_vencimento
        self.data_matricula = data_matricula if data_matricula else datetime.now().strftime("%Y-%m-%d")

        self.servicos = []
        self.infracoes = 0
        self.status_pagamento = "Em dia"

        # Atributos protegidos do Cartão
        self._numero_cartao = numero_cartao
        self._titular_cartao = titular_cartao
        self._validade_cartao = validade_cartao
        self._cvv = cvv

        # CORREÇÃO CRÍTICA: Definir o status ANTES de tentar adicionar o serviço/plano
        if not auto_declaracao_saude:
            self.status = "Bloqueado - Sem Declaração de Saúde"
        else:
            self.status = "Ativo"

        # Agora o método adicionar_servico consegue ler o self.status sem quebrar!
        if plano:
            self.adicionar_servico(plano)

    @property
    def numero_cartao(self):
        return self._numero_cartao

    @property
    def titular_cartao(self):
        return self._titular_cartao

    @property
    def validade_cartao(self):
        return self._validade_cartao

    @property
    def cvv(self):
        return self._cvv

    def adicionar_servico(self, servico):
        if self.status == "Convidado a se retirar" or "Bloqueado" in self.status:
            return

        servico_lower = servico.lower()

        if "plus" in servico_lower:
            self.servicos = ["Plano Plus"]
        elif "fidelidade" in servico_lower:
            self.servicos = ["Plano Fidelidade"]
        elif "premium" in servico_lower:
            self.servicos = ["Plano Premium"]
        elif "basic" in servico_lower:
            self.servicos = ["Plano Basic"]
        elif "diarista" in servico_lower:
            self.servicos = ["Plano Diarista"]
        else:
            if not self.servicos:
                self.servicos.append(servico)

    def aplicar_infracao(self, motivo):
        if self.status == "Convidado a se retirar":
            return

        self.infracoes += 1

        if self.infracoes >= 3:
            self.status = "Convidado a se retirar"
            self.servicos = []

    def controlar_financeiro(self, dias_atraso):
        if self.status == "Convidado a se retirar":
            return

        if dias_atraso > 0:
            self.status_pagamento = "Saldo Devedor"
            if dias_atraso > 3:
                self.status = "Bloqueado - Saldo Devedor"
        else:
            self.status_pagamento = "Em dia"
            if self.status == "Bloqueado - Saldo Devedor":
                self.status = "Ativo"

    def calcular_mensalidade(self):
        if self.status == "Convidado a se retirar":
            return 0.0

        precos_planos = {
            "Plano Basic": 90.0,
            "Plano Plus": 140.0,
            "Plano Premium": 200.0,
            "Plano Fidelidade": 220.0,
            "Plano Diarista": 35.0
        }

        nome_plano_atual = self.servicos[0] if self.servicos else "Plano Basic"
        valor = precos_planos.get(nome_plano_atual, 90.0)

        if self.personal:
            if self.tipo_aluno.lower() == "diarista":
                valor += 50.0
            else:
                valor += 100.0

        return valor

    def exibir(self):
        print("\n" + "----------------------------------------")
        print("           INFORMAÇÕES DO ALUNO         ")
        print("----------------------------------------")
        print(f"Data de Matrícula: {self.data_matricula}")
        print(f"Nome: {self.nome}")
        print(f"Nome Social: {self.nome_social if self.nome_social else 'Nenhum'}")
        print(f"Idade: {self.idade}")
        print(f"Gênero: {self.genero}")
        print(f"Email: {self.email}")
        print(f"Contato: {self.contato}")
        print(f"Endereço: {self.endereco}")
        print(f"CPF: {self.CPF}")
        print(f"Tipo de Aluno: {self.tipo_aluno}")
        print(f"Plano Contratado: {self.servicos[0] if self.servicos else 'Nenhum'}")
        print(f"Necessidades Especiais: {self.necessidades_especiais if self.necessidades_especiais else 'Nenhuma'}")
        print(f"Personal Trainer: {self.personal if self.personal else 'Nenhum'}")
        print(f"Objetivo do Treino: {self.objetivo if self.objetivo else 'Não Informado'}")
        print(f"Forma de Pagamento: {self.forma_pagamento}")
        
        if self.forma_pagamento == "Cartão de Crédito" and self._numero_cartao:
            print(f"Dados do Cartão: Final {self._numero_cartao[-4:]} | Titular: {self._titular_cartao} | Validade: {self._validade_cartao}")
            
        print(f"Autodeclaração de Saúde: {'Apto (Sim)' if self.auto_declaracao_saude else 'Inapto (Não)'}")
        print(f"Status Pagamento: {self.status_pagamento}")
        print(f"Status do Aluno: {self.status}")
        print(f"Vencimento: Todo dia {self.dia_vencimento}")
        print(f"Valor Total Mensalidade: R$ {self.calcular_mensalidade():.2f}")
        print("----------------------------------------")

        if self.idade < 18:
            print("[ Informações do Responsável Legal ]")
            if self.autorizacao_responsavel:
                print("Status: AUTORIZADO PELO RESPONSÁVEL")
                print(f"Responsável: {self.nome_responsavel}")
                print(f"Contato do Responsável: {self.contato_responsavel}")
            else:
                print("Status: ❌ NÃO AUTORIZADO")
            print("----------------------------------------")