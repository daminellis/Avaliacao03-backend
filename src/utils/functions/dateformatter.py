from datetime import datetime

def date_formatter(data_str):
    try:
        data = datetime.strptime(data_str, '%d/%m/%Y')

        data_americana = data.strftime('%Y-%m-%d')
        return data_americana
    except ValueError:
        raise ValueError("Data inválida. Use o formato dd/mm/aaaa.")