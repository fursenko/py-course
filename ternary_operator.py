# ask_price = 100

# if ask_price > 50:
#     volume = 50
# else:
#     volume = 80

# volume = 50 if ask_price > 50 else 80

def get_volume(ask_price: int) -> int:
    return 50 if ask_price > 50 else 80

def get_distance(a: int, b: int) -> int:
    distance = (a - b) if a >= b else (b - a)
    return distance

def calculate(current_value: int, running_total: int, running_count: int) -> int:
    if current_value == -999:
        clean_value = 0
    else: 
        clean_value = current_value
    
    running_total = running_total + clean_value

    return running_total

def calculate_opt(current_value: int, running_total: int, running_count: int) -> int:
    # current_value = 0 if current_value == -999 else current_value
    clean_value = current_value if current_value != -999 else 0
    running_total += clean_value
    return running_total

def calculate_opt2(current_value: int, running_total: int, running_count: int) -> int:
    return running_total + (0 if current_value == -999 else current_value)

def print_divider() -> None:
    print('----------------------')

# print(get_volume(10))
# print(get_distance(10, 20))
# print(get_distance(20, 10))

print(calculate(100, 15_000, 125))
print(calculate(-999, 15_000, 125))
print_divider()
print(calculate_opt(100, 15_000, 125))
print(calculate_opt(-999, 15_000, 125))
print_divider()
print(calculate_opt2(100, 15_000, 125))
print(calculate_opt2(-999, 15_000, 125))
