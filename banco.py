from utils import verificar_se_e_numero_1_parametro


class Banco:

    def __init__(self):
        self.nome = ''
        self.sobrenome = ''
        self.idade = 0
        self.__cpf = ''
        self.cidade = ''
        self.saldo = 0
        self.conta_bancaria_aberta = False

    def cadastrar_clientes(self, nome, sobrenome, idade, cpf, cidade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.__cpf = cpf
        self.cidade = cidade

        if verificar_se_e_numero_1_parametro(idade):
            print('Cliente cadastrado com sucesso.')

    def abrir_conta_bancaria(self):
        if self.idade >= 18:
            print('Conta bancária aberta com sucesso!')
            self.conta_bancaria_aberta = True
        else:
            raise ValueError(
                'Você não tem idade o suficiente para abrir uma conta bancária')

    def depositar_dinheiro(self, valor):
        if self.conta_bancaria_aberta:
            self.saldo += valor
            print(f'Depósito de R${valor} realizado com sucesso!')
            print(f'Saldo Atual: {self.saldo}')
        else:
            print(f'Você não possui conta bancária aberta nesse Banco')

    def sacar_dinheiro(self, valor):
        if self.conta_bancaria_aberta:
            if self.saldo >= valor:
                self.saldo -= valor
                print(f'Você sacou R${valor}')
                print(f'Saldo Atual {self.saldo}')
            else:
                print('Você não tem saldo o suficiente para realizar essa operação')

    def verificar_saldo(self):
        if self.conta_bancaria_aberta:
            print(f'Saldo Atual: R${self.saldo}')


cliente = Banco()
cliente.cadastrar_clientes('Eric', 'Santos', 21, '06271954588', 'Lagarto')
cliente.abrir_conta_bancaria()
cliente.depositar_dinheiro(500)
cliente.sacar_dinheiro(1000)
cliente.verificar_saldo()
