from utils import verificar_se_e_numero_1_parametro


class Carro:

    def __init__(self, marca, modelo, velocidade_atual_carro) -> None:
        self.marca = marca
        self.modelo = modelo
        self.velocidade_atual_carro = velocidade_atual_carro

    def acelerar(self, aceleracao):
        verificar_se_e_numero_1_parametro(aceleracao)
        self.velocidade_atual_carro += aceleracao
        print(
            f'O carro acelerou. Velocidade atual: {self.velocidade_atual_carro}')

    def frear(self, freio):
        verificar_se_e_numero_1_parametro(freio)
        self.velocidade_atual_carro -= freio
        print(
            f'O carro freou. Velocidade atual: {self.velocidade_atual_carro}')

    def exibir_velocidade_atual(self):
        print(f'A velocidade atual é {self.velocidade_atual_carro}')


corola = Carro("Toyota", "Corola", 50)

corola.exibir_velocidade_atual()
corola.acelerar(50)
corola.frear(20)
corola.exibir_velocidade_atual()
