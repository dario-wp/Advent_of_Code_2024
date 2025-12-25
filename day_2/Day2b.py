filepath = 'input.txt'

def find_unsafe_index(values):
    index = 0
    is_safe = True

    if values[0] > values[1]:
        # decreasing
        allow_values = {1, 2, 3}
    else:
        allow_values = {-1, -2, -3}

    while is_safe and (index< len(values)-1):
        if not((values[index] - values[index+1]) in allow_values):
            return False
        index+=1 
    return True

partOne = 0
partTwo = 0

with open(filepath) as f:
    lines = f.readlines()
    for index, line in enumerate(lines):
        values = [int(val) for val in line.split()]
        is_safe = find_unsafe_index(values)
        if is_safe:
            partOne += 1
        else:
            for x in range(len(values)):
                temp_values = values[:x] + values[x+1:]
                if find_unsafe_index(temp_values):
                    partTwo +=1
                    break
            
print(partOne)
print(partTwo)
