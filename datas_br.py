from datetime import datetime

class DatasBr:

    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        return self.formata_data()

    def mes_cadastro(self):
        meses_do_ano = [
            "janeiro", "fevereiro", "março", "abril", "maio", "junho",
            "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
        ]
        mes_cadastro = self.momento_cadastro.month - 1
        return meses_do_ano[mes_cadastro]

    def dia_semana(self):
        dia_semana_lista = [
            "segunda-feira", "terça-feira", "quarta-feira", "quinta-feira",
            "sexta-feira", "sábado", "domingo"
        ]
        dia_semana = self.momento_cadastro.weekday()
        return dia_semana_lista[dia_semana]

    def formata_data(self):
        deta_formatada = self.momento_cadastro.strftime("%d/%m/%Y %H:%M")
        return deta_formatada