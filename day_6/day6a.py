filepath = "input.txt"
total_data = []
row = -1
col = 0
player_col = 0
player_row = 0
in_map = True
direction = "up"
total_x = 0

def movement(direction,player_col,player_row,total_data):
    total_data[player_row][player_col] = "X"
    
    #it goes forward
    if direction == "up":
        player_row -=1
        if player_row <0:
            return False,direction,player_col,player_row
        else:
            if total_data[player_row][player_col] == "#":
                player_row +=1
                direction = "right"


    elif direction == "right":
        player_col +=1
        if player_col == len(total_data[player_row]):
            return False,direction,player_col,player_row
        else:
            if total_data[player_row][player_col] == "#":
                player_col -=1
                direction = "down"


    elif direction == "down":
        player_row +=1
        if player_row == len(total_data):
            return False,direction,player_col,player_row
        else:
            if total_data[player_row][player_col] == "#":
                player_row -=1
                direction = "left"
                
    elif direction == "left":
        player_col -=1
        if player_col < 0:
            return False,direction,player_col,player_row
        else:
            if total_data[player_row][player_col] == "#":
                player_col +=1
                direction = "up"
            
    return True,direction,player_col,player_row
                

def grid(total_data):
    for row,line in enumerate(total_data):
        print("row",str(row),":",line)
    print("\n")


with open(filepath) as f:
    data = f.readlines()


for line in data:
    row +=1
    print("row"+str(row)+":"+line.strip())
    total_data.append(list(line.strip()))
    try:
        player_col = line.index("^")
        player_row = row
    except:
        continue


#print("col:",player_col,"row:",player_row)


while in_map:
    in_map,direction,player_col,player_row = movement(direction,player_col,player_row,total_data)
    #grid(total_data)
    
for line in total_data:
    for x in line:
        if x == "X":
            total_x +=1

print(total_x)