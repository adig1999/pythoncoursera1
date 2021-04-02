class BankAccount:
    """ Class definition modeling the behavior of a simple bank account """

    def __init__(self, initial_balance):
        """Creates an account with the given balance."""
        …
    def deposit(self, amount):
        """Deposits the amount into the account."""
        …
    def withdraw(self, amount):
        """
        Withdraws the amount from the account. Each withdrawal resulting
        in a negative balance also deducts a penalty fee of 5 dollars
        from the balance.
        """
        …
    def get_balance(self):
        """Returns the current balance in the account."""
        …
    def get_fees(self):
        """Returns the total fees ever deducted from the account."""
        …
