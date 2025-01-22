class Pessoa:

    __ativo = True

    def __init__(self):
        self.pernas = 2


class Homem(Pessoa):

    def __init__(self, altura):
        self.altura = altura
        self.sexo = 'M'


p1 = Homem(1212)

print(p1.pernas)