soma_pares = 0
numero_atual = 1
limite = 50

while numero_atual <= limite:
    # 1. Verificamos se o número atual é PAR.
    if numero_atual % 2 == 0:
        # 2. Se for par, adicionamos o número à soma.
        soma_pares += numero_atual
        
    # 3. Incrementamos o contador para ir para o próximo número.
    # ESTA LINHA DEVE ESTAR DENTRO DO WHILE (RECUEI ELA).
    numero_atual = numero_atual + 1 

print(f"A soma dos números pares de 1 a 50 é: {soma_pares}")