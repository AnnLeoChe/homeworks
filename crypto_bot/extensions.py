import requests
import json
from config import keys

class ConvertExaption(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def convert(quote:str, base: str, amount: str):


        if quote == base:
            raise ConvertExaption(f'невозможно еревести одинаковые валюты {base}')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertExaption(f'не удалось обработать валюту {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertExaption(f'не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertExaption(f'не удалось введеное количество {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = round(json.loads(r.content)[keys[base]]* amount, 3)

        return total_base