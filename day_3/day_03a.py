import re

total = 0
first_number = 0
second_number = 0
filepath = "input.txt"

def multiply(x):
    answer = 0
    answer =int(x[0])*int(x[1])
    return answer

with open(filepath) as f:
    lines = f.readlines() 
    pattern = r"mul\((\d+),(\d+)\)"
    for line in lines:
        array = re.findall(pattern, line)
        for x in array:
            total = total + multiply(x)
print(total)
