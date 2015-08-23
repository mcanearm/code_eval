import sys

primes = set()
n = 1
while len(primes) < 1000:
    n += 1
    if n==2:
        primes.update([n])
    else:
        divisor = False
        for prime in primes:
            if n%prime==0:
                divisor = True
                break
            else:
                continue
        
        if not divisor:    
            primes.update([n])
        else:
            continue

sys.stdout.write(str(sum(primes)))
