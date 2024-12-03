
def questio_one(input: str) -> None:
    if input is None or input == '' or ',' not in input:
        print(f'input str "{input}" is empty or not valid')
        return
    
    arr = input.split(',')
    result = [[], [], []]
    for i in range(len(arr)):
        cr = arr[i].strip(' ')
        result[0].append(hex(ord(cr)))
        result[1].append(cr.lower())
        result[2].append(cr.upper())

    for item in result:
        print(f'{item}')

    

def question_two(a: int) -> None: 
    print(f'The number {a} is {'even' if a % 2 == 0 else 'not event'}')

def question_three(a: int, b: int) -> None:
    result = (a / b)
    formatted_result = f'{result:.2f}' if (a % b) != 0 else f'{result:.0f}'
    print(f'a / b = {formatted_result}')

# questio_one('a, b,c ')
question_three(9, 3)
question_three(1, 3)

# questio_one('h,g,k ')
# questio_one('')
# questio_one('hello')

# question_two(12)
# question_two(123)