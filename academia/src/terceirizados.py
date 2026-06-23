from membro import Membro
from datetime import datetime

class Terceirizado(Membro):
    def __init__(self, nome, idade, genero, email, contato, endereco, CPF, regime_contratacao, 
                 servico_prestado, 
                 valor_servico, data_inicio, data_fim, banco, agencia, conta, empresa = None, 
                 nome_social = None, necessidades_especiais = None):
        super().__init__(nome, idade, genero, email, contato, endereco, CPF)
        
        self.regime_contratacao = regime_contratacao.upper()
        
        if self.regime_contratacao == "DIARISTA":
            self.empresa = "Contratação Direta (Autônomo)"
        else:
            self.empresa = empresa if empresa else "Não Informada"
            
        self.servico_prestado = servico_prestado
        self.valor_servico = valor_servico
        self.data_inicio = data_inicio  
        self.data_fim = data_fim        
        self.nome_social = nome_social
        self.necessidades_especiais = necessidades_especiais
        self.status = "Ativo"
        
    
        self._banco = banco
        self._agencia = agencia
        self._conta = conta

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
        if self.status == "Serviço Concluído":
            return 0.0
        return self.valor_servico

    def verificar_acesso(self):
        if self.status == "Serviço Concluído":
            return "Bloqueado - Serviço já finalizado"
            
        data_atual = datetime.now()
        data_limite = datetime.strptime(self.data_fim, "%Y-%m-%d")
        
        if data_atual > data_limite:
            self.status = "Serviço Concluído"
            return "Bloqueado - Prazo de contrato expirado"
            
        return "Liberado - Prestação de serviço ativa"

    def finalizar_servico(self):
        self.status = "Serviço Concluído"

    def exibir(self):
        print("--" * 20)
        print(f"   INFORMAÇÕES DO PRESTADOR ({self.regime_contratacao})   ")
        print("--" * 20)
        print(f"Nome: {self.nome}")
        print(f"Tipo de Vínculo: {self.regime_contratacao}")
        
        # MOSTRA A EMPRESA DE ORIGEM DE FORMA EXPLICITA
        print(f"Empresa de Origem: {self.empresa}") 
        
        print(f"Serviço a Realizar: {self.servico_prestado}")
        print(f"Período de Acesso: {self.data_inicio} até {self.data_fim}")
        cpf_valido = getattr(self, 'CPF', None) or getattr(self, 'cpf', 'Não Informado')
        print(f"CPF: {cpf_valido}")
        
        conta_oculta = f"***{self._conta[-4:]}" if len(self._conta) > 4 else "****"
        print(f"Dados para Pagamento: Banco {self._banco} | Ag: {self._agencia} | Conta: {conta_oculta}")
        print(f"Acesso à Portaria: {self.verificar_acesso()}")
        print(f"Status do Trabalho: {self.status}")
        print(f"Valor a Receber pelo Período/Diária: R$ {self.calcular_mensalidade():.2f}")
        print("--" * 20)