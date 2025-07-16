# GalloBank - Sistema Bancário com Orientação a Objetos Avançada
from abc import ABC, abstractmethod
from datetime import datetime

# ============================
# CLASSES DE DOMÍNIO PRINCIPAIS
# ============================

class Cliente:
    def __init__(self, nome, data_nascimento, cpf):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def __str__(self):
        return f"Cliente: {self.nome}, CPF: {self.cpf}, Data de Nascimento: {self.data_nascimento}"


class Conta:
    _contador_contas = 0

    def __init__(self, cliente):
        Conta._contador_contas += 1
        self.numero = Conta._contador_contas
        self.agencia = "0001"
        self._cliente = cliente
        self._saldo = 0.0
        self._historico = Historico()
        self._limite_depositos = 3
        self._depositos_realizados = 0

    @property
    def saldo(self):
        return self._saldo

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def depositar(self, valor):
        if self._depositos_realizados >= self._limite_depositos:
            print("❌ Limite de depósitos diários atingido.")
            return False
        if valor > 0 and valor <= 500.00:
            self._saldo += valor
            self._depositos_realizados += 1
            print(f"✅ Depósito de R${valor:.2f} realizado com sucesso!")
            return True
        print("❌ Valor de depósito inválido ou acima do limite.")
        return False

    def sacar(self, valor):
        if valor <= 0:
            print("❌ Valor de saque inválido.")
            return False
        if valor > self._saldo:
            print("❌ Saldo insuficiente.")
            return False
        self._saldo -= valor
        print(f"✅ Saque de R${valor:.2f} realizado com sucesso!")
        return True

    def __str__(self):
        return f"Conta {self.numero}-{self.agencia}\n{self.cliente.nome}, CPF: {self.cliente.cpf} | Saldo: R${self._saldo:.2f}"


class Historico:
    def __init__(self):
        self._transacoes = []

    def adicionar(self, transacao):
        self._transacoes.append({
            "tipo": transacao.__class__.__name__,
            "valor": transacao.valor,
            "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        })

    def exibir(self):
        if not self._transacoes:
            print("Nenhuma transação realizada.")
            return
        print(f"{'Tipo':<10} {'Valor':<10} {'Data/Hora':<20}")
        print("-" * 50)
        for t in self._transacoes:
            print(f"{t['tipo']:<10} R${t['valor']:<10.2f} {t['data']:<20}")
        print("-" * 50)


# ============================
# TRANSACOES ABSTRATAS E CONCRETAS
# ============================

class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        if conta.depositar(self._valor):
            conta.historico.adicionar(self)


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        if conta.sacar(self._valor):
            conta.historico.adicionar(self)


# ============================
# INTERFACE DE USUÁRIO
# ============================

clientes = []
contas = []

def criar_conta():
    nome = input("Nome: ")
    data_nascimento = input("Data de nascimento (DD/MM/AAAA): ")
    cpf = input("CPF: ")
    cliente = Cliente(nome, data_nascimento, cpf)
    conta = Conta(cliente)
    cliente.adicionar_conta(conta)
    clientes.append(cliente)
    contas.append(conta)
    print(f"✅ Conta criada com sucesso: {conta}")

def localizar_conta():
    numero = int(input("Número da conta: "))
    for conta in contas:
        if conta.numero == numero:
            return conta
    print("❌ Conta não encontrada.")
    return None

def menu():
    print("\n🏦 Bem-vindo ao GalloBank Avançado!")
    print("Limites: 3 depósitos diários, R$500,00 por depósito.")
    print("1. Criar conta")
    print("2. Depositar")
    print("3. Sacar")
    print("4. Consultar extrato")
    print("q. Sair")
    return input("Escolha uma opção: ")

def main():
    while True:
        opcao = menu()
        if opcao == '1':
            criar_conta()
        elif opcao == '2':
            conta = localizar_conta()
            if conta:
                valor = float(input("Valor do depósito: "))
                Deposito(valor).registrar(conta)
        elif opcao == '3':
            conta = localizar_conta()
            if conta:
                valor = float(input("Valor do saque: "))
                Saque(valor).registrar(conta)
        elif opcao == '4':
            conta = localizar_conta()
            if conta:
                print(f"\n📄 Extrato da Conta {conta.numero}-{conta.agencia}")
                conta.historico.exibir()
        elif opcao == 'q':
            print("👋 Encerrando o sistema. Até logo!")
            break
        else:
            print("❗ Opção inválida.")

if __name__ == "__main__":
    main()
