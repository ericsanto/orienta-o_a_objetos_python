def verificar_se_e_numero(num1, num2):
    if not isinstance(num1, (float, int)) or not isinstance(num2, (float, int)):
        raise ValueError('Os parâmtros media e nota devem ser do tipo inteiro')
    else:
        return True


class Aluno:

    def __init__(self, nome, matricula, nota1, nota2) -> None:
        self.nome = nome
        self.matriucla = matricula
        self.nota1 = nota1
        self.nota2 = nota2

    def calcular_media(self):
        verificar_se_e_numero(self.nota1, self.nota2)
        media = (self.nota1 + self.nota2)/2
        return media

    def verificar_situacao(self, media):
        if not isinstance(media, (float, int)):
            raise ValueError('A media deve ser do tipo número')
        else:
            if media >= 6:
                return f'Aprovado'
            else:
                return f'Reprovado'


aluno = Aluno("Éric", "2023004953", 6, 7)

media_aluno = aluno.calcular_media()
situacao_aluno = aluno.verificar_situacao(6.5)
print(f'A média do aluno {aluno.nome} é {media_aluno}')
print(f'O aluno {aluno.nome} foi {situacao_aluno}')
