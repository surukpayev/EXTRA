from enum import Enum

class Currency(Enum):
    USD = 1
    RUB = 2
    KZT = 3
    EUR = 4

class BankAccount:
    def __init__(self, name, surname, initial_amount, currency):
        self.name = name
        self.surname = surname
        self.amount = initial_amount
        self.currency = currency

    @property
    def USD(self):
        return self._USD

    @USD.setter
    def USD(self, value):
        self._USD = value

    @property
    def RUB(self):
        return self._RUB

    @RUB.setter
    def RUB(self, value):
        self._RUB = value

    @property
    def KZT(self):
        return self._KZT

    @KZT.setter
    def KZT(self, value):
        self._KZT = value

    @property
    def EUR(self):
        return self._EUR

    @EUR.setter
    def EUR(self, value):
        self._EUR = value
    def addToBankAccount(self, a):
        self.amount += a

    def substractFromBankAccount(self, a):
        self.amount -= a

    def moneyConversion(self, ex_from, ex_to):
        money = self.amount
        if ex_from == Currency.USD and ex_to == Currency.KZT:
            money *= 470
        elif ex_from == Currency.KZT and ex_to == Currency.USD:
            money /= 470
        elif ex_from == Currency.EUR and ex_to == Currency.KZT:
            money *= 480
        elif ex_from == Currency.KZT and ex_to == Currency.EUR:
            money /= 480
        elif ex_from == Currency.RUB and ex_to == Currency.KZT:
            money *= 6
        elif ex_from == Currency.KZT and ex_to == Currency.RUB:
            money /= 6
        elif ex_from == Currency.USD and ex_to == Currency.RUB:
            money *= 80
        elif ex_from == Currency.RUB and ex_to == Currency.USD:
            money /= 80
        elif ex_from == Currency.EUR and ex_to == Currency.RUB:
            money *= 90
        elif ex_from == Currency.RUB and ex_to == Currency.EUR:
            money /= 90
        else:
            return 'Invalid parametres'
        self.amount = money
        self.currency = ex_to

    def __str__(self):
        return f"Name: {self.name}, Surname: {self.surname}, Amount: {self.amount}, Currency: {self.currency}"

    def __del__(self):
        print("Bank account has been deleted")

def main():
    name = input("Enter name: ")
    surname = input("Enter surname: ")
    initial_amount = float(input("Enter initial amount: "))
    currency = input("Enter currency (USD/RUB/KZT/EUR): ")
    currency = Currency[currency]
    bank_account = BankAccount(name, surname, initial_amount, currency)

    while True:
        print("""
        Choose action:
        1 - Add money to account
        2 - Withdraw money from account
        3 - Convert currency
        4 - Print account information
        5 - Exit
        """)

        action = input("Enter action number: ")

        if action == '1':
            amount = float(input("Enter amount to add: "))
            bank_account.addToBankAccount(amount)

        elif action == '2':
            amount = float(input("Enter amount to withdraw: "))
            bank_account.substractFromBankAccount(amount)

        elif action == '3':
            print("Choose currency to convert:")
            for currency in Currency:
                print(f"{currency.value} - {currency.name}")

            ex_from = input("Enter current currency number: ")
            ex_from = Currency(int(ex_from))

            ex_to = input("Enter currency to convert number: ")
            ex_to = Currency(int(ex_to))

            bank_account.moneyConversion(ex_from, ex_to)

        elif action == '4':
            print(bank_account)

        elif action == '5':
            del bank_account
            break

        else:
            print("Invalid action number, please try again")

if __name__ == "__main__":
    main()
