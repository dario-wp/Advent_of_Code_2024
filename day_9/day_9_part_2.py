filepath = "sample_input.txt"

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

#open file
my_arr = []
with open(filepath) as file:
    c = file.readline()
    c = c.replace("\n", "")
    my_arr = list(c)

# print(my_arr)
new_list = []
count = 0
for i,number in enumerate(my_arr):
    if number == "0":
        continue
    elif i % 2 == 0:
        temp_string = [str(count)]*int(number)

        for x in temp_string:
            new_list.append(x)
        count += 1
    else:
        temp_string = "." * int(number) #creates dots
        for x in temp_string:
            new_list.append(x)


print(new_list)
b_new_list = new_list[::-1]

# print(b_new_list)
position = 0

def dots(dot_search_new_list):
    for i, x in enumerate(dot_search_new_list):
        # print("position",position,"i",i)
        if dot_search_position == i:
            dot_search_search = True
            dot_search_count_of_how_many = 0
            dot_search_count = 0
            while search == True:
                if i + dot_search_count == len(dot_search_new_list):
                    dot_search_search = False
                elif dot_search_new_list[i] == dot_search_new_list[i + dot_search_count]:
                    dot_search_count_of_how_many += 1
                else:
                    dot_search_search = False
                dot_search_count += 1
            print("There are", count_of_how_many, "*", '"', x, '"')
            position = position + count_of_how_many
        else:
            continue

for i,x in enumerate(b_new_list):
    # print("position",position,"i",i)
    if position == i:
        search = True
        count_of_how_many = 0
        count = 0
        while search == True:
            if i+count == len(b_new_list):
                search = False
            elif b_new_list[i] == b_new_list[i+count]:
                count_of_how_many += 1
            else:
                search = False
            count +=1
        # print("There are",count_of_how_many,"*",'"',x,'"')
        position = position + count_of_how_many
    else:
        continue



# for x in
# for i,number in enumerate(new_list):
#     print("number",number)
#     # if number[0] == "0":
#     #     continue
#     if number
#         print(i, number)
#         # temp_string = [str(count)]*int(number)
#         # for x in temp_string:
#         #     new_list.append([x,number])
#         # count += 1
#     else:
#         print(i, number)
#         # temp_string = "." * int(number) #creates dots
#         # for x in temp_string:
#         #     new_list.append([x,number])
#
#
# # new_list_b = new_list[::-1]
#
# print(new_list_b)
#
#
# sorting = True
# s_count = 0
# while sorting == True:
#     print(new_list_b[s_count])
#     # print(s_count)
#     print(new_list_b[s_count][1])
#
#     print("max new list",max(new_list[:]))
#     # if new_list_b[s_count][1] > max(new_list[][])
#     s_count += 1
#     if s_count >= len(new_list_b):
#         sorting=False


# testing_final = finding_list(new_list)
# testing_final = [x for x in testing_final if x != "."]
# total = 0
#
# testing_final = list(testing_final)
# final_testing_final = []
#
# for x in testing_final:
#     if x == ".":
#         final_testing_final.extend("0")
#     else:
#         final_testing_final.extend(x)
# for another_index,x in enumerate(final_testing_final):
#     total = total + (another_index*int(x))
# print("TOTAL ",total)