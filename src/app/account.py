class Account:
    def __init__(self, *, number, firstname, lastname, balance=0.0):
        self._check_number(number)
        self._check_balance(balance)
        self.number = number
        self.firstname = firstname
        self.lastname = lastname
        self.balance = balance

    @classmethod
    def _check_number(cls, number):
        if not type(number) is int:
            raise AssertionError('Number needs to be an integer')

    @classmethod
    def _check_balance(cls, balance):
        if not type(balance) is float:
            raise AssertionError('Balance needs to be a float')

    def info(self):
        return f'Number {self.number}: {self.firstname} {self.lastname} - {self.balance} €'

    def has_funds_for(self, value):
        if self.balance >= value:
            return True
        else:
            return False

    def add_to_balance(self, value):
        if value > 0:
            self.balance = self.balance + value
        else:
            raise AssertionError('Amount needs to be greater than 0')

    def subtract_from_balance(self, value):
        if self.balance > value:
            self.balance = self.balance - value
        else:
            raise AssertionError('Account has not enough funds')
