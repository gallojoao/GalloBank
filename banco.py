# Gallo Bank - Sistema de Gerenciamento Bancário

import uuid
from datetime import datetime

extrato = []
contas = []
numero_conta = 0

def criar_conta(cpf):
    global contas
    global numero_conta
    global usuarios

    usuario = next((u for u in usuarios if u['cpf'] == cpf), None)
    if not usuario:
        print("\nErro: CPF não cadastrado.\n")
        return contas

    numero_conta += 1
    agencia = "0001"
    contaformat = f"{numero_conta:04d}-{agencia}"
    usuario = next(u for u in usuarios if u['cpf'] == cpf)

    conta = {
        'cpf': cpf,
        'nome': usuario['nome'],
        'agencia': agencia,
        'numero_conta': numero_conta,
        'contaformat': contaformat
    }

    if numero_conta in [c['numero_conta'] for c in contas]:
        try:
            raise ValueError("Número da conta já cadastrado.")
        except ValueError as e:
            print(f"\nErro: {e}\n")
    else:
        print("\nConta cadastrada com sucesso.\n")
        contas.append(conta)
    return contas

usuarios = []

def criar_usuario(nome, data_nascimento, cpf, endereco):
    global usuarios
    
    cliente = {
        'nome': nome,
        'data_nascimento': data_nascimento,
        'cpf': cpf,
        'endereco': endereco
              }
    if cpf in [c['cpf'] for c in usuarios]:
        try:
            raise ValueError("CPF já cadastrado.")
        except ValueError as e:
            print(f"\nErro: {e}\n")
    else:
        print("\nUsuário cadastrado com sucesso.\n")
        usuarios.append(cliente)
    return usuarios

def gerar_transacao(tipo, valor):
    return {
        "id": str(uuid.uuid4())[:8],  # hash curta
        "tipo": tipo,
        "valor": valor,
        "data_hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

# Variáveis globais para armazenar depósitos, saques, saldo e limite
# Limite de depósito é de R$ 500,00 e o usuário pode realizar até 3 depósitos
# O saldo é atualizado a cada depósito ou saque realizado
# O extrato é atualizado com cada transação realizada
# O usuário pode consultar o extrato a qualquer momento
# O usuário pode realizar depósitos, saques e consultar o extrato
# O usuário pode sair do sistema a qualquer momento

deposito = []
saques = []
saldo = 0.0
limite = 500.0

def depositar(valor):
    global saldo
    if valor > 0 and valor <= limite:
        if len(deposito) >= 3:
            print("\nVocê já atingiu o limite de 3 depósitos.\n")
            return
        deposito.append(valor)
        saldo += valor
        transacao = gerar_transacao("Depósito", valor)
        extrato.append(transacao)
        print(f"\nDepósito de R$ {valor:.2f} realizado com sucesso! ID: {transacao['id']}\n")
    else:
        print("\nValor inválido para depósito.\n")

def sacar(valor):
    global saldo, saques
    if valor > 0 and valor <= saldo:
        saques.append(valor)
        saldo -= valor
        transacao = gerar_transacao("Saque", valor)
        extrato.append(transacao)
        print(f"\nSaque de R$ {valor:.2f} realizado com sucesso! ID: {transacao['id']}\n")
    else:
        print("\nValor de saque inválido. Verifique se o valor é positivo e menor ou igual ao seu saldo.\n")

def mostrar_extrato():
    if not extrato:
        print("\nNenhuma transação realizada.\n")
        return
    print("\n===== EXTRATO =====")
    print(f"{'Data/Hora':20} | {'Tipo':10} | {'Valor':>10} | {'ID':8}")
    print("-"*60)
    for transacao in extrato:
        print(f"{transacao['data_hora']:20} | {transacao['tipo']:10} | R$ {transacao['valor']:9.2f} | {transacao['id']:8}")
    print("="*60 + "\n")

def mostrar_contas():
    if not contas:
        print("\nNenhuma conta cadastrada.\n")
        return
    print("\n=== Contas cadastradas ===")
    for conta in contas:
        print("-" * 40)
        print(f"Cliente: {conta['nome']}")
        print(f"CPF: {conta['cpf']}")
        print(f"Conta/Agência: {conta['contaformat']}")
    print("-" * 40 + "\n")

print("Bem-vindo ao Gallo Bank!")
print("Você pode realizar até 3 depósitos de até R$ 500,00 cada.")
print(f"Seu saldo atual é R$ {saldo:.2f}")

menu = f"""
Escolha uma das opções abaixo:

1 - Depositar
2 - Sacar
3 - Extrato
4 - Sair
5 - Criar Conta
6 - Criar Usuário
7 - Listar Contas

Digite sua opção:

"""

while True:
    escolha = input(menu)

    if escolha == "1":
        print("Você escolheu Depositar")
        valor = float(input("Digite o valor do depósito: "))
        depositar(valor)
        print(f"Seu saldo atual é R$ {saldo:.2f}")
    elif escolha == "2":
        print("Você escolheu Sacar")
        valor = float(input("Digite o valor do saque: "))
        sacar(valor)
        print(f"Seu saldo atual é R$ {saldo:.2f}")
    elif escolha == "3":
        print("Você escolheu Extrato")
        mostrar_extrato()
    elif escolha == "4":
        print("Obrigado por usar o Gallo Bank!")
        break
    elif escolha == "5":
        print("Você escolheu Criar Conta")
        cpf = input("Digite o CPF do usuário: ")
        criar_conta(cpf)
    elif escolha == "6":
        print("Você escolheu Criar Usuário")
        nome = input("Digite o nome do usuário: ")
        data_nascimento = input("Digite a data de nascimento (DD/MM/AAAA): ")
        cpf = input("Digite o CPF do usuário: ")
        endereco = input("Digite o endereço do usuário: ")
        criar_usuario(nome, data_nascimento, cpf, endereco)
    elif escolha == "7":
        print("Você escolheu Listar Contas")
        mostrar_contas()

