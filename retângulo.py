def verificar_se_e_numero(num1, num2):
    if not isinstance(num1, (float, int)) or not isinstance(num2, (float, int)):
        raise ValueError(
            'Tanto a largura quanto a altura devem ser do tipo inteiro')
    else:
        return True


class Retangulo:
    def __init__(self, altura, largura) -> None:
        self.altura = altura
        self.largura = largura

    def calcular_area(self):
        verificar_se_e_numero(self.altura, self.largura)
        area = self.largura * self.altura
        return area

    def calcular_perimetro(self):
        verificar_se_e_numero(self.altura, self.largura)
        perimetro = 2 * (self.altura + self.largura)
        return perimetro


retangulo = Retangulo(6, 8)

area = retangulo.calcular_area()
print(f'A area do retângulo é {area}')

perimetro = retangulo.calcular_perimetro()
print(f'O perímetro do retângulo é {perimetro}')
