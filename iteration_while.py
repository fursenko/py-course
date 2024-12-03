# count = 0

# while count < 10:
#     count += 1
#     print(count)

#----------------------------------------

# price = 100

# while price > 90:
#     print(f'price = {price} - waiting for price come down ...')
#     # price = price - 1
#     price -= 1

# print(f'buy at {price}')

# while price < 90:
#     print(f'price = {price} - waiting for price come down ...')
#     # price = price - 1
#     price -= 1
#     break

# print(f'buy at {price}')

# while price >= 90:
#     print('infinite loop')
#     price += 1
#     break

#----------------------------------------

data  = [100, 200, 300, 400, 500]

while len(data) > 0:
    r_element = data.pop()
    print(f'r_element = {r_element}')