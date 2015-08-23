# Memoization
import sys

input_file = sys.argv[1]

def fib(n, fib_dict={0: 0, 1: 1}):
    if n not in fib_dict:
        fib_dict[n] = fib(n-1, fib_dict) + fib(n-2, fib_dict)
        
    return fib_dict[n]
    
with open(input_file, 'r') as i:
    for line in i:
        output = fib(int(line.strip()))
        sys.stdout.write('%i\n' % output)
