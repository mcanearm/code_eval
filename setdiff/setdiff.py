import sys

input_file = sys.argv[1]

with open(input_file) as i:
    for line in i:

        sets = line.split(';')
        set1 = set([int(val) for val in sets[0].split(',')])
        set2 = set([int(val) for val in sets[1].split(',')])

        output_set = sorted(set1.intersection(set2))
        if output_set:
            print(','.join([str(val) for val in output_set]))
        else:
            print('')
