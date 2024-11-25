from datetime import datetime

def timestamp_formatter(data_str):
    try:
        data = datetime.strptime(data_str, '%d/%m/%Y %H:%M:%S')

        data_americana = data.strftime('%Y-%m-%d %H:%M:%S')
        return data_americana
    except ValueError:
        raise ValueError("Data inválida. Use o formato dd/mm/aaaa HH:MM:SS.")