# ----------- SECTION OPEN: IMPORTS AND VALUES -----------
import re

filepath = "sample_input.txt"
pattern = "[a-zA-z0-9]"

# ----------- SECTION CLOSED: IMPORTS AND VALUES -----------
# ----------- SECTION OPEN: FUNCTIONS -----------
def search_values(pattern, all_data, total_columns, total_rows):
    all_searched_values = []
    matches = re.findall(pattern, all_data)
    for match in matches:
        all_searched_values.append([match, all_data.index(match) // total_columns, all_data.index(match) % total_rows])
        all_data = all_data.replace(match, ".", 1)
    return all_searched_values


def hashtag_counter(pair, total_columns, total_rows):
    valid_hashtags = set()
    row_difference = int(pair[1][1]) - int(pair[0][1])
    column_difference = int(pair[1][0]) - int(pair[0][0])
    first_pair = (int(pair[0][0]), int(pair[0][1]))
    second_pair = (int(pair[1][0]), int(pair[1][1]))

    #first hashtag
    counter = 0
    in_boundary = True
    while in_boundary:
        hashtag1 = (int(pair[0][0]) +(counter*column_difference), int(pair[0][1]) + (counter*row_difference))
        if total_columns > hashtag1[0] >= 0 and total_rows > hashtag1[1] >= 0:
            if hashtag1 == first_pair or hashtag1 == second_pair:
                counter += 1
                continue
            else:
                valid_hashtags.add(hashtag1)
                counter += 1
        else:
            in_boundary = False

    #second hashtag
    counter = 0
    in_boundary = True
    while in_boundary:
        hashtag2 = (int(pair[0][0]) - (counter*column_difference), int(pair[0][1]) - (counter*row_difference))
        if total_columns > hashtag2[0] >= 0 and total_rows > hashtag2[1] >= 0:
            if hashtag2 == first_pair or hashtag2 == second_pair:
                counter += 1
                continue
            else:
                valid_hashtags.add(hashtag2)
                counter += 1
        else:
            in_boundary = False

    #third hashtag
    counter = 0
    in_boundary = True
    while in_boundary:
        hashtag3 = (int(pair[1][0]) + (counter*column_difference), int(pair[1][1]) + (counter*row_difference))
        if total_columns > hashtag3[0] >= 0 and total_rows > hashtag3[1] >= 0:
            if hashtag3 == first_pair or hashtag3 == second_pair:
                counter += 1
                continue
            else:
                valid_hashtags.add(hashtag3)
                counter += 1
        else:
            in_boundary = False

    #fourth hashtag
    counter = 0
    in_boundary = True
    while in_boundary:
        hashtag4 = (int(pair[1][0]) - (counter*column_difference), int(pair[1][1]) - (counter*row_difference))
        if total_columns > hashtag4[0] >= 0 and total_rows > hashtag4[1] >= 0:
            if hashtag4 == first_pair or hashtag4 == second_pair:
                counter += 1
                continue
            else:
                valid_hashtags.add(hashtag4)
                counter += 1
        else:
            in_boundary = False

    # hashtag1 = (int(pair[0][0]) + column_difference, int(pair[0][1]) + row_difference)
    # hashtag2 = (int(pair[0][0]) - column_difference, int(pair[0][1]) - row_difference)
    # hashtag3 = (int(pair[1][0]) + column_difference, int(pair[1][1]) + row_difference)
    # hashtag4 = (int(pair[1][0]) - column_difference, int(pair[1][1]) - row_difference)
    # all_hashtags = [hashtag1, hashtag2, hashtag3, hashtag4]
        # if (hashtag == first_pair or hashtag == second_pair) or (not (total_columns > hashtag[0] >= 0 and total_rows > hashtag[1] >= 0)):
        #     continue
        # else:
        #     valid_hashtags.add(hashtag)
    print("VALID",valid_hashtags)

    return valid_hashtags
# ----------- SECTION CLOSED: FUNCTIONS -----------
# ----------- SECTION OPEN: READ FILE -----------
# no need to read the file twice...
values=[]
with open(filepath) as file:
    lines = file.readlines()
    total_rows = len(lines)  # this is actually the number of rows
    all_data = ''
    for line in lines:
        total_columns = len(line)  # this is actually the number of cols - but the inputs are square so it doesn't matter...
        line = line.strip()
        all_data += line  # this does now simply concatenate each line to all_data... without the \n
        if len(line) == total_columns:
            values.append(list(line))
# ----------- SECTION CLOSED: OPEN FILE -----------
# ----------- SECTION OPEN: THE REAL DEAL -----------
all_searched_values = search_values(pattern, all_data, total_columns, total_rows)

total_pairs = []
for index, value in enumerate(all_searched_values[:-1]):
    for value2 in all_searched_values[index + 1:]:
        if value[0] == value2[0]:
            total_pairs.append([[value[1], value[2]], [value2[1], value2[2]]])

valid_hashtags = set()
for pair in total_pairs:
    valid_hashtags=valid_hashtags.union(hashtag_counter(pair, total_columns, total_rows))

print("all valid hashtags",valid_hashtags)
print("Amount of Unique Hashtags", len(valid_hashtags))
# ----------- SECTION CLOSED: THE REAL DEAL -----------