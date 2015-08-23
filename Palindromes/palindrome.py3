import sys

def palindromeTest(integer):
    integer_str = str(integer)
    integer_flip = integer_str[::-1]
    
    if (integer_str==integer_flip):
        return integer
    else:
        return

primes = set([3])
for integer in range(5, 1000, 2):
    divisor = False
    for prime in primes:
        if integer%prime==0:
            divisor = True
            break
        else:
            continue
    
    if not divisor:    
        primes.update([integer])
    else:
        continue
    
        
palindromes = set([result for result in map(palindromeTest, primes) if result])

sys.stdout.write(str(max(palindromes)))


