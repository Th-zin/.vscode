import random
import string

def gerar_senha(comprimento):
	if comprimento <= 0:
		return "O comprimento deve ser maior que zero"
	caracteres = string.ascii_letters + string.digits + string.punctuation
	senha = ''.join(random.choices(caracteres, k=comprimento))
	return senha

if __name__ == "__main__":
    print("--Gerador de Senhas--")
try:
    comprimento = int(input("Digite o comprimento da senha: "))
    senha_gerada = gerar_senha(comprimento)
    print(f"Senha gerada: {senha_gerada}")
except ValueError:
    print("Por favor, Digite um número válido para o comprimento.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")














