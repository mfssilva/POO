import sys
import os
from datetime import datetime

raiz_projeto = os.path.dirname(os.path.abspath(__file__))
pasta_src = os.path.join(raiz_projeto, "src")
if pasta_src not in sys.path:
    sys.path.insert(0, pasta_src)

from aluno import Aluno
from funcionario import Funcionario  
from personal import Personal
from terceirizados import Terceirizado
from RH import RH

PRECO_PLANOS = {
    "1": ("Basic", 90.00),
    "2": ("Plus", 140.00),
    "3": ("Premium", 200.00),
    "4": ("Fidelidade", 220.00),
    "5": ("Diarista", 35.00)
}
TAXA_FIXA_PERSONAL = 250.00   
CUSTO_DIARIA_PRESTADOR = 80.00 

alunos_cadastrados = []
funcionarios_cadastrados = []
prestadores_cadastrados = []

personais_cadastrados = [
    Personal(nome="Moniq Peixoto", idade=25, genero="Feminino", email="moniq@fittrack.com", contato="85999991111", 
             endereco="Rua da Academia, 100", cpf="00000000001", especialidade="Musculacao", valor=0.0, 
             cref="CREF-000001", banco="Banco do Brasil", agencia="0001", conta="1000-1", taxa_academia=0.0),
    Personal(nome="Sthefany Silva", idade=24, genero="Feminino", email="sthefany@fittrack.com", contato="85999992222", 
             endereco="Rua da Academia, 100", cpf="00000000002", especialidade="Pilates / Funcional", valor=0.0, 
             cref="CREF-000002", banco="Itau", agencia="0001", conta="2000-2", taxa_academia=0.0),
    Personal(nome="David Wytalo", idade=27, genero="Masculino", email="david@fittrack.com", contato="85999993333", 
             endereco="Rua da Academia, 100", cpf="00000000003", especialidade="Cardio / HIIT", valor=0.0, 
             cref="CREF-000003", banco="Bradesco", agencia="0001", conta="3000-3", taxa_academia=0.0),
    Personal(nome="Zaion Luz", idade=26, genero="Masculino", email="zaion@fittrack.com", contato="85999994444", 
             endereco="Rua da Academia, 100", cpf="00000000004", especialidade="Crosstraining", valor=0.0, 
             cref="CREF-000004", banco="Santander", agencia="0001", conta="4000-4", taxa_academia=0.0)
]

def buscar_pessoa_por_cpf(cpf):
    for lista in [alunos_cadastrados, funcionarios_cadastrados, personais_cadastrados, prestadores_cadastrados]:
        for p in lista:
            p_cpf = getattr(p, 'CPF', None) or getattr(p, 'cpf', None)
            if p_cpf == cpf:
                return p
    return None

def ler_inteiro(mensagem):
    while True:
        try: return int(input(mensagem))
        except ValueError: print("❌ Erro: Digite um número inteiro válido.")

def validar_contato():
    while True:
        contato = input("Contato (Apenas numeros, minimo 8 digitos): ").strip()
        if contato.isdigit() and len(contato) >= 8: return contato
        print("❌ Contato Invalido!")

def validar_cpf():
    while True:
        cpf = input("CPF (Somente 11 numeros): ").strip()
        if cpf.isdigit() and len(cpf) == 11: return cpf
        print("❌ CPF Invalido! Digite exatamente 11 numeros.")

def validar_email():
    while True:
        email = input("Email: ").strip()
        if "@" in email and "." in email.split("@")[-1]: return email
        print("❌ Email Invalido!")

def capturar_endereco():
    print("\n[ Informacoes de Endereco ]")
    tipo = "Rua"
    opcao_tipo = input("Tipo: 1. Rua | 2. Avenida | 3. Outro: ").strip()
    if opcao_tipo == "2": tipo = "Avenida"
    elif opcao_tipo == "3": tipo = input("Digite o tipo: ").strip().capitalize()

    nome_logradouro = input(f"Nome do(a) {tipo}: ").strip()
    numero = input("Numero (Em branco para S/N): ").strip() or "S/N"
    bairro = input("Bairro: ").strip()
    
    while True:
        cep = input("CEP (Somente 8 numeros): ").strip()
        if len(cep) == 8 and cep.isdigit(): break
        print("❌ CEP Invalido!")
        
    return f"{tipo} {nome_logradouro}, No {numero}, Bairro: {bairro}, CEP: {cep}"

