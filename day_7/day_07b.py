filepath = "input.txt"
data = []
total_value = 0


def create_equations(values):
    if len(values)==1:
        return [str(values[0])]
    else:
        result=[]
        last_val=values[-1]
        for equation in create_equations(values[:-1]):
            result.append(f"({equation}+{last_val})")
            result.append(f"({equation}*{last_val})")
            result.append(f"{eval(equation)}{last_val}")
        return result

def do_equation(target, values):
    eq_strings=create_equations(values)
    for x in eq_strings:
        if int(eval(x)) == int(target):
            return True

    return False
    calculation_string = ""
    for value in values[:-1]:
        calculation_string = calculation_string+value+"*"
    calculation_string = calculation_string+values[-1]
    x = bin(36)[2:].zfill(8)


with open(filepath) as f:
    lines = f.readlines()

for line in lines:
    new_line = line.strip().split(":")
    values = new_line[1].strip().split(" ")
    data.append((new_line[0],values))



for (target,values) in data:
    if do_equation(target,values):
        total_value += int(target)


print(total_value)
