class CheckingAccount:
    __balance = 0

    def __init__(self, name, address, emailAddress, phoneNumber, accountNumber):
        self.name = name
        self.address = address
        self.emailAddress = emailAddress
        self.phoneNumber = phoneNumber
        self.accountNumber = accountNumber
        print('Welcome to ABC Bank')
        print('--------------------')
        print('Name::=> ', self.name)
        print('Account Number::=> ', self.accountNumber)
        print('--------------------')

    def getCurrentBalance(self):
        return int(self.__balance)

    def credit(self, amount):
        self.__balance = self.__balance + amount
        print('Amount Credited to your Account ::=> ', amount)
        print('Your balance is::=> ', self.__balance)

    def debit(self, amount):
        self.__balance = self.__balance - amount
        print('Amount Debited from your Account ::=> ', amount)
        print('Your Balance is::=> ', self.__balance)
