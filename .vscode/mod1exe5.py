for num in range(1000, 10000):
    menor = num % 100
    maior = num // 100
    raiz = maior + menor

    if (raiz * raiz) == num:
        print(num)
        print(menor)
        print(maior)
        print(raiz)
print('Terminou')
print('saiu', num)







