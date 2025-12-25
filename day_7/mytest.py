file = "input.txt"
values = []
total_value = 0
binary_list = []
numbers_line = []
god_damn_order = []

def check(line):
    final = line[0]
    numbers = line[1].split(" ")

def does_this_work(line):
    binary_list = get_binary(line)
    # if check(line):
    #     total_value =+ 1
    #print(line[1])
    #print(binary_list)
    #print("THIS IS LINE",line)
    for bin_value in binary_list:
        finalscript = ""
        seperator = list(bin_value)
        #print("starting value:",seperator)
        number_of_brackets = len(seperator)
        #print(number_of_brackets)
        for index,value in enumerate(seperator):
            #print("real position",seperator[2])
            value = int(value)
            if value == 0:
                seperator[index] = ")+"
            if value == 1:
                seperator[index] = ")*"
        #print("ending value:",seperator)
        seperator.append("")
        #print(seperator)
        numbers_line = line[1].split(" ")
        #print("numbers_list:",numbers_line)
        for index,x in enumerate(numbers_line):    
            finalscript = finalscript +numbers_line[index] + seperator[index]
            #print(finalscript)
            
        for x in range(number_of_brackets):
            finalscript = "(" + finalscript
            
            
        #print(finalscript,"-->",eval(finalscript),"?=",line[0])
        if int(eval(finalscript)) == int(line[0]):
            #print("We have found one!!")
            return True
            print(finalscript,"-->",eval(finalscript),"?=",line[0])

def get_binary(line):
    final = line[0]
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
        
        
        # for x in seperator:
        #     print(x)
        #     print("index:",seperator[int(x)])
        #     x = str(x)
  
        #     if x == "0":
        #         seperator[int(x)] = "+"
        #     elif x == "1":
        #         seperator[int(x)] = "*"
        
        #line_new = line[1].split(" ")