def validar_data(mensagem):
    while True:
        data_str = input(mensagem).strip()
        try:
            datetime.strptime(data_str, "%Y-%m-%d")
            return data_str
        except ValueError:
            print("❌ Use o formato AAAA-MM-DD.")

def validar_horario(mensagem):
    while True:
        hora_str = input(mensagem).strip()
        try:
            datetime.strptime(hora_str, "%H:%M")
            return hora_str
        except ValueError:
            print("❌ Use o formato HH:MM.")

def menu_cadastro_aluno():
    print("\n--- CADASTRO DE ALUNO ---")
    cpf = validar_cpf()
    pessoa_existente = buscar_pessoa_por_cpf(cpf)

    if pessoa_existente:
        print(f"⚠️ Resgatando dados de: {pessoa_existente.nome}")
        nome = pessoa_existente.nome
        idade = pessoa_existente.idade  
        genero = p_existente.genero if (p_existente := pessoa_existente) and hasattr(p_existente, 'genero') else "Nao Informado"
        email = pessoa_existente.email
        contato = pessoa_existente.contato
        endereco = pessoa_existente.endereco
        nome_social = getattr(pessoa_existente, 'nome_social', None)
    else:
        nome = input("Nome Completo: ").strip()
        nome_social = input("Nome Social (Em branco se nao houver): ").strip() or None
        idade = ler_inteiro("Idade: ")
        genero = input("Genero: ").strip()
        email = validar_email()
        contato = validar_contato()
        endereco = capturar_endereco()

    necessidades_especiais = input("Restricao medica? (Em branco se nao houver): ").strip() or None

    print("\n--- SELECAO DE PLANOS ---")
    for k, v in PRECO_PLANOS.items():
        print(f"{k}. {v[0]} - R$ {v[1]:.2f}")

    while True:
        op = input("Escolha o plano (1-5): ").strip()
        if op in PRECO_PLANOS:
            plano, valor_plano = PRECO_PLANOS[op]
            tipo_aluno = "DIARISTA" if op == "5" else "MENSALISTA"
            break
        print("❌ Opcao invalida!")

    auto_saude = (input("Declaracao de saude (APTO/INAPTO): ").strip().upper() == "APTO")
    objetivo = input("Objetivo do Treino: ").strip()
    forma_pagamento = input("Forma de Pagamento (Pix/Boleto/Cartao): ").strip()
    dia_vencimento = 10

    personal_vinculado = None
    vincular = input("Deseja treinar com personal? (S/N): ").strip().upper()

    if vincular == "S":
        print("\nDeseja treinar com os disponiveis da academia?")
        print("Digite o numero do profissional ou digite 'N' (Nao) para sair/informar outro:")
        
        for i, p in enumerate(personais_cadastrados, 1):
            print(f"{i}. {p.nome} (Especialidade: {p.especialidade})")
        
        escolha = input("Opcao: ").strip()
        
        if escolha.upper() == 'N':
            op_externo = input("Deseja informar um personal externo que nao esta na lista? (S/N): ").strip().upper()
            if op_externo == "S":
                personal_vinculado = input("Digite o nome do Personal Externo: ").strip()
        else:
            try:
                idx = int(escolha) - 1
                if 0 <= idx < len(personais_cadastrados):
                    personal_vinculado = personais_cadastrados[idx].nome
                    print(f"✅ Personal {personal_vinculado} vinculado com sucesso!")
                else:
                    print("❌ Opcao invalida! Nenhum personal foi vinculado.")
            except ValueError:
                print("❌ Opcao invalida! Nenhum personal foi vinculado.")

    nome_resp, contato_resp, autorizacao = None, None, False
    if idade < 18:
        nome_resp = input("Nome do Responsavel: ").strip()
        contato_resp = validar_contato()
        autorizacao = True

    try:
        aluno = Aluno(nome, idade, genero, email, contato, endereco, cpf, tipo_aluno, personal_vinculado,
                      autorizacao, nome_resp, contato_resp, nome_social, necessidades_especiais, forma_pagamento,
                      auto_saude, objective=objetivo, plano=plano, dia_vencimento=dia_vencimento)
        print(f"\n✅ Aluno matriculado!")
        aluno.exibir()
        return aluno
    except Exception as e:
        print(f"❌ Erro: {e}")
        return None

