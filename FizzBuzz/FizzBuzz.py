import sys

test_file = sys.argv[1]

def divisorTest(X, Y, N):
    res1 = N % X
    res2 = N % Y
    
    finalOutput = '%s%s' % (output1, output2)

    if finalOutput == '':
        return N
    else:
        return finalOutput


# With funciton defined proceed to operate on the file
with open(test_file, 'r') as f:
    for line in f:
        values = [int(val) for val in line.strip().split(' ')]
        div1_x = values[0]
        div2_y = values[1]
        N      = values[2]
        
        sequence = range(1, N+1)
        
        result = ' '.join([str(divisorTest(div1_x, div2_y, n)) for n in sequence])
        print(result)
