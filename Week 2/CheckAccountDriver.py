from CheckingAccount import CheckingAccount


def main():
    print('--------------------')
    print('Welcome to ABC Bank')
    print('--------------------')
    print('Let''s get your information to access your account:')
    name = input('Enter Name::=> ')
    address = input('Enter Address::=> ')
    emailAddress = input('Enter Email Adresss::=> ')
    phoneNumber = input('Enter Phone Number::=> ')
    accountNumber = input('Enter Account Number::=> ')
    accountInfo = CheckingAccount(name, address, emailAddress, phoneNumber, accountNumber);
    print('Your Current Balance Is::', accountInfo.getCurrentBalance())
    action = input('Press D for Debit Transaction OR C for Credit Transaction=> ')
    if action.__eq__('D'):
        amount = int(input('Enter Amount you want to Debit::=> '))
        availableBalance = accountInfo.getCurrentBalance()
        if availableBalance > amount:
            accountInfo.debit(amount)
        else:
            print('You don\'t have sufficient balance to debit ', amount, 'from your account. Kindly Credit your '
                                                                          'Account with sufficient balance')
    else:
        amount = int(input('Enter Amount you want to Credit::=> '))
        accountInfo.credit(amount)


main()
