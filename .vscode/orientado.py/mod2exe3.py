class Conta:
    def __init__(self, numero, cpf, nomeTitular, saldo):
        self.numero = numero
        self.cpf = cpf
        self.nomeTitular = nomeTitular
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if valor > 0 and self.saldo >= valor:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
        elif valor <= 0:
            print("Valor de saque inválido.")
        else:
            print("Saldo insuficiente.")

    def gerar_extrato(self):
        print("--- Extrato da Conta ---")
        print(f"Número da Conta: {self.numero}")
        print(f"Nome do Titular: {self.nomeTitular}")
        print(f"CPF: {self.cpf}")
        print(f"Saldo Atual: R${self.saldo:.2f}")
        print("------------------------")

# Seu código de teste (no main ou em outro script que importa a classe)
def main():
    c1 = Conta(numero=1, cpf=1, nomeTitular="Joao", saldo=0)
    c1.depositar(valor=300)
    c1.gerar_extrato()
    c1.sacar(valor=100)
    c1.gerar_extrato()


def main():
    conta1 = Conta(numero=1, cpf=123, nomeTitular='João', saldo=0)
    conta2 = Conta(numero=3, cpf=456, nomeTitular='Maria', saldo=0)

    if (conta1 != conta2):
        print("Endereços de memória diferentes")


        print(conta1)
        print(conta2)


        print(conta1.saldo)
        print(conta2.saldo)
        conta1.depositar(300)
        print(conta1.saldo)
        print(conta2.saldo)

        conta1 = conta2

        if (conta1 == conta2):
            ...
            print("Endereços de memória iguais")

        print(conta1)
        print(conta2)

        print(conta1.saldo)
        print(conta2.saldo)
        conta1.depositar(1000)
        print(conta1.saldo)
        print(conta2.saldo)

if __name__ == "__main__":
    main()



