f = open("input.txt")
safe = 0
lines = f.readlines()

def find_unsafe_index(values):
    index = 0
    is_safe = True

    if len(values) == 1:
        save += 1
        return True
    # increasing or decreasing?
    if values[0] == values[1]:
        # neither - unsafe
        return False
    elif values[0] > values[1]:
        # decreasing
        allow_values = {1, 2, 3}
    else:
        allow_values = {-1, -2, -3}

    while is_safe and (index< len(values)-1):
        if not((values[index] - values[index+1]) in allowed_values):
            return False
        index+=1 
    return True



for line in lines:
    values = [int(x) for x in line.split()]
    print(values)
    if len(values) ==1:
        safe+= 1
    elif values[0] == values[1]:
        values.pop(0)
        if values[0] == values[1]:
            continue
        elif values[0] > values[1]:
            #decreasing
            allowed_values = {1,2,3}
        else:
            #increasing
            allowed_values = {-1,-2,-3}
    elif values[0] > values[1]:
        #decreasing
        allowed_values = {1,2,3}
    else:
        #increasing
        allowed_values = {-1,-2,-3}

    index, is_safe = find_unsafe_index(values, allowed_values)
    if not(is_safe):
        values.pop(index)
        index, is_safe = find_unsafe_index(values, allowed_values)

    print(is_safe)
    if is_safe:
        safe += 1

print(safe)



