# Criando classe pessoa com o atributo ativo como private(privado)
class Pessoa:

    __ativo = True

    def __init__(self, nome, sexo, cpf):
        self.nome = nome
        self.sexo = sexo
        self.cpf = cpf

    def desativarPessoa(self):
        self.__ativo = False
        print(f'{self.nome} foi desativado!')

    def ativarPessoa(self):
        self.__ativo = True
        print(f'{self.nome} foi ativado!')

    @property
    def get_ativo(self):
        return (self.__ativo)
    
    @property
    def set_ativo(self, valor):
        self.__ativo  = valor



p1 = Pessoa('Gabriel', 'M', '0123')
p2 = Pessoa('Joao', 'M', '0123')

p1.desativarPessoa()
# # p1.ativarPessoa()
 
p1.__ativo = True #Ele cria um novo atributo diferente do declarado na classe.


print(p1.get_ativo) #Essa é a única forma  de acessar o  __ativo  declarado dentro da classe.
print(p2.get_ativo)
