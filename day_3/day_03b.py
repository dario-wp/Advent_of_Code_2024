import re

total = 0
first_number = 0
second_number = 0
filepath = "input.txt"
enabled = True

def multiply(x):
    answer = 0
    answer =int(x[0])*int(x[1])
    return answer

with open(filepath) as f:
    lines = f.readlines()
    pattern = r"(mul\((\d+),(\d+)\)|don't\(\)|do\(\))"

    for line in lines:
        matches = re.findall(pattern, line)
        for match in matches:
            if match[0] != "don't()" and enabled == True :
                try:
                    #print("enabled:  ",match)
                    total = total + int(match[1])*int(match[2])
                except:
                    continue
            elif match[0] == "do()":
                #print("ON:       ",match)
                enabled = True
            elif match[0] != "don't()" and enabled == False:
                #print("disabled: ",match)
                continue
            else:
                enabled = False
                #print("OFF:      ",match)

print(total)
