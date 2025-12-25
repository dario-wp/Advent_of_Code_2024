filepath = "sample_input.txt"
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
infinite_loop = 0

def movement(direction,player_col,player_row,total_data,infinite_loop):
    #it goes forward
    if direction == "up":
        total_data[player_row][player_col] = "U"
        player_row -=1
        if player_row <0:
            return False,direction,player_col,player_row,infinite_loop
        current_char = total_data[player_row][player_col]
        if current_char == "R":
            infinite_loop +=1
            grid(total_data)
        else:
            if current_char == "#":
                player_row +=1
                direction = "right"


    elif direction == "right":
        total_data[player_row][player_col] = "R"
        player_col +=1
        if player_col == len(total_data[player_row]):
            return False,direction,player_col,player_row,infinite_loop
        current_char = total_data[player_row][player_col]
        if current_char == "D":
            infinite_loop +=1
            grid(total_data)
        else:
            if total_data[player_row][player_col] == "#":
                player_col -=1
                direction = "down"


    elif direction == "down":
        total_data[player_row][player_col] = "D"
        player_row +=1
        
        if player_row == len(total_data):
            return False,direction,player_col,player_row,infinite_loop
        current_char = total_data[player_row][player_col]
        if current_char == "L":
            infinite_loop +=1
            grid(total_data)
        else:
            if total_data[player_row][player_col] == "#":
                player_row -=1
                direction = "left"
                
    elif direction == "left":
        total_data[player_row][player_col] = "L"
        player_col -=1
        if player_col < 0:
            return False,direction,player_col,player_row,infinite_loop
        current_char = total_data[player_row][player_col]
        if current_char == "U":
            infinite_loop +=1
            grid(total_data)
        else:
            if total_data[player_row][player_col] == "#":
                player_col +=1
                direction = "up"
            
    return True,direction,player_col,player_row,infinite_loop         

def grid(total_data):
    for row,line in enumerate(total_data):
        print("row",str(row),":",line)
    print("\n")


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

while in_map:
    in_map,direction,player_col,player_row,infinite_loop = movement(direction,player_col,player_row,total_data,infinite_loop)
    

    
print(infinite_loop)