columns = 1
row = 1
filepath = 'sample_input.txt'
my_list = []
count_xmas = 0
row_i = 0
col_j = 0
# def check(position, line):
#     if (index_position-1)

def number_of_xmas_found(row_i,col_j,my_list,rows,columns):
    count= 0
    found= False
    still_to_find=list("mas")
    must_not_find_again = ("x")
    for dir1 in row_i[-1,0,1]:
        print(row_i)
        for dir2 in col_j[-1,0,1]:
            print(col_j)
            if dir1==0 and dir2==0:
                continue
            else:
                Check_dir=(dir1, dir2)

    if found: 
        count+=1
    return count



with open(filepath) as f:
    lines = f.readlines()
    for index_line, line in enumerate(lines):
        tmp_line = list(line.strip())
        print("row ",str(row).zfill(3),tmp_line)
        row+=1
        my_list.append(tmp_line)
rows = len(my_list)
columns = len(my_list[0])
print(rows,columns)
         
print(my_list)

print({lines[row_i][col_j]})
for row_i in range(rows):
    for col_j in range(columns):
        if my_list[row_i][col_j] == "X":
            count_xmas = count_xmas + number_of_xmas_found(row_i,col_j,my_list,rows,columns)


print("Total number of X: ",count_xmas)
    # cells = numpy.array
    # for index_line, line in enumerate(lines):
    #     seperated = textwrap.wrap(line,1)
    #     for index_position ,i in enumerate(seperated):
    #         if i == "X":
    #             print("\nHere is index_position",index_position,"\nHere is Index_line:",index_line)
    #             check(index_position,index_line)
    #         else:
    #             continue
