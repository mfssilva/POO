# Guia 5 — Projeto de Sistema com Orientação a Objetos

## Contexto

O **FitTrack** é um sistema completo de gestão de unidades fitness desenvolvido em Python. O projeto consolida e aplica na prática os conceitos fundamentais do paradigma de Orientação a Objetos (POO): classes, objetos, construtores, métodos, encapsulamento, atributos de classe, herança, polimorfismo e composição.

O foco da aplicação é centralizar o ecossistema corporativo de uma academia, gerenciando de forma inteligente o cruzamento de dados de pessoas pelo CPF e automatizando regras de negócios e contratuais.

---

## 1. Diagrama UML

### Diagrama de Classes Principal

```text
                  +-----------------------------------+
                  |              Membro               |
                  |-----------------------------------|
                  | - nome: str                       |
                  | - idade: int                      |
                  | - genero: str                     |
                  | - email: str                      |
                  | - contato: str                    |
                  | - endereco: str                   |
                  | - CPF: str                        |
                  +-----------------------------------+
                                    |
         +--------------------------+--------------------------+
         |                          |                          |
         v                          v                          v
+-----------------+       +-------------------+       +-----------------+
|      Aluno      |       |    Funcionario    |       |    Personal     |
|-----------------|       |-------------------|       |-----------------|
| - plano: str    |       | - cargo: str      |       | - cref: str     |
| - tipo_aluno:str|       | - salario_base:flt|       | - valor_hora:flt|
| - personal_vinc |       | - tipo_contrato:st|       | - taxa_academia |
+-----------------+       +-------------------+       +-----------------+
                                    |
                                    v
                          +-------------------+
                          |   Terceirizado    |
                          |-------------------|
                          | - regime: str     |
                          | - servico: str    |
                          | - valor_custo: flt|
                          +-------------------+
Descrição das Classes
Membro: Classe base abstrata que define o contrato comum e armazena os dados cadastrais obrigatórios de qualquer indivíduo vinculado à instituição.

Aluno: Herda de Membro. Adiciona regras de matrícula, seleção automatizada de planos e vinculação direta com a equipe interna ou personais cadastrados externos.

Funcionario: Herda de Membro. Representa o corpo de colaboradores corporativos da empresa, dividindo-os nos regimes de contratação CLT ou Estágio.

Personal: Herda de Membro. Representa os profissionais credenciados que utilizam a infraestrutura da academia mediante uma taxa mensal tabelada de uso de espaço.

Terceirizado: Herda de Funcionario/Membro. Gerencia prestadores de serviço externos atuando sob regime Terceirizado Contratual ou Diarista Autônomo.

RH: Classe utilitária baseada em composição e métodos específicos para realizar rotinas trabalhistas como registro de ponto, cálculo de FGTS e férias.

Esquema de Pastas do Projeto
Plaintext
academia/
├── src/
│   ├── __init__.py
│   ├── aluno.py
│   ├── funcionario.py
│   ├── membro.py
│   ├── personal.py
│   ├── RH.py
│   └── terceirizados.py
├── tests/
│   ├── __init__.py
│   ├── test_aluno.py
│   ├── test_funcionario.py
│   ├── test_personal.py
│   └── test_terceirizados.py
├── requirements.txt
├── Guia5_FitTrack_README.md
└── main.py
Como preparar o ambiente
Siga rigorosamente a sequência descrita abaixo para garantir a reprodutibilidade da aplicação em qualquer ambiente de desenvolvimento do Professor Raimundo Valter.

1. Criar ambiente virtual (venv)
O ambiente virtual isola as execuções do sistema da instalação global do Python na máquina, prevenindo conflitos de escopo. Na pasta raiz do projeto (..\academia>), execute o comando para construir a pasta isolada:

Bash
python -m venv .venv
2. Ativar ambiente
A activation direciona o terminal para utilizar os binários e scripts contidos dentro do diretório virtualizado criado.

Windows
Na pasta raiz do projeto, execute o comando via CMD ou PowerShell:

DOS
.\.venv\Scripts\activate
Linux/macOS
Na pasta raiz do projeto, execute o comando:

Bash
source .venv/bin/activate
3. Instalar dependências
O arquivo requirements.txt mapeia a lista de dependências externas do projeto. Como a arquitetura do FitTrack priorizou a performance e a portabilidade utilizando apenas pacotes nativos da biblioteca padrão do Python (como unittest, sys, os e datetime), o arquivo atua de forma descritiva e garante que nenhuma biblioteca externa seja baixada sem necessidade.

Para executar o leitor de dependências padrão, utilize:

Bash
pip install -r requirements.txt
4. Testes
A suíte de testes automatizados foi dividida de forma modular em arquivos independentes por entidade. Ela valida as regras de negócio individuais (como o cálculo de taxas de personais, regras contratuais e upgrades do RH) aplicando conceitos robustos de cobertura de código.

Para rodar a validação em lote e obter o relatório detalhado de acertos no terminal, execute o comando de descoberta automática:

Bash
python -m unittest discover -s tests -v
5. Execução
Para iniciar o sistema interativo em modo terminal, execute o arquivo principal:

Bash
python main.py
Na tela que abrir, você poderá interagir com o sistema por meio de um menu numérico (1 a 5). O usuário poderá experimentar as seguintes funcionalidades inteligentes:

Vitrine e Equipe Fixa de Personal Trainers (Opção 1): Ao matricular um aluno e optar por vincular um Personal Trainer, o sistema atua como uma plataforma e lista de forma nativa e automatizada a equipe interna pré-configurada da academia (Moniq Peixoto, Sthefany Silva, David Wytalo e Zaion Luz) exibindo também suas especialidades. O sistema permite escolher um profissional pelo seu número identificador ou recusar a lista digitando 'N' para incluir um profissional externo de sua livre escolha.

Cadastro Inteligente por CPF (Opção 1, 2, 3 e 4): Se você cadastrar um Personal Trainer parceiro com um CPF específico (Opção 3) e, em seguida, tentar matricular um Aluno (Opção 1) com esse mesmo CPF, o sistema identificará o registro existente e reaproveitará todos os dados pessoais básicos automaticamente, eliminando a digitação redundante. Novos profissionais cadastrados via menu passam a fazer parte dinamicamente da vitrine de ofertas para futuros alunos.

Upgrade de Contrato de Estágio para CLT (Opção 2): Ao tentar cadastrar um funcionário com um CPF que já pertence a um Estagiário ativo, o sistema oferecerá um fluxo automático de promoção para CLT, solicitando apenas o novo cargo e o novo salário-base.

Precificação Corporativa Automatizada: Ao selecionar os planos de alunos ou o regime de diaristas terceirizados, o sistema injetará de forma autônoma os custos de diárias (R$ 80,00) e taxas de espaço (R$ 250,00), impedindo que o operador insira valores manuais arbitrários.

Validações de Idades Legais: O sistema barra automaticamente credenciamentos de Personal Trainers menores de 18 anos e bloqueia vínculos de trabalho para menores de 14 anos, exigindo também dados de responsáveis legais para alunos menores de idade.