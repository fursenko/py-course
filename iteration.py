# r = range(1, 10)
# print(type(r))
# print(tuple(r))
# print(range(10))
# print(list(range(3, 10)))
# print(list(range(3, 12, 2)))

#----------------------------------------------------------------------------------------------------------

# for i in ['a', 'b', 'c']:
#     r = i + i
#     print(r)
# print('done')
# print(list(range(10)))

# for i in range(10):
#     print(i * 2)

# for i in range(100):
#     print(''.join(['*'] * i))

# for t in enumerate('hello, my dear friend'):
#     print(t[0])

# data = [10, 23, 34, 5, -3, 12, -98]
# print(data)

# for t in enumerate(data):
#     i, vl = t
#     data[i] = vl if vl >= 0 else -1 * vl

# print(data)

# for i, value in enumerate(data):
#     data[i] = value if value >= 0 else 'NEGATIVE'

# print(data)

# suits = ['spades', 'club', 'diamonds', 'hearts']

# for suit in suits:
#     abbrev = suit[0].upper()
#     print(f'{abbrev} = {suit}')

# for i in 'python':
#     print(i)

# print(i)
# print(suit)

# for i in range(2, 11, 2):
#     print(i)

# for i in range(3):
#     for j in range(3):
#         print(f'i: {i}, j={j}')

# m = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
# ]

# for row in m:
#     for item in row:
#         print(item)

# print('\n'.join(m))

# for yi, y in enumerate(range(2, -1, -1)):
#     for x in range(3):
#         print(f'({x}, {yi}) = {m[y][x]}')

# for row_index in range(len(m)):
#     for column_index in range(len(m[0])):
#         print()

# m = [
#     [1,2,3,4],
#     [5,6,7],
#     [8,9],
#     [10]
# ]

# for row_index in range(len(m)):
#     for column_index in range(len(m[row_index])):
#         print(f'row_i {row_index}, column_i {column_index} = {m[row_index][column_index]}')

# n = 10

# matrix = []

# for r_i in range(n):
#     matrix.append([0] * n)
#     for c_i in range(n):
#         if r_i == c_i:
#             matrix[r_i][c_i] = '*'
#         else:
#             matrix[r_i][c_i] = 'O'

# for row in matrix:
#     print(row)

data = [10, 20, 30]
en = enumerate(data)
# print(en)
# print(id(en))
# print(hex(id(en)))

# for i, value in enumerate(data):
#     print(i, value)

m = [
    [1,2,3,4],
    [5,6,7],
    [8,9],
    [10]
]

# for row in m:
#     for item in row:
#         print(item)

# for ri, row in enumerate(m):
#     print(ri, row)

# for ri, row in enumerate(m):
#     for ci, value in enumerate(row):
#         print(f'{str((ri, ci)).replace('(', '[').replace(')', ']')} = {value}')

data = [10.5, 12.3, 12.9, None, 55.0, None]
print(data)

# for i, value in enumerate(data):
#     data[i] = value if value is not None else 0

# for i, value in enumerate(data):
#     if value is not None:
#         continue

#     data[i] = 0

# i = 0

# while i < len(data):
#     data[i] = data[i] if data[i] is not None else 0
#     ++i

## print(data)

def get_average(arr) -> int:
    total = 0
    for i, value in enumerate(data):
        if value is not None:
            total += value
    
    return total / len(data)

def align_int_arr(arr, average):
    for i, value in enumerate(arr):
        if value is None:
            arr[i] = average

average = int(get_average(data))

print(get_average(data))
# align_int_arr(data, average)
print(data)

# print(list(value for value in data if value is not None))
print(sum(1 for value in data if value is not None))

print(sum(value for value in data if value is not None))
# print(max(value for value in data if value is not None))
print(sum(value if value is not None else 0 for value in data))

from statistics import fmean
data = [12, 3434, 35, 22, 98, None, 90]
average = fmean(value for value in data if value is not None)
clean_data = list(value if value is not None else average for value in data)
print(average)
print(clean_data)