def menu_cadastro_funcionario():
    print("\n--- CADASTRO DE FUNCIONARIO ---")
    cpf = validar_cpf()
    
    for f in funcionarios_cadastrados:
        if (getattr(f, 'CPF', None) or getattr(f, 'cpf', None)) == cpf:
            if f.tipo_contrato == "ESTAGIARIO":
                if input(f"📈 Promover o estagiario {f.nome} para CLT? (S/N): ").strip().upper() == "S":
                    f.tipo_contrato = "CLT"
                    f.cargo = input("Novo Cargo CLT: ").strip()
                    f.salario_base = ler_inteiro("Novo Salario Base: R$ ")
                    print("🎉 Promovido com sucesso!")
                    f.exibir()
                return None
            print("❌ Ja cadastrado como CLT.")
            return None

    pessoa_existente = buscar_pessoa_por_cpf(cpf)
    if pessoa_existente:
        nome, idade = pessoa_existente.nome, pessoa_existente.idade
        genero = p_existente.genero if (p_existente := pessoa_existente) and hasattr(p_existente, 'genero') else "Nao Informado"
        email, contato, endereco = pessoa_existente.email, pessoa_existente.contato, pessoa_existente.endereco
    else:
        nome = input("Nome Completo: ").strip()
        idade = ler_inteiro("Idade: ")
        if idade < 14: print("❌ Proibido menor de 14 anos!"); return None
        genero = input("Genero: ").strip()
        email = validar_email()
        contato = validar_contato()
        endereco = capturar_endereco()

    tipo_contrato = "CLT" if input("Contrato: 1. CLT | 2. Estagio: ").strip() == "1" else "ESTAGIARIO"
    cargo = input("Cargo: ").strip()
    salario_base = ler_inteiro("Salario Base: R$ ")
    ctps = input("CTPS: ").strip()
    data_adm = datetime.now().strftime("%Y-%m-%d")
    h_entrada = validar_horario("Entrada (HH:MM): ")
    h_saida = validar_horario("Saida (HH:MM): ")
    banco, agencia, conta = input("Banco: ").strip(), input("Agencia: ").strip(), input("Conta: ").strip()

    nome_resp, contato_resp = (input("Responsavel Legal: ").strip(), validar_contato()) if idade < 18 else (None, None)

    try:
        novo_func = Funcionario(nome, idade, genero, email, contato, endereco, cpf, cargo, salario_base,
                                ctps, tipo_contrato, data_adm, h_entrada, h_saida, banco, agencia, conta,
                                nome_resp, contato_resp)
        print("\n✅ Funcionario cadastrado!")
        novo_func.exibir()
        return novo_func
    except Exception as e:
        print(f"❌ Erro: {e}")
        return None

