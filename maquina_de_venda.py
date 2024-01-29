class Produto:

    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque


class MaquinaDeVendas:

    def __init__(self):
        self.produtos = []
        self.total = 0
        self.troco = 0
        self.produto_pago = False
        self.__caixa = 0
        self.estoque = 0
        self.quantidade = 0

    def cadastrar_produtos(self, nome, preco, estoque):
        novo_produto = Produto(nome, preco, estoque)
        self.estoque = estoque
        self.produtos.append(novo_produto)
        print('Produto cadastrado!')

    def comprar_produto(self, nome, quantidade):
        if self.estoque >= quantidade:
            for produto in self.produtos:
                if produto.nome.upper() == nome.upper():
                    produto.preco *= quantidade
                    self.total += produto.preco
                    self.quantidade = quantidade
                    print(
                        f'Produto escolhido: {produto.nome}, R${produto.preco}')
                    print('Produto pendente. Pague-o para levá-lo')
        else:
            print('Não temos a quantidade desejada em estoque')

    def pagar_produto(self, valor):
        print(f'Você deve pagar R${self.total}')
        if valor > self.total:
            self.troco = valor - self.total
            self.__caixa = self.total
            self.estoque -= self.quantidade
            print(f'Pagamento feito. Seu troco é de R${self.troco}')
            self.produto_pago = True
        elif valor == self.total:
            print('Pagamento feito!')
            self.__caixa = self.total
            self.estoque -= self.quantidade
            self.produto_pago = True
        else:
            print(
                'Não é possível realizar a compra. O valor do produto é superior ao valor que você está dando')

    def mostrar_todos_os_produtos(self):
        for produto in self.produtos:
            print(f'Produto: {produto.nome}, Preço: R${produto.preco}')
            print(end=' ')

    def get_caixa(self) -> int:
        return self.__caixa

    def set_caixa(self, valor) -> int:
        self.__caixa = valor
        return self.__caixa

    def mostrar_estoque_produto(self):
        print(f'Etoque: {self.estoque}')


maquina = MaquinaDeVendas()

maquina.cadastrar_produtos('Café', 8, 10)
maquina.comprar_produto('Café', 10)
maquina.pagar_produto(200)
maquina.mostrar_estoque_produto()
