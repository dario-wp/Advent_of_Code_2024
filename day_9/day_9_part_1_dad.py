# read the input
input_file = 'input.txt'
with open(input_file) as f:
    lines = f.readlines()
    if 0 < len(lines) < 2:
        value = [int(a) for a in list((lines.pop(0)).strip())]
    else:
        print('wrong number of lines - expected only 1 line')
        exit(1)
print(value)
# create the file system
file_system = []
file_id = 0
empty_pos = []
current_pos = 0
for index, length in enumerate(value):
    if index % 2 == 0:
        # this is a file
        file_system.extend([file_id] * length)
        file_id += 1
    else:
        # this is empty space
        file_system.extend(['.'] * length)
        empty_pos.extend(list(range(current_pos, current_pos + length)))
    current_pos += length
print(file_system)
print(empty_pos)

last_pos = len(file_system) - 1
cur_empty_index = 0
empty_pos_index = empty_pos[cur_empty_index]
while empty_pos_index < last_pos:
    file_id = file_system[last_pos]
    if file_id != '.':
        file_system[last_pos] = '.'
        file_system[empty_pos_index] = file_id
        cur_empty_index += 1
        empty_pos_index = empty_pos[cur_empty_index]
    last_pos -= 1
print(file_system)

# compute checksum
checksum = 0
for index, file_id in enumerate(file_system):
    if file_id == '.':
        continue
    else:
        checksum += index * file_id
print(checksum)
