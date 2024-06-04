#!/usr/bin/env python

# 1
inp = input('Number to single digit: ')

while len(inp) > 1:
    m = 0
    for n in inp:
        m += int(n)
    inp = str(m)

print(inp)

# 2
inp = input('\nMovie seats: ')
rows = eval(inp)
inp = int(input('Number of tickets: '))
avail = '0'*inp
for i in range(len(rows)):
    row = ''.join(str(j) for j in rows[i])
    if avail in row:
        break
else:
    i = False
print(f'{inp} -> {i}')


# 3
inp = input('\nRLE input string: ')
counter = 0
prev = ''
out = ''
for c in inp:
    if prev and c != prev:
        out += f'{counter}{prev}'
        counter = 0
    counter += 1
    prev = c
if prev:
    out += f'{counter}{prev}'
print(f'{inp} -> {out}')

# 4
inp = input('\nCaesar input string: ')
key = int(input('Key: '))
key %= 26
out = ''
for c in inp:
    s = ''
    if 'A' <= c <= 'Z':
        s = chr(ord(c) + key)
        if s > 'Z':
            s = chr(ord(s) - 26)
    elif 'a' <= c <= 'z':
        s = chr(ord(c) + key)
        if s > 'z':
            s = chr(ord(s) - 26)
    elif c == ' ':
        s = ' '
    out += f'{s}'
print(f'{inp} -> {out}')


# 5
print('\nClasses')
classes = {}
while(True):
    inp = input('')
    if not inp:
        break
    cls = inp.split()[0]
    if cls not in classes:
        classes[cls] = {}
    name = inp.split()[1]
    if name not in classes[cls]:
        classes[cls][name] = []
    grade = inp.split()[2]
    classes[cls][name].append(grade)

for cls, student in classes.items():
    print(cls)
    for name, grade in student.items():
        print(name, end=' ')
        for g in grade:
            print(g, end=' ')
        print('')
    print('')
