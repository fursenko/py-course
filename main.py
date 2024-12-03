class Account:
    def __init__(self, account_number, account_type, initial_balance) -> None:
        self.account_number = account_number
        self.account_type = account_type
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance  = self.balance + amount
            print(f'Deposited {amount}')
            print(f'New balance is: {self.balance}')
        else:
            print(f'{amount} is an invalid amount')

    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance = self.balance - amount
            print(f'Withdrawal: {amount}')
            print(f'New balance is: {self.balance}')
        else:
            if amount < 0:
                print(f'{amount} is invalid amount')
            else:
                print('Insuficient funds')
                print(f'Current balance is {self.balance}')

my_account = Account('123-456', 'savings', 1_000.00)

print('\n')

# print(my_account.account_number)
# print(my_account.account_type)
# print(my_account.balance)
# print('\n')

# my_account.deposit(100)
# print('\n')

# my_account.withdraw(600)
# print('\n')

# my_account.withdraw(10_000)
# print('\n')

print((10).__add__(25))
print(0.125)
print((0.125).as_integer_ratio())
print((0.1).as_integer_ratio())

print('\n')