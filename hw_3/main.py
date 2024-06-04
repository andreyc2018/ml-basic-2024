#!/usr/bin/env python

from string import ascii_uppercase
import re


# 1
def change_name_style(inp:str, style:str = 'auto') -> str:
    result = []
    if sorted(inp)[0] in ascii_uppercase:
        """Input is CamelStyle"""
        if style == 'camel':
            return inp
        for p in re.findall('[A-Z][^A-Z]*', inp):
            result.append(p[0].lower() + p[1:])
        return '_'.join(result)

    if sorted(inp)[0] == '_':
        """Input is snake_style"""
        if style == 'snake':
            return inp
        for p in inp.split('_'):
            result.append(p[0].upper() + p[1:])
        return ''.join(result)

    return inp

inp = input('Function name: ')
style = input('New style (auto): ')
if len(style) == 0:
    style = 'auto'
result = change_name_style(inp, style=style)
print(f'{inp} -> {result}')


# 2
DAYSINMONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap_year(year:int) -> bool:
    leap = False
    if year % 4 != 0:
        leap = False
    elif year % 100 != 0:
        leap = True
    elif year % 400 == 0:
        leap = True
    return leap

def is_valid_date(inp:str, sep='.') -> bool:
    day = int(inp.split(sep)[0])
    month = int(inp.split(sep)[1])
    year = int(inp.split(sep)[2])
    leap = is_leap_year(year)
    if month < 1 or month > 12:
        return False
    days_in_month = DAYSINMONTH[month-1]
    if month == 2:
        days_in_month += leap
    return 1 <= day <= days_in_month

years = {4: True, 5: False, 100: False, 400: True, 500: False, 2000: True }
for year, is_leap in years.items():
    assert(is_leap_year(year) == is_leap)

inp = input('Enter date: ')
result = is_valid_date(inp)
print(f'{inp} -> {result}')


# 3
def is_prime(n:int) -> bool:
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i*i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

inp = int(input('Enter number: '))
result = is_prime(inp)
print(f'{inp} -> {result}')


# 4
"""
Alden, Haney, 18, 22638
Yoselin, Greer, 8, 7834
Darrell, Boone, 5, 26811
Eddie, Schultz, 43, 10302
Triston, Jefferson, 38, 19203
naima, Landry, 59, 8642
Dawson, Stone, 46, 22345
Saniyah, Crawford, 81, 13747
Eliezer, proctor, 19, 28429
Alexandra, Oneal, 8, 14070
Yaritza, Horne, 22, 16436
Araceli, Anthony, 19, 2927
"""
def parse_input(users:dict, inp:str, maxlen:list) -> None:
    items = inp.split(',')
    record = []
    for i in range(len(items)):
        if i <= 1:
            name = items[i].strip()
            if maxlen[i] < len(name):
                maxlen[i] = len(name)
            record.append(name.title())
        elif i == 2:
            age = int(items[i])
            if age < 18 or age > 60:
                return
            record.append(age)
        elif i == 3:
            id = int(items[i])
            if id in users.keys():
                return
            users[id] = (record)

def print_table(users:dict, maxlen:list) -> None:
    for k,v in users.items():
        print(f'{k:08} : {v[0]:>{maxlen[0]}} {v[1]:>{maxlen[1]}} {v[2]:2}')

print('\nUsers:')
users = {}
maxlen = [0, 0]
while(inp := input('')):
    parse_input(users, inp, maxlen)
print_table(users, maxlen)
