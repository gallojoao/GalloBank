# Gallo Bank - Sistema de Gerenciamento Bancário

import uuid
from datetime import datetime

extrato = []

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
            print("Você já atingiu o limite de 3 depósitos.")
            return
        deposito.append(valor)
        saldo += valor
        transacao = gerar_transacao("Depósito", valor)
        extrato.append(transacao)
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso! ID: {transacao['id']}")
    else:
        print("Valor inválido para depósito.")

def sacar(valor):
    global saldo, saques
    if valor > 0 and valor <= saldo:
        saques.append(valor)
        saldo -= valor
        transacao = gerar_transacao("Saque", valor)
        extrato.append(transacao)
        print(f"Saque de R$ {valor:.2f} realizado com sucesso! ID: {transacao['id']}")
    else:
        print("Valor de saque inválido. Verifique se o valor é positivo e menor ou igual ao seu saldo.")
def mostrar_extrato():
    if not extrato:
        print("Nenhuma transação realizada.")
        return
    print("Extrato de Transações:")
    print("\n===== EXTRATO =====")
    for transacao in extrato:
        print(f"{transacao['data_hora']} | {transacao['tipo']:10} | R$ {transacao['valor']:.2f} | ID: {transacao['id']}")
    print("===================\n")


# Exibição do menu e opções de interação com o usuário

print("Bem-vindo ao Gallo Bank!")
print("Você pode realizar até 3 depósitos de até R$ 500,00 cada.")
print(f"Seu saldo atual é R$ {saldo:.2f}")
menu = f"""
Escolha uma das opções abaixo:

1 - Depositar
2 - Sacar
3 - Extrato
4 - Sair

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