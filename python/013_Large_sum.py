import math

int_list = []
with open("data.txt") as f:
    for line in f:
        int_list.append(int(line))

total = sum(int_list)

print (total)
