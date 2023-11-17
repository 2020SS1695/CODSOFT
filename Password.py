import random

letters = []
for i in range(97, 123):
    letters.append(chr(i))

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['@', '#', '$', '&', '*']

n = int(input('ENTER THE LENGTH OF THE PASSWORD '))
if n > 0:
    complexity = input('ENTER THE STRENGTH OF THE PASSWORD (weak/strong) ').lower()
    pwd = ''
    for i in range(0, n - 3):
        pwd = pwd + random.choice(letters)
    for i in range(0, 2):
        pwd = pwd + random.choice(numbers)
    if complexity == 'weak':
        print('WEAK PASSWORD: ' + ''.join(random.choice(pwd) for _ in range(n)))
    elif complexity == 'strong':
        strpwd = []
        pwd = pwd + random.choice(symbols)
        strpwd.extend(pwd)
        random.shuffle(strpwd)
        fpwd = ''
        for i in range(0, n):
            fpwd = fpwd + strpwd[i]
        print('STRONG PASSWORD: ' + fpwd)
    else:
        print('PLEASE ENTER THE STRENGTH OF PASSWORD CORRECTLY(weak/strong)')
else:
    print('PLEASE ENTER A VALID PASSWORD LENGTH (n > 0)')

