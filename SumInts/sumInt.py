import sys

input_file = sys.argv[1]

run_sum = 0
with open(input_file) as i:
    for line in i:
        run_sum += int(line)
        
    print(run_sum)
