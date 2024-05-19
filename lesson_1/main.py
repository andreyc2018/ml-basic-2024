#!/usr/bin/env python

# 1
inp = int(input('Five digit number: '))

r0 = inp // 10000 % 10
r1 = inp // 1000 % 10
r2 = inp // 100 % 10
r3 = inp // 10 % 10
r4 = inp // 1 % 10

result = r0 * 10000 + r3 * 1000 + r2 * 100 + r1 * 10 + r4 * 1

print(f'{inp} -> {result}')


# 2
days = int(input('\nDays until vacation: '))
weeks = days // 7
reminder = days - (weeks * 7)
result = weeks * 2
if reminder == 6:
    result += 1

print(f'{days} -> {result}')


# 3
print('\nChocolate.')
inp = input('Length, Width, Pieces: ')
l = int(inp.split(',')[0].strip())
w = int(inp.split(',')[1].strip())
p = int(inp.split(',')[2].strip())
result = False

if (l * w >= p) and (p % l == 0 or p % w == 0):
    result = True

print(f'{l}, {w}, {p} -> {result}')


# 4
a_number = int(input('\nArabic to Roman.\nArabic number: '))
if a_number >= 1:
    r_number = ''

    if a_number > 0:
        divider = 1000
        r = a_number // divider
        if r > 0:
            r_number += 'M' * r
            a_number -= (divider * r)

    if a_number > 0:
        divider = 900
        r = a_number // divider
        if r > 0:
            r_number += 'CM' * r
            a_number -= (divider * r)

    if a_number > 0:
        divider = 500
        r = a_number // divider
        if r > 0:
            r_number += 'D' * r
            a_number -= (divider * r)

    if a_number > 0:
        divider = 400
        r = a_number // divider
        if r > 0:
            r_number += 'CD' * r
            a_number -= (divider * r)

    if a_number > 0:
        divider = 100
        r = a_number // divider
        if r > 0:
            r_number += 'C' * r
            a_number -= (divider * r)

    if a_number > 0:
        divider = 90
        r = a_number // divider
        if r > 0:
            r_number += 'XC' * r
            a_number -= (divider * r)

    if a_number > 0:
        divider = 50
        r = a_number // divider
        if r > 0:
            r_number += 'L' * r
            a_number -= (divider * r)

    if a_number > 0:
        divider = 40
        r = a_number // divider
        if r > 0:
            r_number += 'XL' * r
            a_number -= (divider * r)

    if a_number > 0:
        divider = 10
        r = a_number // divider
        if r > 0:
            r_number += 'X' * r
            a_number -= (divider * r)

    if a_number > 0:
        divider = 9
        r = a_number // divider
        if r > 0:
            r_number += 'IX' * r
            a_number -= (divider * r)

    if a_number > 0:
        divider = 5
        r = a_number // divider
        if r > 0:
            r_number += 'V' * r
            a_number -= (divider * r)

    if a_number > 0:
        divider = 4
        r = a_number // divider
        if r > 0:
            r_number += 'IV' * r
            a_number -= (divider * r)

    if a_number > 0:
        divider = 1
        r = a_number // divider
        if r > 0:
            r_number += 'I' * r
            a_number -= (divider * r)

    print(f'{a_number} -> {r_number}')
else:
    print(f'Unable to process {a_number}')


# 5
inp = input('\nCheck if input is a float number.\nInput: ')
result = False
inp_len = len(inp)

if inp.count('.') == 0:
    if inp.count('-') == 0:
        result = inp.isdecimal()
    elif inp[0] == '-':
        result = inp[1:].isdecimal()
elif inp.count('.') == 1:
    if inp[0] == '.':
        result = inp[1:].isdecimal()
    elif inp[-1] == '.':
        result = inp[:-1].isdecimal()
    else:
        result = inp.split('.')[0].isdecimal() and inp.split('.')[1].isdecimal()

print(f'{inp} -> {result}')
