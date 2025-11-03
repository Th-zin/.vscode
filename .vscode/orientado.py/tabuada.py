while True:
    try:
        numero_str = input("Escolha o número inteiro para ver a tabuada(1 a 10):")
        numero = int(numero_str)

        break
    except ValueError:
        print("Valor inválido. Tente novamente.")

print("-" * 25)
print("Tabuada do {numero}:")
print("-" * 25)

for i in range(1, 21):

    resultado = numero * i

    print(f"{numero} x {i:2} = {resultado}")

print("-" * 25)