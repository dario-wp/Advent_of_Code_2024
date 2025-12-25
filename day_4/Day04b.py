def number_of_xmas_found(row_i, col_j, lines):
    #check forward
    half_check = 0

    if lines[row_i-1][col_j-1] == 'm':
        if lines[row_i+1][col_j+1] == "s":
            half_check+=0.5
    if lines[row_i-1][col_j-1] == "s":
        if lines[row_i+1][col_j+1] == "m":
            half_check+=0.5    
    if lines[row_i-1][col_j+1] == 'm':
        if lines[row_i+1][col_j-1] == "s":
            half_check+=0.5
    if lines[row_i-1][col_j+1] == "s":
        if lines[row_i+1][col_j-1] == "m":
            half_check+=0.5

    if half_check == 1:
        return 1
    return 0




input_file = 'input.txt'
f = open(input_file, 'r')
lines=[]
row_count=0
for line in f:
    tmp_line = list(line.strip().lower())
    print(f"row {str(row_count).zfill(3)}: {tmp_line}")
    lines.append(tmp_line)
    row_count+=1
num_of_rows=len(lines)
num_of_cols=len(lines[0])
print(f"Number of rows: {num_of_rows}")
print(f"Number of columns: {num_of_cols}")
#find a character at row_i, col_j
row_i=0 # ie the forth row as the count starts at 0
col_j=0 # ie the fifth element in that row as the count starts at 0
print(f"lines[{row_i}, {col_j}]: ={lines[row_i][col_j]}")

count_xmas=0
for row_i in range(1,num_of_rows-1):
    for col_j in range(1,num_of_cols-1):
        if lines[row_i][col_j] == 'a':
            #there might be one or more xmas here...
             count_xmas=count_xmas+number_of_xmas_found(row_i, col_j, lines)

print(count_xmas)
