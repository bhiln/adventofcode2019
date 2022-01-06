def get_params(codes, cur_index, num):
    return [codes[cur_index + i] for i in range(1,num+1)]

def get_mode(codes, cur_index, i):
    mode = 0

    try:
        mode = str(codes[cur_index])[i]
    except:
        pass

    return int(mode)

def get_modes(codes, cur_index):

    return [get_mode(codes, cur_index, -3), get_mode(codes, cur_index, -4)]

codes = []
with open("input.txt",'r') as f:
    line = f.readline()
    codes = line.split(',')

codes = list(map(int, codes))

cur_index = 0
user_input = None

opcode = int(str(codes[cur_index])[-2:])

while opcode != 99:
    if opcode == 1:
        int1, int2, loc = get_params(codes, cur_index, 3)
        modes = get_modes(codes, cur_index)
        val1 = codes[int1] if modes[0] == 0 else int1
        val2 = codes[int2] if modes[1] == 0 else int2
        codes[loc] = val1 + val2
        cur_index += 4
    elif opcode == 2:
        int1, int2, loc = get_params(codes, cur_index, 3)
        modes = get_modes(codes, cur_index)
        val1 = codes[int1] if modes[0] == 0 else int1
        val2 = codes[int2] if modes[1] == 0 else int2
        codes[loc] = val1 * val2
        cur_index += 4
    elif opcode == 3:
        loc = get_params(codes, cur_index, 1)[0]
        codes[loc] = int(input('>>>'))
        cur_index += 2
    elif opcode == 4:
        loc = get_params(codes, cur_index, 1)[0]
        mode = get_mode(codes, cur_index, -3)
        print(codes[loc] if mode == 0 else loc)
        cur_index += 2
    elif opcode == 5:
        # jump-if-true
        int1, loc = get_params(codes, cur_index, 2)
        mode = get_mode(codes, cur_index, -3)
        val1 = codes[int1] if mode == 0 else int1
        cur_index = codes[loc] if val1 != 0 else cur_index + 3
    elif opcode == 6:
        # jump-if-false
        int1, loc = get_params(codes, cur_index, 2)
        mode = get_mode(codes, cur_index, -3)
        val1 = codes[int1] if mode == 0 else int1
        cur_index = codes[loc] if val1 == 0 else cur_index + 3
    elif opcode == 7:
        # less than
        int1, int2, loc = get_params(codes, cur_index, 3)
        modes = get_modes(codes, cur_index)
        val1 = codes[int1] if modes[0] == 0 else int1
        val2 = codes[int2] if modes[1] == 0 else int2
        if val1 < val2:
            codes[loc] = 1
        else:
            codes[loc] = 0
        cur_index += 4
    elif opcode == 8:
        # equals
        int1, int2, loc = get_params(codes, cur_index, 3)
        modes = get_modes(codes, cur_index)
        val1 = codes[int1] if modes[0] == 0 else int1
        val2 = codes[int2] if modes[1] == 0 else int2
        if val1 == val2:
            codes[loc] = 1
        else:
            codes[loc] = 0
        cur_index += 4
    else:
        print('error: unknown opcode', opcode)
        exit()
    
    opcode = int(str(codes[cur_index])[-2:])
