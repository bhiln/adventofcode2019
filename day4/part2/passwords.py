from itertools import groupby

lower_bound = 0
upper_bound = 0
possible_count = 0
with open("input.txt",'r') as f:
    lower_bound, upper_bound = f.readline().split('-')

for i in range(int(lower_bound), int(upper_bound)):
    sort = list(map(int,str(i)))
    sort.sort()
    sort = ''.join([str(elem) for elem in sort])
    sort_int = int(sort)
    if sort_int == i and len(sort) is 6:
        groups = groupby(sort)
        result = [sum(1 for _ in group)==2 for label, group in groups]
        print (result)
        if True in result:
            possible_count += 1
            print(sort)

print (possible_count)