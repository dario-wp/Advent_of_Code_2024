filepath = "input.txt"
def finding_list(f_list):
    last_pos = len(f_list) -1
    for i, x in enumerate(f_list):
        if x == "." and i<last_pos:
            search = True
            while search == True:
                element = f_list[last_pos]
                if element != ".":
                    f_list[last_pos] = "."
                    f_list[i] = element
                    search = False
                last_pos = last_pos-1
    return f_list
my_arr = []
with open(filepath) as file:
    c = file.readline()
    my_arr = list(c)
new_list = []
count = 0
for i,number in enumerate(my_arr):
    if number == "0":
        continue
    elif i % 2 == 0:
        # print("true")
        new_list.extend([str(count)]*int(number))
        count += 1
    else:
        temp_string = "." * int(number)
        for x in temp_string:
            new_list.append(x)
final = finding_list(new_list)
final = [x for x in final if x != "."]
total = 0
for another_index,x in enumerate(final):
    total = total + (another_index*int(x))
print("TOTAL ",total)
