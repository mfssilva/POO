from datetime import datetime

class RH:
    def registrar_ponto(self, funcionario, horas_trabalhadas):
        if "Demitido" in funcionario.status:
            print(f"ERRO RH: Não é possível registrar ponto de {funcionario.nome}. Funcionário desligado.")
            return

        if funcionario.tipo_contrato == "ESTAGIARIO" and horas_trabalhadas > 4:
            print(f"ALERTA RH: O estagiário {funcionario.nome} não pode trabalhar mais de 4 horas por dia!")
            funcionario.horas_acumuladas += 4
            return

        if funcionario.tipo_contrato == "CLT":
            if horas_trabalhadas > 8:
                horas_extras = horas_trabalhadas - 8
                funcionario.horas_acumuladas += horas_extras
                print(f"RH: {funcionario.nome} realizou {horas_extras}h extras hoje.")
                
                if funcionario.horas_acumuladas >= 8:
                    funcionario.banco_folgas += 1
                    funcionario.horas_acumuladas -= 8
                    print(f"NOTIFICAÇÃO RH: {funcionario.nome} acumulou 8h extras e ganhou 1 folga no banco.")
            else:
                print(f"RH: Ponto registrado normalmente para {funcionario.nome} ({horas_trabalhadas}h trabalhadas).")

    def aplicar_advertencia(self, funcionario, motivo):
        if "Demitido" in funcionario.status:
            print(f"ERRO RH: Não é possível aplicar advertência. {funcionario.nome} já está desligado.")
            return

        if not hasattr(funcionario, 'advertencias'):
            funcionario.advertencias = 0
            
        funcionario.advertencias += 1
        print(f"NOTIFICAÇÃO RH: Advertência escrita aplicada a {funcionario.nome}. Motivo: {motivo}. Total: {funcionario.advertencias}/3")
        
        if funcionario.advertencias >= 3:
            funcionario.status = "Demitido - Justa Causa"
            print(f"🚨🚨 ALERTA MÁXIMO RH: O funcionário {funcionario.nome} foi DEMITIDO POR JUSTA CAUSA devido ao acúmulo de 3 advertências escritas!")

    def calcular_fgts(self, funcionario):
        if funcionario.tipo_contrato != "CLT":
            return f"Funcionário {funcionario.nome} é {funcionario.tipo_contrato}. Não possui direito ao recolhimento de FGTS."
            
        fgts_mensal = funcionario.salario_base * 0.08
        
        data_admissao = datetime.strptime(funcionario.data_contratacao, "%Y-%m-%d")
        data_atual = datetime.now()
        dias_trabalhados = (data_atual - data_admissao).days
        meses_trabalhados = max(1, dias_trabalhados // 30)
        
        fgts_acumulado = fgts_mensal * meses_trabalhados
        
        print(f"--- EXTRATO FGTS: {funcionario.nome} ---")
        print(f"Depósito Mensal (8%): R$ {fgts_mensal:.2f}")
        print(f"Tempo de Contribuição: {meses_trabalhados} meses")
        print(f"Saldo Total Estimado em Conta FGTS: R$ {fgts_acumulado:.2f}")
        return fgts_acumulado

    def gerenciar_sobre_aviso(self, funcionario, status):
        if "Demitido" in funcionario.status or funcionario.tipo_contrato == "ESTAGIARIO":
            print(f"ERRO RH: Estagiários ou funcionários demitidos não entram em regime de sobre-aviso.")
            return
        funcionario.sobre_aviso = status

    def calcular_direito_ferias(self, funcionario, vendeu_ferias=False):
        if "Demitido" in funcionario.status:
            print("Funcionário já desligado da empresa.")
            return 0

        data_admissao = datetime.strptime(funcionario.data_contratacao, "%Y-%m-%d")
        data_atual = datetime.now()
        dias_trabalhados = (data_atual - data_admissao).days
        
        print(f"--- ANÁLISE DE FÉRIAS: {funcionario.nome} ---")
        print(f"Tempo de casa: {dias_trabalhados} dias.")
        
        if dias_trabalhados >= 365:
            print("Status Férias: Direito a férias adquirido (Período Aquisitivo Completo).")
            
            if funcionario.tipo_contrato == "CLT":
                if vendeu_ferias:
                    dias_descanso = 20
                    dias_vendidos = 10
                    valor_abono = (funcionario.salario_base / 30) * 10
                    valor_abono_com_terco = valor_abono + (valor_abono / 3)
                    
                    print(f"Opção Escolhida: Venda de 1/3 das férias (Abono Pecuniário).")
                    print(f"   Dias de descanso: {dias_descanso} dias.")
                    print(f"   Dias vendidos: {dias_vendidos} dias.")
                    print(f"   Valor extra a receber pelas férias vendidas: R$ {valor_abono_com_terco:.2f}")
                    return dias_descanso
                else:
                    print("Opção Escolhida: Tirar os 30 dias completos de descanso.")
                    return 30
            else:
                print("Contrato de Estágio: Direito a 30 dias de recessos (Não permite venda).")
                return 30
        else:
            dias_restantes = 365 - dias_trabalhados
            print(f"Status Férias: Em período aquisitivo. Faltam {dias_restantes} dias para o direito.")
            return 0

    def gerar_escala(self, funcionario, dias_semana):
        if "Demitido" in funcionario.status:
            return
        print(f"ESCALA DE TRABALHO DE {funcionario.nome.upper()}:")
        print(f"Dias da Semana: {dias_semana}")
        print(f"Turno: {funcionario.horario_entrada} às {funcionario.horario_saida}")