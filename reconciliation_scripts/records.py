
class Trade(object):
    """A generic trade class.

       Defines the common attributes that all trade objects must have for
       comparison across different clearing firms and trading software"""

    def __init__(self, contract_name, quantity, price)
        self.contract_name = contract_name
        self.quantity = quantity
        self.price = price
        # contract_type, executing broker, conterparty, house, house, exchange, electronic, time, spread, blah blah

class Position(object):
    def __init__(self, contract_name, contract_type, quantity)
        self.contract_name = contract_name
        self.contract_type = contract_type
        self.quantity = quantity
