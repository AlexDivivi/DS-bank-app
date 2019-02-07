import app


class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}
        self.transactions = []

    def open_account(self, account):
        if not type(account) is app.Account:
            raise AssertionError('Account should be an app.Account')
        elif account.number in self.accounts:
            raise AssertionError(f'Account number {account.number} already taken!')
        else:
            self.accounts.update({account.number: account})
            return account

    def add_transaction(self, *, sender, recipient, subject, amount):
        if amount <= 0:
            raise AssertionError('Amount needs to be greater than 0')
        elif sender.number not in self.accounts:
            raise AssertionError('Sender has no account yet!')
        elif recipient.number not in self.accounts:
            raise AssertionError('Recipient has no account yet!')
        else:
            trans = app.Transaction(sender=sender.number, recipient=recipient.number, subject=subject, amount=amount)
            self.transactions.append(trans)
            self._update_funds(sender, recipient, amount)
            return trans

    def _update_funds(self, sender, recipient, amount):
        if sender.has_funds_for(amount):
            recipient.add_to_balance(amount)
            sender.subtract_from_balance(amount)
        else:
            self.transactions.pop()
            raise AssertionError('Account has not enough funds')
