# ----------- SECTION OPEN: IMPORTS AND VALUES -----------

filepath = "input.txt"

# ----------- SECTION CLOSED: IMPORTS AND VALUES -----------
# ----------- SECTION OPEN: FUNCTIONS -----------

def hashtag_counter(pair, total_columns, total_rows):
    valid_hashtags = set()
    row_difference = int(pair[1][1]) - int(pair[0][1])
    column_difference = int(pair[1][0]) - int(pair[0][0])
    for x in range(0,2):
        counter = 0
        in_boundary = True
        while in_boundary:
            if x == 0:
                hashtag = (int(pair[0][0]) +(counter*column_difference), int(pair[0][1]) + (counter*row_difference))
            elif x == 1:
                hashtag = (int(pair[0][0]) - (counter * column_difference),int(pair[0][1]) - (counter * row_difference))
            if total_columns > hashtag[0] >= 0 and total_rows > hashtag[1] >= 0:
                valid_hashtags.add(hashtag)
                counter += 1
            else:
                in_boundary = False

    return valid_hashtags


# ----------- SECTION CLOSED: FUNCTIONS -----------
# ----------- SECTION OPEN: READ FILE -----------
# no need to read the file twice...
all_searched_values = []
with open(filepath) as file:
    lines = file.readlines()
    total_rows = len(lines)
    total_columns = 0
    for row, line in enumerate(lines):
        line = line.strip()
        if row == 0:
            # only do this once
            total_columns = len(line)
        if len(line) == total_columns:
            # we only append lines that have the same length as the first one.
            for col, char in enumerate(line):
                # find the antenna positions
                if char != '.':
                    all_searched_values.append([char, row, col])
# ----------- SECTION CLOSED: OPEN FILE -----------
# ----------- SECTION OPEN: THE REAL DEAL -----------

total_pairs = []
for index, value in enumerate(all_searched_values[:-1]):
    for value2 in all_searched_values[index + 1:]:
        if value[0] == value2[0]:
            total_pairs.append([[value[1], value[2]], [value2[1], value2[2]]])

valid_hashtags = set()
for pair in total_pairs:
    valid_hashtags = valid_hashtags.union(hashtag_counter(pair, total_columns, total_rows))

print("all valid hashtags", valid_hashtags)
print("Amount of Unique Hashtags", len(valid_hashtags))  # ----------- SECTION CLOSED: THE REAL DEAL -----------
