import calendar
import holidays
from datetime import timedelta
from datetime import datetime


class Calendario:

    def __init__(self):
        self.__aa = 2024
        self.mm = 0
        self.feriados = holidays.country_holidays("BR")
        self.feriados_2024 = datetime
        self.diferenca_dias = 0

    def exibir_calendario_mes(self, mes):
        self.mm = int(mes)
        print(calendar.month(self.__aa, self.mm))

    def verificar_diferenca_dias_entre_datas(self, data_inicial: datetime, data_final: datetime) -> int:
        diferenca = abs((data_final - data_inicial).days)
        return diferenca


calend = Calendario()
calend.exibir_calendario_mes(5)


dias = calend.verificar_diferenca_dias_entre_datas(
    datetime(2024, 1, 1), datetime(2024, 2, 2))
print(
    f'A diferença de dias entre as datas que foram fornecidas é/são: {dias} dias')
