from datetime import date, time, datetime, timedelta


def trabalhando_datetime():
    data_atual = datetime.now()
    print(data_atual)
    print(data_atual.strftime('%d/%m/%Y - %H:%M'))
    print(data_atual.strftime('%c'))
    print(data_atual.weekday())
    tupla_dias = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo')
    tupla_meses = ('Janeiro', 'Fevereiro', 'Março')
    print(tupla_dias[data_atual.weekday()])
    print(tupla_meses[data_atual.month])
    nova_data = data_atual - timedelta(days=365)
    nova_data = nova_data.strftime('%d/%m/%Y')
    print(nova_data)


def trabalhando_date():
    data_atual = date.today()
    data_atual = data_atual.strftime('%d/%B/%Y')
    print(data_atual)


def trabalhando_time():
    horario = time(hour=15, minute=18, second=30)
    print(horario.strftime('%H:%M:%S'))


if __name__ == '__main__':
    # trabalhando_date()
    # trabalhando_time()
    trabalhando_datetime()
