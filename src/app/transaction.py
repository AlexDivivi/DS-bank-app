class Transaction:
    def __init__(self, *, sender, recipient, subject, amount):
        self._check_sender(sender)
        self._check_recipient(recipient)
        self._check_amount(amount)
        self.sender = sender
        self.recipient = recipient
        self.subject = subject
        self.amount = amount

    @classmethod
    def _check_sender(cls, sender):
        if not type(sender) is int:
            raise AssertionError('Sender needs to be an integer')

    @classmethod
    def _check_recipient(cls, recipient):
        if not type(recipient) is int:
            raise AssertionError('Recipient needs to be an integer')

    @classmethod
    def _check_amount(cls, amount):
        if not type(amount) is float:
            raise AssertionError('Amount needs to be a float')
        elif amount <= 0:
            raise AssertionError('Amount needs to be greater than 0')

    def info(self):
        return f'From {self.sender} to {self.recipient}: {self.subject} - {self.amount} €'
