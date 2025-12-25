file = "input.txt"
values = []
total_value = 0
binary_list = []
numbers_line = []
god_damn_order = []

def does_this_work(line):
    binary_list = get_binary(line)
    for bin_value in binary_list:
        finalscript = ""
        seperator = list(bin_value)
        number_of_brackets = len(seperator)
        for index,value in enumerate(seperator):
            value = int(value)
            if value == 0:
                seperator[index] = ")+"
            if value == 1:
                seperator[index] = ")*"
        seperator.append("")
        numbers_line = line[1].split(" ")
        for index,x in enumerate(numbers_line):    
            finalscript = finalscript +numbers_line[index] + seperator[index]
        for x in range(number_of_brackets):
            finalscript = "(" + finalscript
        if int(eval(finalscript)) == int(line[0]):
            return True

def get_binary(line):
    numbers = line[1].split(" ")
    binary_list = []
    for x in range(pow(2,len(numbers)-1)):
        binary = str((bin(int(x))[2:]).zfill(len(numbers)-1)+"\n")
        binary_list.append(str(binary).strip())
    return binary_list

with open(file) as f:
    lines = f.readlines()
    
for line in lines:
    x,y = line.strip().split(":")
    y = y.strip()
    values.append((x,y))
    
for line in values:
    if does_this_work(line):
        total_value = total_value + int(line[0])

print(total_value)