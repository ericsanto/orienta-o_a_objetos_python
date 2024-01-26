def verificar_se_e_numero(num1, num2):
    if not isinstance(num1, (float, int)) or not isinstance(num2, (float, int)):
        raise ValueError(
            'Os parâmetros preço e quantidade devem ser do tipo numero')


class Produto:

    def __init__(self, nome, valor, estoque):
        self.nome = nome
        self.valor = valor
        self.estoque = estoque

    def calcular_valor_total_em_estoque(self):
        verificar_se_e_numero(self.estoque, self.valor)
        valor_total = self.valor * self.estoque
        return valor_total

    def verificar_disponibilidade_produto(self):
        if self.estoque > 0:
            return f"Quantidade diponível em estoque {self.estoque}"
        else:
            return "Não está disponível em estoque"


produto = Produto("Café", 7, 10)

produto_valor_total = produto.calcular_valor_total_em_estoque()
print(produto_valor_total)
