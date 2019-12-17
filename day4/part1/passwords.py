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
        adjacent = False
        for i in range(len(sort)-1):
            if sort[i] is sort[i+1]:
                adjacent = True
                break
        if adjacent:
            possible_count += 1

print (possible_count)