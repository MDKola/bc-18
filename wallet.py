""" Demonstrates virtual wallet """


class Wallet(object):
    """ Defines blue print for digital wallet """
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        """ Adds money to wallet """
        if not isinstance(amount,int):
            return "Numbers only please"
        self.balance += amount
        return self.balance

    def withdraw(self):
        """ Withdraws money from wallet """
