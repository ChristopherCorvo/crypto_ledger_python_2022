import pymongo

'''
    This is a script to seed my mongo database with a collection of crypto transaction records
'''

MONGODB_NAME = 'crypto-ledger'
MONGODB_COLLECTION = 'records'
MONGODB_URI = "mongodb://localhost:27017/"

seed_data = [{
        "name_crypto": "Cardano",
        "symbol_crypto": "ADA",
        "action": "BUY",
        "exchange_name": "Kraken",
        "transaction_date_time": "2/5/2021",
        "quantity_of_crypto": 5000,
        "purchase_price": .51,
        "transaction_fee": 1.50
    },
    {
        "name_crypto": "Etherium",
        "symbol_crypto": "ETH",
        "action": "BUY",
        "exchange_name": "Coinbase",
        "transaction_date_time": "2/16/2021",
        "quantity_of_crypto": 1.61876792,
        "purchase_price": 1782.00,
        "transaction_fee": 5.00
    },
    {
        "name_crypto": 'Bitcoin',
        "symbol_crypto": 'BTC',
        "action": 'BUY',
        "exchange_name": 'Kraken',
        "transaction_date_time": '2/19/2021',
        "quantity_of_crypto": 0.1993,
        "purchase_price": 50782.00,
        "transaction_fee": 5.00
    },
    {
        "name_crypto": 'Etherium',
        "symbol_crypto": 'ETH',
        "action": 'BUY',
        "exchange_name": 'Coinbase',
        "transaction_date_time": '3/22/2021',
        "quantity_of_crypto": 2.00,
        "purchase_price": 1685.30,
        "transaction_fee": 5.00
    },
    {
        "name_crypto": 'Bitcoin',
        "symbol_crypto": 'BTC',
        "action": 'BUY',
        "exchange_name": 'Kraken',
        "transaction_date_time": '3/28/2021',
        "quantity_of_crypto": .17647324,
        "purchase_price": 55528.80,
        "transaction_fee": 5.00
    },
    {
        "name_crypto": 'Cardano',
        "symbol_crypto": 'ADA',
        "action": 'BUY',
        "exchange_name": 'Coinbase',
        "transaction_date_time": '4/18/2021',
        "quantity_of_crypto": 4059,
        "purchase_price": 1.23,
        "transaction_fee": 15.70
    },
    {
        "name_crypto": 'Polygon',
        "symbol_crypto": 'MATIC',
        "action": 'BUY',
        "exchange_name": 'Kucoin',
        "transaction_date_time": '5/6/2021',
        "quantity_of_crypto": 3216,
        "purchase_price": .77,
        "transaction_fee": 8.26
    },
    {
        "name_crypto": 'TelCoin',
        "symbol_crypto": 'TEL',
        "action": 'BUY',
        "exchange_name": 'Kucoin',
        "transaction_date_time": '5/8/2021',
        "quantity_of_crypto": 54813,
        "purchase_price": .04,
        "transaction_fee": 2.75
    },
    {
        "name_crypto": 'Algorand',
        "symbol_crypto": 'ALGO',
        "action": 'BUY',
        "exchange_name": 'Kraken',
        "transaction_date_time": '10/17/2021',
        "quantity_of_crypto": 812,
        "purchase_price": 1.84,
        "transaction_fee": 7.45
    },
    {
        "name_crypto": 'Shib Inu',
        "symbol_crypto": 'SHIB',
        "action": 'BUY',
        "exchange_name": 'Kucoin',
        "transaction_date_time": '10/18/2021',
        "quantity_of_crypto": 20114942,
        "purchase_price": .56,
        "transaction_fee": 7.45
    },
    {
        "name_crypto": 'Amp',
        "symbol_crypto": 'AMP',
        "action": 'BUY',
        "exchange_name": 'Coinbase',
        "transaction_date_time": '10/20/2021',
        "quantity_of_crypto": 30250,
        "purchase_price": .05,
        "transaction_fee": 7.46
    }
]

def seed_mongodb(seed_data):
    # connecting to a local mongodb instance
    my_client = pymongo.MongoClient(MONGODB_URI)
    # connect to specified database that is stored locally
    my_database = my_client[MONGODB_NAME]
    # connect to a given collection within the specified database
    my_collection = my_database[MONGODB_COLLECTION]

    # load seed_data into mongodb collection
    seed_data_record_ids = my_collection.insert_many(seed_data)
    print(seed_data_record_ids)

if __name__ == "__main__":
    seed_mongodb(seed_data)


