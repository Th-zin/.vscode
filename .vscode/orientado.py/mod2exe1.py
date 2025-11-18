class conta:
    def  __init__(self, numero, cpf, nomeTitular, saldo):
        self.numero = numero
        self.cpf = cpf
        self.nomeTitular = nomeTitular
        self.saldo = saldo
        

#observe os parametros passados na criação do objeto

def main():
    c1 = conta(1, 1 , "Fulano", 1000)
    print(f"Nome do titular da conta: {c1.nomeTitular}")
    print(f"Número da conta: {c1.numero}")
    print(f"CPF do titular: {c1.cpf}")
    print(f"Saldo da conta: {c1.saldo}")



if __name__ == "__main__":
    main()