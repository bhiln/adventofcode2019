codes = []
with open("input.txt",'r') as f:
    line = f.readline()
    codes = line.split(',')

codes = list(map(int, codes))
codes[1] = 12
codes[2] = 2

cur_index = 0
opcode = codes[cur_index]
while opcode != 99:
    int1 = codes[cur_index+1]
    int2 = codes[cur_index+2]
    loc = codes[cur_index+3]
    if opcode == 1:
        codes[loc] = codes[int1] + codes[int2]
    elif opcode == 2:
        codes[loc] = codes[int1] * codes[int2]
    cur_index += 4
    opcode = codes[cur_index]

print (codes[0])