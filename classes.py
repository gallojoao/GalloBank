from datetime import datetime
import uuid 

contas = []
clientes = []

class Cliente:
    def __init__(self, nome, data_nascimento, cpf):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

    def __str__(self):
        return f"Cliente: {self.nome}, CPF: {self.cpf}, Data de Nascimento: {self.data_nascimento}"
    
class Conta(Cliente):
    _contador_contas = 0  # Atributo de classe (compartilhado entre todas as instâncias)
    

    def __init__(self, nome, data_nascimento, cpf, agencia="0001"):
        super().__init__(nome, data_nascimento, cpf)
        
        Conta._contador_contas += 1  # Incrementa o número de contas
        self.numero_conta = Conta._contador_contas  # Atribui o número atual à nova conta
        
        self.agencia = agencia
        self.saldo = 0.0
        self._contador_depositos = 0

    def gerar_transacao_id(self):
        return str(uuid.uuid4())[:8]  # Gera um ID de transação curto
    
    
    def depositar(self, valor):
        LIMITE = 3  # Limite de depositos por dia
        LIMITE_DEPOSITO = 500.00  # Limite de depósito por dia

        self.tipo = "depósito"
        if self._contador_depositos >= LIMITE:
            print("Limite de depósitos diários atingido.")
            return
        elif 0 < valor <= LIMITE_DEPOSITO:
            self.saldo += valor 
            self._contador_depositos += 1  # Incrementa o contador de depósitos
            self.id = self.gerar_transacao_id()  # Gera um ID de transação
            print(f"Depósito de R${valor:.2f} realizado com sucesso. Depositos realizados: {self._contador_depositos}\n Transação ID: {self.id} Tipo: {self.tipo}")
        else:
            print("Valor de depósito acima do limite permitido.")

    def sacar(self, valor):
        self.tipo = "saque"
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            self.id = self.gerar_transacao_id()  # Gera um ID de transação
            print(f"Saque de R${valor:.2f} realizado com sucesso. Transação ID: {self.id} Tipo: {self.tipo}")
        else:
            print("Saldo insuficiente ou valor inválido.")

    def __str__(self):
        return f"Conta {self.numero_conta}-{self.agencia}\n{self.nome}, CPF: {self.cpf} | Saldo: R${self.saldo:.2f}"
    

#cliente1 = Cliente("João Silva", "01/01/1990", "123.456.789-00")
#conta1 = Conta(cliente1.nome, cliente1.data_nascimento, cliente1.cpf)
#
#cliente2 = Cliente("Maria Oliveira", "02/02/1992", "987.654.321-00")
#conta2 = Conta(cliente2.nome, cliente2.data_nascimento, cliente2.cpf)
#
#print(cliente1)
#print(conta1)
#
#conta1.depositar(500.00)  # Depósito válido
#conta1.depositar(200.00)  # Depósito válido
#conta1.depositar(600.00)
#conta1.depositar(500.00)  # Tentativa de depósito acima do limite
#conta1.depositar(100.00)  # Tentativa de depósito após atingir o limite
#
#print(conta1.saldo)
#conta1.sacar(200.00)  # Saque válido
#print(conta1.saldo)

def criar_conta(nome, data_nascimento, cpf):
    global contas
    global clientes
    
    cliente = Cliente(nome, data_nascimento, cpf)
    conta = Conta(cliente.nome, cliente.data_nascimento, cliente.cpf)
    
    contas.append(conta)
    clientes.append(cliente)
    
    print(f"Conta criada com sucesso: {conta}")
    return conta

def  consultar_extrato(numero_conta):
    global contas
    for conta in contas:
        if conta.numero_conta == numero_conta:
            print(f"Extrato da conta {conta.numero_conta}-{conta.agencia}:\n")
            print(f"Cliente: {conta.nome}, CPF: {conta.cpf}")
            print(f"Saldo atual: R${conta.saldo:.2f}")
            if conta._contador_depositos == 0:
                print("Nenhuma transação realizada hoje.")
            else:
                print(f"Depósitos realizados: {conta._contador_depositos}")
                print("Transações:")
                print(f"{'ID':<10} {'Tipo':<10} {'Valor':<10} {'Data/Hora':<20}")
                print("-" * 60)
                for transacao in conta.depositar.__self__.__dict__.get('_contador_depositos', []):
                    print(f"{transacao.id:<10} {transacao.tipo:<10} {transacao.valor:<10} {datetime.now().strftime('%d/%m/%Y %H:%M:%S'):<20}")
                print("-" * 60)
            return
        print("Conta não encontrada.")

def menu():
    print("\nBem-vindo ao Sistema Bancário!")

    print("Limite de depósito: R$ 500,00. Você pode realizar até 3 depósitos por dia.")

    print("\nMenu:")
    print("1. Criar Conta")
    print("2. Depositar")
    print("3. Sacar")
    print("4. Consultar Saldo")
    print("5. Consultar Extrato")

    print("q. Sair")

    escolha = input("Escolha uma opção: ")
    return escolha

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
                print("Nenhuma conta cadastrada. Por favor, crie uma conta primeiro.")
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
                    print("Conta não encontrada.")
        
        elif escolha == '3':
            numero_conta = int(input("Digite o número da conta: "))
            valor = float(input("Digite o valor do saque: "))
            for conta in contas:
                if conta.numero_conta == numero_conta:
                    conta.sacar(valor)
                    break
                else:
                    print("Conta não encontrada.")
        
        elif escolha == '4':
            numero_conta = int(input("Digite o número da conta: "))
            for conta in contas:
                if conta.numero_conta == numero_conta:
                    print(f"Saldo atual: R${conta.saldo:.2f}")
                    break
                else:
                    print("Conta não encontrada.")
        
        elif escolha == 'q':
            print("Saindo do sistema. Até logo!")
            break

        elif escolha == '5':
            numero_conta = int(input("Digite o número da conta para consultar o extrato: "))
            consultar_extrato(numero_conta)
        
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__ma    in__":
    main()