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
        new_list.append([int(count),int(number)])
        count += 1
    else:
        new_list.append([".",int(number)])


print(new_list)
b_new_list = new_list[::-1]
print(b_new_list)
length_list = len(new_list)
for x in b_new_list:
    if type(x[0]) is int:
        print("it is an int")
        search_dots = True
        while search_dots == True:
            for y in new_list:
                if type(y[0]) is not int:
                    if y[1] <= x[1]:
                        search_dots = False
                        
            search_dots = False



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