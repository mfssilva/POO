from membro import Membro

class Personal(Membro):
    def __init__(self, nome, idade, genero, email, contato, endereco,
                 cpf, especialidade, valor, cref, banco, agencia, conta, taxa_academia,
                 nome_social = None, necessidades_especiais = None):
        
        super().__init__(nome, idade, genero, email, contato, endereco, cpf)
        self.especialidade = especialidade
        self.valor = valor
        self.cref = cref
        self.nome_social = nome_social
        self.necessidades_especiais = necessidades_especiais
        self._banco = banco
        self._agencia = agencia
        self._conta = conta
        self.taxa_academia = taxa_academia
        self.status = "credenciado"

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
        if self.status == "Suspenso":
            return 0.0
        return self.taxa_academia

    def vinculo_com_academia(self, status_vinculo):
        if self.status == "Suspenso":
            print(f"Aviso: O personal {self.nome} está suspenso e não pode atuar.")
            return
        self.status = status_vinculo.lower()

    def exibir(self):
        print("--" * 20)
        print("   INFORMAÇÕES DO PERSONAL TRAINER   ")
        print("--" * 20)
        print(f"Nome: {self.nome} | CREF: {self.cref}")
        print(f"Especialidade: {self.especialidade}")
        print(f"Valor cobrado por hora/aluno: R$ {self.valor:.2f}")
        
        # 🔥 CORREÇÃO AQUI: Tenta ler 'CPF' maiúsculo se o minúsculo não existir
        cpf_valido = getattr(self, 'CPF', None) or getattr(self, 'cpf', 'Não Informado')
        print(f"CPF: {cpf_valido} | Contato: {self.contato}")
        
        conta_oculta = f"***{self._conta[-4:]}" if len(self._conta) > 4 else "****"
        print(f"Dados Bancários: Banco {self._banco} | Ag: {self._agencia} | Conta: {conta_oculta}")
        
        print(f"Status do Credenciamento: {self.status}")
        print(f"Taxa Mensal Devida à Academia: R$ {self.calcular_mensalidade():.2f}")
        print("--" * 20)