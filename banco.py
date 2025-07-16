# GalloBank - Sistema Bancário Simples
# Este é um sistema bancário simples que permite criar contas, realizar depósitos, saques e consultar extratos.
# O sistema registra transações com ID, tipo, valor e data/hora

# Projeto desenvolvido para fins educacionais.

# Importando bibliotecas necessárias
from datetime import datetime
import uuid

# Listas para armazenar contas e clientes
contas = []
clientes = []

# Definindo a classe Cliente
class Cliente:
    # Inicializa o cliente com nome, data de nascimento e CPF
    def __init__(self, nome, data_nascimento, cpf):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

    # Representação em string do cliente
    def __str__(self):
        return f"Cliente: {self.nome}, CPF: {self.cpf}, Data de Nascimento: {self.data_nascimento}"

# Definindo a classe Transacao para registrar transações bancárias
class Transacao:
    # Inicializa a transação com tipo, valor e gera um ID único
    def __init__(self, tipo, valor):
        self.id = str(uuid.uuid4())[:8]
        self.tipo = tipo
        self.valor = valor
        self.data_hora = datetime.now()

    # Representação em string da transação
    def __str__(self):
        return f"{self.id:<10} {self.tipo:<10} R${self.valor:<10.2f} {self.data_hora.strftime('%d/%m/%Y %H:%M:%S')}"

# Definindo a classe Conta que herda de Cliente
class Conta(Cliente):
    _contador_contas = 0

    # Inicializa a conta com os dados do cliente e define saldo, agência e contador de depósitos
    def __init__(self, nome, data_nascimento, cpf, agencia="0001"):
        super().__init__(nome, data_nascimento, cpf)
        Conta._contador_contas += 1
        self.numero_conta = Conta._contador_contas
        self.agencia = agencia
        self.saldo = 0.0
        self._contador_depositos = 0
        self.transacoes = []

    # Método para depositar valores na conta
    def depositar(self, valor):
        LIMITE = 3
        LIMITE_DEPOSITO = 500.00

        # Verifica se o limite de depósitos diários foi atingido 
        if self._contador_depositos >= LIMITE:
            print("❌ Limite de depósitos diários atingido.")
            return

        # Verifica se o valor do depósito está dentro do limite permitido
        if 0 < valor <= LIMITE_DEPOSITO:
            self.saldo += valor
            self._contador_depositos += 1
            transacao = Transacao("Depósito", valor)
            self.transacoes.append(transacao)
            print(f"✅ Depósito de R${valor:.2f} realizado com sucesso. Transação ID: {transacao.id}")
        else:
            print("❌ Valor de depósito acima do limite permitido.")

    # Método para sacar valores da conta
    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            transacao = Transacao("Saque", valor)
            self.transacoes.append(transacao)
            print(f"✅ Saque de R${valor:.2f} realizado com sucesso. Transação ID: {transacao.id}")
        else:
            print("❌ Saldo insuficiente ou valor inválido.")

    # Representação em string da conta
    def __str__(self):
        return f"Conta {self.numero_conta}-{self.agencia}\n{self.nome}, CPF: {self.cpf} | Saldo: R${self.saldo:.2f}"

# Função para criar uma nova conta
def criar_conta(nome, data_nascimento, cpf):
    cliente = Cliente(nome, data_nascimento, cpf)
    conta = Conta(cliente.nome, cliente.data_nascimento, cliente.cpf)
    contas.append(conta)
    clientes.append(cliente)
    print(f"✅ Conta criada com sucesso: {conta}")
    return conta

# Função para consultar o extrato de uma conta
def consultar_extrato(numero_conta):
    for conta in contas:
        if conta.numero_conta == numero_conta:
            print(f"\n📄 Extrato da Conta {conta.numero_conta}-{conta.agencia}")
            print(f"Cliente: {conta.nome}, CPF: {conta.cpf}")
            print(f"Saldo atual: R${conta.saldo:.2f}\n")
            if not conta.transacoes:
                print("Nenhuma transação realizada.")
            else:
                print(f"{'ID':<10} {'Tipo':<10} {'Valor':<10} {'Data/Hora':<20}")
                print("-" * 60)
                for t in conta.transacoes:
                    print(t)
                print("-" * 60)
            return
    print("❌ Conta não encontrada.")

# Função para exibir o menu principal
def menu():
    print("\n🏦 Bem-vindo ao GalloBank!")
    print("Limite de depósito: R$ 500,00. Você pode realizar até 3 depósitos por dia.")
    print("\nMenu:")
    print("1. Criar Conta")
    print("2. Depositar")
    print("3. Sacar")
    print("4. Consultar Saldo")
    print("5. Consultar Extrato")
    print("q. Sair")
    return input("Escolha uma opção: ")

# Função principal que executa o sistema bancário
def main():
    while True:
        escolha = menu()

        if escolha == '1':
            nome = input("Digite o nome do cliente: ")
            data_nascimento = input("Digite a data de nascimento (DD/MM/AAAA): ")
            cpf = input("Digite o CPF: ")
            criar_conta(nome, data_nascimento, cpf)

        elif escolha == '2':
            if not contas:
                print("❗ Nenhuma conta cadastrada. Crie uma conta primeiro.")
                continue
            print("Contas disponíveis:")
            for conta in contas:
                print(f"{conta.numero_conta} - {conta.nome}")
            numero_conta = int(input("Digite o número da conta: "))
            valor = float(input("Digite o valor do depósito: "))
            for conta in contas:
                if conta.numero_conta == numero_conta:
                    conta.depositar(valor)
                    break
            else:
                print("❌ Conta não encontrada.")

        elif escolha == '3':
            numero_conta = int(input("Digite o número da conta: "))
            valor = float(input("Digite o valor do saque: "))
            for conta in contas:
                if conta.numero_conta == numero_conta:
                    conta.sacar(valor)
                    break
            else:
                print("❌ Conta não encontrada.")

        elif escolha == '4':
            numero_conta = int(input("Digite o número da conta: "))
            for conta in contas:
                if conta.numero_conta == numero_conta:
                    print(f"Saldo atual: R${conta.saldo:.2f}")
                    break
            else:
                print("❌ Conta não encontrada.")

        elif escolha == '5':
            numero_conta = int(input("Digite o número da conta para consultar o extrato: "))
            consultar_extrato(numero_conta)

        elif escolha == 'q':
            print("👋 Saindo do sistema. Até logo!")
            break

        else:
            print("❗ Opção inválida. Tente novamente.")

# Executa a função principal se o script for executado diretamente
if __name__ == "__main__":
    main()