def menu_cadastro_personal():
    print("\n--- CADASTRO DE PERSONAL TRAINER ---")
    cpf = validar_cpf()
    pessoa_existente = buscar_pessoa_por_cpf(cpf)

    if pessoa_existente:
        if pessoa_existente.idade < 18:
            print("❌ Erro: Menores de idade nao podem atuar como Personal.")
            return None
        nome, idade = pessoa_existente.nome, pessoa_existente.idade
        genero = p_existente.genero if (p_existente := presidential_var) and hasattr(p_existente, 'genero') else "Nao Informado"
        email, contato, endereco = presidential_var.email, presidential_var.contato, presidential_var.endereco if (presidential_var := pessoa_existente) else (None, None, None)
        nome_social = getattr(pessoa_existente, 'nome_social', None)
    else:
        nome = input("Nome Completo: ").strip()
        nome_social = input("Nome Social (Em branco se nao houver): ").strip() or None
        idade = ler_inteiro("Idade: ")
        if idade < 18: print("❌ Menores de idade nao podem possuir CREF."); return None
        genero = input("Genero: ").strip()
        email = validar_email()
        contato = validar_contato()
        endereco = capturar_endereco()

    especialidade = input("Especialidade: ").strip()
    valor_hora = ler_inteiro("Valor Cobrado por Hora/Aula: R$ ")
    cref = input("Registro CREF: ").strip()
    
    taxa_academia = TAXA_FIXA_PERSONAL 
    print(f"ℹ️ Taxa de uso do espaco fixada pelo sistema: R$ {taxa_academia:.2f}")

    banco, agencia, conta = input("Banco: ").strip(), input("Agencia: ").strip(), input("Conta: ").strip()

    try:
        novo_personal = Personal(nome=nome, idade=idade, genero=genero, email=email, contato=contato,
                                 endereco=endereco, cpf=cpf, especialidade=especialidade, valor=valor_hora,
                                 cref=cref, banco=banco, agencia=agencia, conta=conta, taxa_academia=taxa_academia,
                                 nome_social=nome_social)
        novo_personal.exibir()
        return novo_personal
    except Exception as e:
        print(f"❌ Erro: {e}")
        return None

def menu_cadastro_terceirizado():
    print("\n--- CADASTRO DE PRESTADOR DE SERVICO ---")
    cpf = validar_cpf()
    pessoa_existente = buscar_pessoa_por_cpf(cpf)

    if p_existente := pessoa_existente:
        nome, idade = p_existente.nome, p_existente.idade
        genero = p_existente.genero if hasattr(p_existente, 'genero') else "Nao Informado"
        email, contato, endereco = p_existente.email, p_existente.contato, p_existente.endereco
    else:
        nome = input("Nome Completo: ").strip()
        idade = ler_inteiro("Idade: ")
        genero = input("Genero: ").strip()
        email = validar_email()
        contato = validar_contato()
        endereco = capturar_endereco()
        
    regime = input("Regime (TERCEIRIZADO ou DIARISTA): ").strip().upper()
    
    if regime == "TERCEIRIZADO":
        empresa = input("Nome da Empresa Parceira: ").strip()
        valor_custo = ler_inteiro("Valor Mensal do Contrato de Repasse: R$ ")
    else:
        empresa = None
        valor_custo = CUSTO_DIARIA_PRESTADOR
        print(f"ℹ️ Custo da diaria predefinido pelo corporativo: R$ {valor_custo:.2f}")
        
    servico = input("Servico Prestado (Ex: Limpeza, Recepcao): ").strip()
    data_inicio = validar_data("Data de Inicio (AAAA-MM-DD): ")
    data_fim = validar_data("Data de Fim (AAAA-MM-DD): ")
    banco, agencia, conta = input("Banco: ").strip(), input("Agencia: ").strip(), input("Conta: ").strip()

    try:
        novo_prestador = Terceirizado(nome, idade, genero, email, contato, endereco, cpf, regime,
                                      servico, valor_custo, data_inicio, data_fim, banco, agencia, conta, empresa)
        print(f"\n✅ Prestador registrado!")
        novo_prestador.exibir()
        return novo_prestador
    except Exception as e:
        print(f"❌ Erro: {e}")
        return None

def main():
    while True:
        print("\n" + "="*40)
        print("   SISTEMA FITTRACK - GESTAO DE ACADEMIA   ")
        print("="*40)
        print("1. Cadastrar Aluno\n2. Cadastrar Funcionario\n3. Cadastrar Personal\n4. Cadastrar Prestador\n5. Sair")
        print("="*40)
        opcao = input("Opcao: ").strip()

        if opcao == "1":
            aluno = menu_cadastro_aluno()
            if aluno: alunos_cadastrados.append(aluno)
        elif opcao == "2":
            func = menu_cadastro_funcionario()
            if func: funcionarios_cadastrados.append(func)
        elif opcao == "3":
            personal = menu_cadastro_personal()
            if personal: personais_cadastrados.append(personal)
        elif opcao == "4":
            prestador = menu_cadastro_terceirizado()
            if prestador: prestadores_cadastrados.append(prestador)
        elif opcao == "5":
            break
        else:
            print("❌ Opcao invalida!")

if __name__ == "__main__":
    main()