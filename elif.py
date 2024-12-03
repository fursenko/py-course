account_enabled = True
balance = 1_000
# withdraw = 100_000

# if account_enabled and withdraw <= balance:
#     print('withdrawal authorized')
# else:
#     if not account_enabled:
#         print('account disabled')
#     else:
#         print('insufficient funds')

def lock_account() -> None:
    global account_enabled
    account_enabled = False
    print('account is locked')

def unlock_account() -> None:
    global account_enabled
    account_enabled = True
    print('account is unlocked')

def do_transaction(withdrawal: int) -> None:
    if not account_enabled:
        print('account is disabled')
    elif withdrawal > balance:
        print('insuficient balance')
    else:
        print('withdrawal authorized')

do_transaction(withdrawal=1_0_0)
do_transaction(withdrawal=100_000)

lock_account()

do_transaction(10)

unlock_account()

do_transaction(100)