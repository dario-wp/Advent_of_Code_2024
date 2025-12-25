filepath = "input.txt"

# open file
my_arr = []
with open(filepath) as file:
    c = file.readline()
    c = c.replace("\n", "")
    my_arr = [int(x) for x in list(c)]


# print(my_arr)
new_list = []
count = 0
empty_list = []
pos = 0
final_list = []
for i,number in enumerate(my_arr):
    if number == 0:
        continue
    elif i % 2 == 0:
        new_list.append([int(count),number])
        temp_string = [count] * int(number)
        for x in temp_string:
            final_list.append(x)
        count += 1
    else:
        new_list.append([".",number])
        empty_list.append((pos,number))
        temp_string = "." * int(number) #creates dots
        for x in temp_string:
            final_list.append(x)
    pos += number

b_new_list = new_list
b_new_list.reverse()
length_list = len(final_list) -1 #counting from ZERO

for file_id,length in b_new_list:
    if type(file_id) is int:
        # print("it is an int")
        search_space = True
        while search_space == True:
            for i,(pos,anzahl) in enumerate(empty_list):
                if anzahl >= length and pos <length_list:
                    for z in range(length):
                        final_list[pos+z] = file_id
                        final_list[length_list-z] = "."
                    number_of_empty_spaces_left = anzahl-length
                    pos_of_next_empty_space = pos+length
                    empty_list[i] = (pos_of_next_empty_space,number_of_empty_spaces_left)
                    break
            search_space = False
    length_list = length_list - length

checksum = 0
for index, file_id in enumerate(final_list):
    if file_id == '.':
        continue
    else:
        checksum += index * file_id

print("Total:",checksum)
