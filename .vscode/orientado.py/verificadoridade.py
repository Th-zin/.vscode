idade = input("Digite sua idade:")
try:

    if int(idade) >= 18 and int(idade) < 60:
        print("Você é Adulto.")
    elif int(idade) < 18 and int(idade) >= 14: 
        print("Você é Adolescente.")
    elif int(idade) < 14 and int(idade) > 3:
        print("Você é Criança.")
    else:
        print("Você É idoso")
except ValueError:
    print("Valor inválido. Tente novamente.")