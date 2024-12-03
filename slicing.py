s = 'Python rocks!'

print(s[5])
print(s[0:5])
print(s[0:6])

t = (1, 2, 3, 4, 5)
t2 = (1, 2, 3, 4, 5)

tp = type(t[1: 4])
# print(tp)
# print(type(t[1:3]) is type(t2[1:3]))
# print(type('a') is type('b'))

# print(tp[0])

l = [[0, 0, 0], [1, 1, 1], [2, 2, 2]]
sub = l[0]
sub[0] = 'python'
sub[1] = 100

test = l[len(l) - 1:len(l) - 3:-1]

test[0][0] = 'bjj'

# print(l)

s = 'Python rocks!'

# print(s[6:])
# print(s[:6])
# print(s[:])

# l = [0] * 7
# for i in range(len(l)):
#     l[i] = i

# del l[0]

# print(l)

# l2 = l[:]

# print(l is l2)

l = [0] * 10
for i in range(len(l)):
    l[i] = i + 1

print(l)
print(l[1:8:2])
print(l[1::2])
print(l[::2])
print(l[-4:-1])
print(l[-4:])
print(l[-5::1])
print(l[-1:-5:-1])
print(l[-1::-1])
print(l[-1:-4:-1])
# print(l[-4:0])
# print(l[-1:-4])

def isPolindrome(s: str) -> bool:
    return s == s[-1::-1]

# print(isPolindrome('anna'))
# print(isPolindrome('bob'))
# print(isPolindrome('hello'))

# print(('hello')[-2:1:1])