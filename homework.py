def print_divider() -> None:
    print('----------------------------------')

def exersise_one(a):
    if a is None:
        return 'N/A'
    return a

print(exersise_one(10))
print(exersise_one('10'))
print(exersise_one(None))

print_divider()

def exersise_two(input):
    result = 'N/A' if input is None else input
    return result

print(exersise_two(10))
print(exersise_two('10'))
print(exersise_two(None))

print_divider()

def exersise_two_b(input):
    return input if input != None else 'N/A'

print(exersise_two_b(10))
print(exersise_two_b('10'))
print(exersise_two_b(None))

print_divider()

def evaluate_credit_score(score: int) -> str:
    result = ''

    if score < 0 or score > 850:
        result = 'N/A'
    elif score < 580:
        result = 'Poor'
    elif score < 670:
        result = 'Fair'
    elif score < 740:
        result = 'Good'
    elif score < 800:
        result = 'Very Good'
    else:
        result = 'Excellent'

    return result

print(550, evaluate_credit_score(550))
print(570, evaluate_credit_score(570))
print(580, evaluate_credit_score(580))
print(590, evaluate_credit_score(590))
print(670, evaluate_credit_score(670))
print(739, evaluate_credit_score(739))
print(740, evaluate_credit_score(740))
print(801, evaluate_credit_score(801))
print(850, evaluate_credit_score(850))

print_divider()

def get_magnitude(elapsed: int) -> str:
    hours = elapsed // (60 ** 2)
    minutes = (elapsed - (hours * (60 ** 2))) // 60

    days = hours / 24
    weeks = days / 7

    if weeks > 1:
        return 'weeks'
    elif days > 1:
        return 'days'
    elif hours > 1:
        return 'hours'
    elif minutes > 1:
        return 'minutes'
    
    return 'seconds'

print(get_magnitude(10))
print(get_magnitude(100))
print(get_magnitude(1000))
print(get_magnitude(10_000))
print(get_magnitude(100_000))