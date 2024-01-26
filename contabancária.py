class ContaBancaria:

    def __init__(self, num_conta, nome_titular, saldo) -> None:
        self.num_conta = num_conta
        self.nome_titular = nome_titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print(f'Depósito de R${valor} realizado com sucesso!')

    def sacar(self, valor):
        if not isinstance(valor, int):
            raise ValueError('O depósito deve ser do tipo Inteiro')

        if valor > 0:
            if self.saldo >= valor:
                print(
                    f'Você sacou {valor} e esse valor já foi descontado do seu saldo!')
                self.saldo -= valor
                print(f'Seu saldo atual é de R${self.saldo}')
            else:
                print('Você não possui saldo sufuciente para sacar essa quantia')

        else:
            print('O valor a ser sacado deve ser maior que zero')

    def consultar_saldo(self):
        print(f'Seu saldo é de : R${self.saldo}')


conta = ContaBancaria("5544321", "Eric Santos", 0)

conta.depositar(500)
conta.depositar(500)
