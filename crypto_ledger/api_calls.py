from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

API_KEY = '425014b7-4f47-41ce-8438-36f778e30c5c'
HEADER = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': API_KEY
}

URL = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency'


def get_all_symbol_ids():
    url = f'{URL}/map'
    headers = HEADER

    session = Session()
    session.headers.update(headers)

    res = None

    try:
        response = session.get(url)
        res = json.loads(response.text)
        data = res["data"]
    except (ConnectionError, Timeout, TooManyRedirects) as error:
        print(error)

    crypto_ids = list()
    crypto_obj = dict()
    # iterate through res and create a map of name, symbol, slug
    for obj in data:
        for field in obj:
            if field in ["id", "name", "symbol", "slug"]:
                crypto_obj[field] = obj[field]

        crypto_ids.append(crypto_obj)

    return crypto_ids


def retrieve_current_price(symbol):
    url = f'{URL}/quotes/latest'
    parameters = {
        "symbol": symbol,
        "convert": "USD"
    }

    headers = HEADER

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        res = json.loads(response.text)["data"][symbol]["quote"]["USD"]["price"]
        return res
    except (ConnectionError, Timeout, TooManyRedirects) as error:
        print(error)
