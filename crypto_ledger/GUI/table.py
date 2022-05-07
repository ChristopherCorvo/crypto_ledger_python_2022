import sys

from api_calls import *
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure


def get_records():
    """ Fetches transaction records from mongodb

        returns: [] of crypto records
    """
    client = MongoClient("mongodb://localhost:27017")
    db = client.get_database("crypto-ledger")
    collection = db.get_collection("records")

    test = [record for record in collection.find()]
    return test


def get_symbols_from_db():
    """ query mongodb for symbols

    Query mongodb for all symbols in db
    """
    client = MongoClient("mongodb://localhost:27017")
    db = client.get_database("crypto-ledger")
    collection = db.get_collection("records")

    query = {}
    projection = {
        "symbol_crypto": 1,
        "_id": 0
    }
    crypto_objs = [sym for sym in collection.find(query, projection)]
    crypto_list = list()

    for obj in crypto_objs:
        crypto_list.append(obj["symbol_crypto"])

    return crypto_list


def calc_curr_price():
    """ calls the api for the latest quote of a given symbol
    """
    cur_symbols = get_symbols_from_db()
    symbol_curr_price_map = {}

    for symbol in cur_symbols:
        symbol_curr_price_map[symbol] = retrieve_current_price(symbol)

    return symbol_curr_price_map


def format_rows():
    """ creates an array of formatted rows

    :return:
    """
    formatted_res_arr = []
    records = get_records()

    # this is an obj of symbols and their current price
    current_prices = calc_curr_price()

    for record in records:
        row = []
        curr_price = ""
        quantity = record['quantity_of_crypto']
        purchase_price = record['purchase_price']

        total_money = 0
        for field in record:
            if field != "_id":
                row.append(record[field])
                if field == "symbol_crypto":
                    if record[field] in current_prices:
                        symbol = record[field]
                        curr_price = current_prices[symbol]

        # append current price
        row.append(curr_price)
        # append cost basis
        cost_basis = purchase_price * quantity
        row.append(cost_basis)
        # append cost basis %
        row.append(0)
        # append net profit/loss
        row.append(0)
        # append position roi
        row.append(0)
        tuple_row = tuple(row)
        formatted_res_arr.append(tuple_row)

    return formatted_res_arr


def add_row():
    """ adds a row from ledger
    """
    pass


def delete_row():
    """ removes a row from ledger
    """
    pass


def edit_row():
    """ edits row from ledger
    """
    pass


# ----------------------------------------------------
class DemoApp(MDApp):
    def build(self):
        self.table = MDDataTable(
            use_pagination=True,
            column_data=[
                # populated via mongodb
                ("Name", dp(18)),
                ("Symbol", dp(18)),
                ("Action", dp(18)),
                ("Exchange", dp(18)),
                ("Date/Time", dp(18)),
                ("Quantity", dp(18)),
                ("Purchase Price", dp(18)),
                ("Fee", dp(18)),
                ("Current Price", dp(18)),
                ("Cost Basis", dp(18)),
                ("Cost Basis %", dp(18)),
                ("net profit/loss", dp(18)),
                ("position ROI", dp(18))
                # ---------------------
            ],
            row_data=format_rows(),
        )
        self.table.bind(on_row_press=self.on_row_press)
        screen = MDScreen()
        screen.add_widget(self.table)
        return screen

    @staticmethod
    def on_row_press(instance_table, instance_row):
        res = [field for field in instance_row]
        print(res)


DemoApp().run()
