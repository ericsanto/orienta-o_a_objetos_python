class Pessoa:

    def __init__(self, name, age, cpf) -> None:
        self.name = name
        self.age = age
        self.__cpf = cpf

    def beber(self, bebida):
        if bebida == 'cerveja':
            self.__apresentar_documento()
        print('bebendo')

    def __apresentar_documento(self):
        print(self.__cpf)


pessoa1 = Pessoa("Eric", 21, "623.386.290-60")

print(pessoa1.name)
pessoa1.beber('refrigerante')
