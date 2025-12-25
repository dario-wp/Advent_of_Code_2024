filepath = "input.txt"
total_data = []
row = -1
col = 0
player_col = 0
player_row = 0
initial_player_row = 0
initial_player_col = 0
in_map = True
direction = "up"
total_x = 0
initial_setup = []
changed_setup = []
total_positions = 0

def movement(direction,player_col,player_row,total_data):
    #it goes forward
    if direction == "up":
        total_data[player_row][player_col] = "U"
        player_row -=1
        if player_row <0:
            return False,direction,player_col,player_row
        else:
            if total_data[player_row][player_col] == "#":
                player_row +=1
                direction = "right"


    elif direction == "right":
        total_data[player_row][player_col] = "R"
        player_col +=1
        if player_col == len(total_data[player_row]):
            return False,direction,player_col,player_row
        else:
            if total_data[player_row][player_col] == "#":
                player_col -=1
                direction = "down"


    elif direction == "down":
        total_data[player_row][player_col] = "D"
        player_row +=1
        if player_row == len(total_data):
            return False,direction,player_col,player_row
        else:
            if total_data[player_row][player_col] == "#":
                player_row -=1
                direction = "left"
                
    elif direction == "left":
        total_data[player_row][player_col] = "L"
        player_col -=1
        if player_col < 0:
            return False,direction,player_col,player_row
        else:
            if total_data[player_row][player_col] == "#":
                player_col +=1
                direction = "up"
            
    return True,direction,player_col,player_row
                
def movement2(direction,player_col,player_row,total_data,infinite_loop):
    #it goes forward
    if direction == "up":
        total_data[player_row][player_col] = "U"
        player_row -=1
        if player_row <0:
            return False,direction,player_col,player_row,infinite_loop,False
        current_char = total_data[player_row][player_col]
        if current_char == "R":
            if player_row-1 >=0:
                if total_data[player_row-1][player_col] == "#":
                    infinite_loop +=1
                    #grid(total_data)
                    return False,direction,player_col,player_row,infinite_loop,True
        else:
            if current_char == "#":
                player_row +=1
                direction = "right"


    elif direction == "right":
        total_data[player_row][player_col] = "R"
        player_col +=1
        if player_col == len(total_data[player_row]):
            return False,direction,player_col,player_row,infinite_loop,False
        current_char = total_data[player_row][player_col]
        if current_char == "D":
            if player_col+1 < len(total_data[player_row]):
                if total_data[player_row][player_col+1] == "#":
                    infinite_loop +=1
                    #grid(total_data)
                    return False,direction,player_col,player_row,infinite_loop,True
        
        else:
            if total_data[player_row][player_col] == "#":
                player_col -=1
                direction = "down"


    elif direction == "down":
        total_data[player_row][player_col] = "D"
        player_row +=1
        
        if player_row == len(total_data):
            return False,direction,player_col,player_row,infinite_loop,False
        current_char = total_data[player_row][player_col]
        if current_char == "L":
            if player_row+1 < len(total_data):
                if total_data[player_row+1][player_col] == "#":
                    infinite_loop +=1
                    #grid(total_data)
                    return False,direction,player_col,player_row,infinite_loop,True
        else:
            if total_data[player_row][player_col] == "#":
                player_row -=1
                direction = "left"
                
    elif direction == "left":
        total_data[player_row][player_col] = "L"
        player_col -=1
        if player_col < 0:
            return False,direction,player_col,player_row,infinite_loop,False
        current_char = total_data[player_row][player_col]
        if current_char == "U":
            if player_col-1>= 0:
                if total_data[player_row][player_col-1] == "#":
                    infinite_loop +=1
                    #grid(total_data)
                    return False,direction,player_col,player_row,infinite_loop,True
        else:
            if total_data[player_row][player_col] == "#":
                player_col +=1
                direction = "up"
            
    return True,direction,player_col,player_row,infinite_loop,False     

def grid(total_data):
    for row,line in enumerate(total_data):
        print("row",str(row),":",line)
    print("\n")

def copy_array(initial_setup):
    total_data = []
    for row in initial_setup:
        temp_row = []
        for col in row:
            temp_row.append(col)
        total_data.append(temp_row)
    return total_data

def checks_loop(direction,player_col,player_row,new_data):
    in_loop=False
    infinite_loop = 0
    in_map = True
    count = 1
    while in_map and not in_loop and count<=20000:
         #print(count)
         count +=1
         
         in_map,direction,player_col,player_row,infinite_loop,in_loop = movement2(direction,player_col,player_row,new_data,infinite_loop)
         if in_loop:
             return True 
    if count >=20000:  
        return True   
    return False   
    

with open(filepath) as f:
    data = f.readlines()


for line in data:
    row +=1
    total_data.append(list(line.strip()))
    initial_setup.append(list(line.strip()))
    changed_setup.append(list(line.strip()))
    try:
        player_col = line.index("^")
        initial_player_col = line.index("^")
        initial_player_row = row
        player_row = row
    except:
        continue


#print("col:",player_col,"row:",player_row)

#inital_setup = total_data.copy()

while in_map:
    in_map,direction,player_col,player_row = movement(direction,player_col,player_row,total_data)
    #grid(total_data)
    
#grid(total_data)
#grid(initial_setup)
#grid(changed_setup)

for index_row,row in enumerate(total_data):
    for index_col,element in enumerate(row):
        if (index_row,index_col) == (initial_player_row,initial_player_col):
            continue
        if element in "UDRL":
            #print(index_row,index_col,element)
            new_data = copy_array(initial_setup)
            new_data[index_row][index_col] = "#"
            direction = "up"
            if checks_loop(direction,initial_player_col,initial_player_row,new_data):
                total_positions +=1

print(total_positions)