class Animal:
    def __init__(self, nome): # Corrigido: self. nome para self, nome
        self.nome = nome

    def falar(self):
        pass

    def mover(self):
        pass # Adicionado pass para que o método não esteja vazio

# Corrigida indentação da classe
class Cachorro(Animal):
    def __init__(self, nome): # Adicionado __init__ para inicializar 'nome'
        super().__init__(nome) # Chama o construtor da classe pai
    def falar(self):
        return "Au!"

    def mover(self):
        return f"{self.nome} está andando."

# Corrigida indentação da classe
class Gato(Animal):
    def __init__(self, nome): # Adicionado __init__ para inicializar 'nome'
        super().__init__(nome) # Chama o construtor da classe pai
    def falar(self):
        return "Miau!"

    def mover(self):
        return f"{self.nome} está andando." # Corrigido ponto final da string

# Corrigida indentação da classe
class Vaca(Animal):
    def __init__(self, nome): # Adicionado __init__ para inicializar 'nome'
        super().__init__(nome) # Chama o construtor da classe pai
    def falar(self):
        return "Muu!"

    def mover(self):
        return f"{self.nome} está andando."

# Classe Voador (Mix-in)
class Voador:
    def voar(self):
        # Assumindo que self.nome virá da classe Animal via herança múltipla
        return f"{self.nome} está voando."

# Classe Nadador (Mix-in)
class Nadador:
    def nadar(self):
        # Assumindo que self.nome virá da classe Animal via herança múltipla
        return f"{self.nome} está nadando."

# Corrigida indentação da classe
class Pato(Animal, Voador, Nadador):
    def __init__(self, nome): # Adicionado __init__ para inicializar 'nome'
        super().__init__(nome) # Chama o construtor da classe Animal

    def falar(self): # Corrigida indentação do método
        return "Quack!"

    def mover(self): # Corrigida indentação do método
        # O método 'mover' deve englobar o comportamento, não concatenar retornos de frases.
        # Se a intenção é dizer o que ele PODE fazer:
        return f"{self.nome} está andando, nadando e voando."
        # Se a intenção é que ele faça os movimentos:
        # return f"{self.andar()}, {self.nadar()} e {self.voar()}" # Isso funciona, mas o resultado textual é repetitivo.

    def andar(self): # Corrigida indentação do método
        return f"{self.nome} está andando."

# Código principal (fora de qualquer classe, na indentação zero)
def fazer_som(animal):
    return animal.falar()

def fazer_movimento(animal):
    return animal.mover()

if __name__ == '__main__': # Boa prática para código executável
    cachorro = Cachorro('Lug')
    gato = Gato('Floquinho')
    vaca = Vaca('Mimosa')
    pato = Pato('Pato Donald')

    print(fazer_som(cachorro))
    print(fazer_som(gato))
    print(fazer_som(vaca))
    print(fazer_som(pato))

    print(fazer_movimento(cachorro))
    print(fazer_movimento(gato))
    print(fazer_movimento(vaca))
    print(fazer_movimento(pato)) # Para o pato, ele vai usar a lógica do mover que você definiu    