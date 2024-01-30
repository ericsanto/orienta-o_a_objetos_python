import math


class Calculadora:

    def __init__(self) -> None:
        self.num1 = 0
        self.num2 = 0
        self.resultado_num1 = 0
        self.resultado_num2 = 0

    def __multiplicar_e_dividir_num1(self, num: int) -> float:
        self.num1 = num
        resultado = (num * 5) / 8
        self.resultado_num1 = resultado
        return resultado

    def __calcular_raiz_quadrada_num1(self, num: int) -> float:
        self.num1 = num
        raiz_quadrada = math.sqrt(self.resultado_num1)
        resultado = raiz_quadrada * raiz_quadrada * raiz_quadrada
        self.resultado_num1 = resultado
        return resultado

    def __multiplicar_num2(self, num: int) -> int:
        self.num2 = num
        resultado = (num * num) + self.num1
        self.resultado_num2 = resultado
        return resultado

    def __calcular_resultado_final_num2(self) -> float:
        resultado = ((self.resultado_num2 * 2)) / 5 + 5.7
        self.resultado_num2 = resultado
        return resultado

    def calcular(self, num1: int, num2: int) -> float:
        self.__multiplicar_e_dividir_num1(num1)
        self.__calcular_raiz_quadrada_num1(num1)
        self.__multiplicar_num2(num2)
        self.__calcular_resultado_final_num2()

        resultado_final = (self.resultado_num1 + self.resultado_num2) * 4.2
        return resultado_final


calc = Calculadora()

resultado = calc.calcular(1, 1)
print(resultado)
