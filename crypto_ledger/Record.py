

class Record:
    # Fields
    name_crypto = " "
    symbol_crypto = " "
    action = " "
    exchange_name = ""

    transaction_date_time = None

    quantity_of_crypto = 0
    purchase_price = 0
    transaction_fee = 0

    # These will be generated based on the current price of a given crypto
    cost_basis = 0
    cost_basis_percent = 0
    net_profit_or_loss = 0
    position_ROI_percent = 0

    # Constructor
    def __init__(self, name_crypto, symbol_crypto, action, exchange_name, transaction_date_time,
                 quantity_of_crypto, purchase_price, transaction_fee):
        self.name_crypto = name_crypto
        self.symbol_crypto = symbol_crypto
        self.action = action
        self.exchange_name = exchange_name
        # TODO: decide if you want to pull a datetime obj automatically
        self.transaction_date_time = transaction_date_time
        self.quantity_of_crypto = quantity_of_crypto
        self.purchase_price = purchase_price
        self.transaction_fee = transaction_fee

    # methods
