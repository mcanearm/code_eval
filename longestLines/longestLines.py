import sys

input_file = sys.argv[1]
text_dict = {}
with open(input_file) as i:
    count = 0
    for line in i:
        count += 1
        if count == 1:
            N = int(line.strip())
        else:
            line_count = len(line)
            if line_count in text_dict:
                text_dict[line_count].append(line.strip())
            else:
                text_dict.update({line_count: [line.strip()]})

line_counts = sorted(text_dict, reverse=True)
max_counts = line_counts[:N]

for key in max_counts:
    text = text_dict[key]
    for string in text:
        print(string)

