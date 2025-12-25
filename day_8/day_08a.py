# ----------- SECTION OPEN: IMPORTS AND VALUES -----------
import re
import numpy as np
filepath = "input.txt"
values = []
line_values = []
pattern = "[a-zA-z0-9]"
all_data = ""
total_columns = 0
total_rows = 0
all_searched_values = []
total=0
total_pairs = []
valid_hashtags = []
# ----------- SECTION CLOSED: IMPORTS AND VALUES -----------



# ----------- SECTION OPEN: FUNCTIONS -----------
def search_values(pattern,all_data,total_columns,total_rows):
    all_data = all_data.replace("\n","")
    matches = re.findall(pattern, all_data)
    #print("MATCHES",matches)
    for match in matches:
        all_searched_values.append([match, int(int(all_data.index(match))/total_columns),int(int(all_data.index(match))%total_rows)])
        #print("ALLVALUES",all_searched_values)
        #print("all_data1",all_data)
        all_data = all_data.replace(match, ".", 1)
        #print("all_data2",all_data)
        #print(match)
    return all_searched_values

def search_pairs(array,value,total_columns,total_rows):
    index_to_remove = int(all_searched_values.index(value))
    filtered_arr = array[:index_to_remove] + array[index_to_remove + 1:]
    pairs =[]
    for filtered_value in filtered_arr:
        if filtered_value[0] == value[0]:
            pairs.append([value,filtered_value])

    return pairs


def removing_duplicates(total_pairs):
    unique_pairs_set = set()

    for sublist in total_pairs:
        frozenset_pair = frozenset(tuple(pair) for pair in sublist)
        unique_pairs_set.add(frozenset_pair)

    unique_pairs = [list(pair) for pair in unique_pairs_set]
    unique_pairs =np.array(unique_pairs)
    return unique_pairs

def hashtag_counter(pair,total_columns,total_rows):
    valid_hashtags = []
    row_difference = int(pair[1][1]) -int(pair[0][1])
    column_difference = int(pair[1][0]) -int(pair[0][0])
    hashtag1 = [int(pair[0][0])+column_difference,int(pair[0][1])+row_difference]
    hashtag2 = [int(pair[0][0])-column_difference,int(pair[0][1])-row_difference]
    hashtag3 = [int(pair[1][0])+column_difference,int(pair[1][1])+row_difference]
    hashtag4 = [int(pair[1][0])-column_difference,int(pair[1][1])-row_difference]
    all_hashtags =[hashtag1,hashtag2,hashtag3,hashtag4]
    first_pair = [int(pair[0][0]), int(pair[0][1])]
    second_pair = [int(pair[1][0]), int(pair[1][1])]
    for hashtag in all_hashtags:
        if total_columns > hashtag[0] >= 0 and total_rows > hashtag[1] >= 0:
            if hashtag == first_pair or hashtag == second_pair:
                continue
            else:
                valid_hashtags.append(hashtag)
        else:
            continue

    return valid_hashtags
# ----------- SECTION CLOSED: FUNCTIONS -----------




# ----------- SECTION OPEN: READ FILE -----------
with open(filepath) as file:
    all_data = file.read()

with open(filepath) as file:
    lines = file.readlines()
    total_columns = len(lines)

for line in lines:
    total_rows = len(line)
    line_values = []
    line = line.strip()
    for char in line:
        line_values.append(char)
    values.append(line_values)
# ----------- SECTION CLOSED: OPEN FILE -----------



# ----------- SECTION OPEN: THE REAL DEAL -----------
all_searched_values = search_values(pattern,all_data,total_columns,total_rows)

for value in all_searched_values:
    temp_pair = search_pairs(all_searched_values,value,total_columns,total_rows)
    total_pairs.extend(temp_pair)

new_pairs = removing_duplicates(total_pairs)
modified_arr = new_pairs[:, :, 1:]

for pair in modified_arr:
    hashtags = []
    hashtags = hashtag_counter(pair,total_columns,total_rows)
    for hashtag in hashtags:
        valid_hashtags.append(hashtag)

unique_arr = [list(item) for item in set(tuple(i) for i in valid_hashtags)]
print("Amount of Unique Hashtags",len(unique_arr))
# ----------- SECTION CLOSED: THE REAL DEAL -----------
