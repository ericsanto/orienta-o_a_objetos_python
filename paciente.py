import uuid


class Paciente:

    def __init__(self, nome, idade, historico_consultas) -> None:
        self.nome = nome
        self.idade = idade
        self.historico_consultas = list(historico_consultas)

    def nova_consulta(self, consulta):
        self.historico_consultas.append(consulta)
        print(
            f'Consulta: {uuid.uuid4()} \n Ocorrência: {consulta} \n Paciente: {self.nome}')

    def exibir_consultas_realizadas(self):
        print(f'Histórico de Consultas da paciente {self.nome}: ')
        for consulta in self.historico_consultas:
            print(consulta, end='\n')


paciente = Paciente("Jubriscleide", 23, 'Vomitando')

paciente.exibir_consultas_realizadas()
paciente.nova_consulta('Dor de cabeça')

paciente.exibir_consultas_realizadas()
paciente.nova_consulta('Febre')
paciente.exibir_consultas_realizadas()
