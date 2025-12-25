def number_of_xmas_found(row_i, col_j, lines, num_of_rows, num_of_cols):
    count=0
    #check forward

  
    for dir1 in [-1,0,1]:
        for dir2 in [-1,0,1]:
            if dir1==0 and dir2==0:
                continue
            else:
                check_dir =(dir1,dir2)
                still_to_find=list("mas") # in this order
                temp_col_j = col_j + dir1
                temp_row_i = row_i + dir2
                while len(still_to_find) > 0 and (0 <= temp_col_j < num_of_cols) and (0 <= temp_row_i < num_of_rows):
                    if lines[temp_row_i][temp_col_j] == still_to_find[0]:
                        still_to_find = still_to_find[1:]
                    else:
                        break
                    temp_col_j +=dir1
                    temp_row_i +=dir2

                if still_to_find == []:
                    count+=1    
    return count



input_file = 'input.txt'
f = open(input_file, 'r')
lines=[]
row_count=0
for line in f:
    tmp_line = list(line.strip().lower())
    #print(f"row {str(row_count).zfill(3)}: {tmp_line}")
    lines.append(tmp_line)
    row_count+=1
num_of_rows=len(lines)
num_of_cols=len(lines[0])
#print(f"Number of rows: {num_of_rows}")
#print(f"Number of columns: {num_of_cols}")
#find a character at row_i, col_j
row_i=0 # ie the forth row as the count starts at 0
col_j=0 # ie the fifth element in that row as the count starts at 0
#print(f"lines[{row_i}, {col_j}]: ={lines[row_i][col_j]}")

count_xmas=0
for row_i in range(num_of_rows):
    for col_j in range(num_of_cols):
        if lines[row_i][col_j] == 'x':
            #there might be one or more xmas here...
             count_xmas=count_xmas+number_of_xmas_found(row_i, col_j, lines, num_of_rows, num_of_cols)

print(count_xmas)
