from copy import deepcopy

def exersise_one() -> None:
    s = 'FfEeDdCcBbAa'
    print(s[-1::-2])
    print(s[-2::-2])

def exersise_two() -> None:
    t1 = 1,2,3,4,5,6
    t2 = 7,8,9,10
    t3 = 11,12,13,14,15,16,17

    result = []
    result.extend(t1)
    result.extend(t2)
    result.extend(t3)

    result[2::2] = [0] * len(result[2::2])

    print(result)

def exersise_three() -> None:
    arr = [0] * 3
    m = [deepcopy(arr), deepcopy(arr), deepcopy(arr)]
    print(m)
    m_copy = m.copy()
    
    for i in range(len(arr)):
        m_copy[i][i] = 1
        print(m[i])

def exersise_four() -> None:
    arr = [0] * 3
    m = [deepcopy(arr), deepcopy(arr), deepcopy(arr)]
    print(m)
    m_copy = deepcopy(m)
    
    for i in range(len(arr)):
        m_copy[i][i] = 1
        print(m_copy[i])

    print('\n')

    for i in range(len(arr)):
        m_copy[i][i] = 1
        print(m[i])

def exersise_five() -> None:
    data = [
        (100, 'USD', 'EUR', 0.83),
        (100, 'USD', 'CAD', 1.27),
        (100, 'CAD', 'EUR', 0.65)
    ]

    for i in range(len(data)):
        amount, currency, target_currency, exchange_rate = data[i]
        print(f'{amount} {currency} = {int(amount * exchange_rate)} {target_currency}')


# exersise_one()
# exersise_two()
# exersise_three()
# exersise_four()
exersise_five()