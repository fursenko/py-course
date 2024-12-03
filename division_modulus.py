total = 0
for i in range(1, 1_001):
    total += i
    if i % 100 == 0:
        print(f'total = {total}') 

print(f'Final total = {total}')