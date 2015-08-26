import sys

def letterInt(i):
    integer = (i - 1) % 26
    letter = chr(65 + integer)
    integer2 = int((i-1) / 26)
    if (integer2 > 0):
        return letterInt(integer2 - 1)
    else:
        return letter
    
test_cases = [1, 52, 3702, (26**3) - 1]

for i in test_cases:
    print(letterInt(i))
