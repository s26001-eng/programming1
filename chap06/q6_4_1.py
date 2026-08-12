import random
# 何回実行しても同じ結果になるように乱数の種(seed)を固定する
random.seed(1)
msgs = ["Hi", "Hello", "Good morning", "Good night", "See you later", "How are you", "Have a good day"]
with open("some.txt","w") as f:
    for i in range(1000000):
        f.write("{}, {}\n".format(i, random.choice(msgs)))

f = open('some.txt')
body = f.read()
lines = body.split('\n')
print('\n'.join(lines[:3]))

f = open('some.txt')
print(next(f), end="")
print(next(f), end="")
f.close()

f = open('some.txt')
c = 0
for l in f:
    print(l, end='')
    if c == 2:
        break
    c += 1
f.close()

f = open('some.txt')
c = 0
for l in f:
    print(l, end='')
    if c == 2:
        break
    c += 1
f.close()

with open('some.txt', 'r') as f:
    for c, l in enumerate(f):
        print(l, end='')
        if c==2:
            break

f = open('some.txt')
lines = ''
for i in range(3):
    lines += f.readline()
print(lines)
f.close()
