from time import sleep


class Verificacoes:

    def __init__(self) -> None:
        pass

    def verificar_se_e_numero(self, num: int) -> bool:
        if isinstance(num, int):
            return True
        else:
            raise ValueError('Tipagem de dados incorreta')


class Elevador(Verificacoes):

    def __init__(self) -> None:
        self.andar = 1
        self.limite = False

    def subir_andar(self, andar: int) -> None:
        try:
            if self.verificar_se_e_numero(andar):
                if self.limite == False and andar <= 15:
                    print(f'Subindo para o {andar} andar')
                    sleep(2)
                    print(f'Chegamos no {andar} andar')
                    self.andar = andar
                else:
                    print(
                        f'Elevador está no limite de andar\n Andar atual: {self.andar}')
        except ValueError as e:
            print(f'Erro: {e}')

    def descer_andar(self, andar: int) -> None:
        try:
            if self.verificar_se_e_numero(andar):
                if self.verficar_se_andar_atual_maior_andar_desejdado(andar):
                    while andar >= 1 and andar <= 15:
                        print(f'Descendo... {self.andar} andar')
                        self.andar -= 1
                        if self.andar == andar:
                            print(f'Chegamos no andar desejado {andar} andar')
                            break
                    else:
                        print(
                            'Você está no térreo. Não é possível descer mais andares')
                else:
                    print(
                        'Não é possível descer, andar atual é menor ou igual ao andar desejado')
        except ValueError as e:
            print(f'Erro: {e}')

    def verificar_andar_atual(self):
        print(f'Atualmente, você está no {self.andar} andar')

    def verificar_se_andar_atual_maior_andar_desejdado(self, andar: int) -> bool or None:
        if self.andar > andar:
            return True
        else:
            raise ValueError('Não é possível descer andar...')


elevador = Elevador()

elevador.verificar_andar_atual()
