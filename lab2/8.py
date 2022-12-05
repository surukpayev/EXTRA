def addToBankAccount(bank_account,a):
    bank_account += a
    return bank_account

def substractFromBankAccount(bank_account,a):
    bank_account -= a
    return bank_account

def moneyConversion(money, ex_from, ex_to):
    match ex_from, ex_to:
        case 'USD', 'KZT':
            return money * 470
        case 'KZT', 'USD':
            return money / 470
        case 'EUR', 'KZT':
            return money * 480
        case 'KZT', 'EUR':
            return money / 480
        case _:
            return 'Invalid parametres'
//Списал с решенных, понял решение
