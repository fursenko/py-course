account_enabled = True
balance = 1000
withdraw = 100

if account_enabled and withdraw <= balance:
    print('authorized')
else:
    print('not authorized')

def get_letter_grade(grade: int) -> str:
    if grade >= 90:
        return 'A'
    elif grade >= 80:
        return'B'
    elif grade >= 70:
        return 'C'
    elif grade >= 60:
        return 'D'

    return 'F'

def get_decision(grade: int) -> str:
    if grade >= 90:
        return 'Passed with distinction'
    elif grade >= 70:
        return 'Passed'

    return 'Failed'

print(get_letter_grade(55), get_decision(55))
print(get_letter_grade(64), get_decision(64))
print(get_letter_grade(72), get_decision(72))
print(get_letter_grade(81), get_decision(81))
print(get_letter_grade(91), get_decision(91))

