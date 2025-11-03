valor_passagem = 4.50
saldo_catraca = 0.0
passageiros_dia = 0


def inicializar_cartao(valor_inicial):
    return{"saldo", valor_inicial}
    # Retorna um dicionário representando o cartão com o saldo inicial.
def passar_catraca(cartao):

    #Tenta debitar o valor da passagem do cartão.
    #Retorna True se a passagem for liberada, False caso contrário.
    
    global saldo_catraca, passageiros_dia
    print("-" * 30)
    print(f"Saldo atual:R$ {cartao['saldo']:.2f}")
    print(f"Valor da passagem:R${valor_passagem:.2f}")

    if cartao["saldo"] >= valor_passagem:
        cartao["saldo"] -= valor_passagem
        saldo_catraca += valor_passagem
        passageiros_dia += 1
        print("Catraca liberada. Bom passeio!")
        return True
    else:
        print("Catrana boqueada. mt pobre para andar de busão")
        return False

def exibir_relatorio_dia():
    print("-" * 30)
    print("Relatório do dia")
    print(f"Total arrecadado: R$ {saldo_catraca: 2f}")
    print(f"Total_passageiros: {passageiros_dia}")