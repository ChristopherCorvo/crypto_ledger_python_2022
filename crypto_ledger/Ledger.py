# The ledger is made up of a collection of records and additional information populated via API and calculations.

class Ledger:
    # Fields:
    total_cost_basis = 0
    total_trade_fees = 0
    total_net_profit_or_loss = 0
    total_portfolio_roi = 0
    total_portfolio_value = 0

    # TODO: this will hold the results of a mongodb query
    current_crypto_positions = list()

    # Constructor:
    def __init__(self):
        pass

    # Methods:
