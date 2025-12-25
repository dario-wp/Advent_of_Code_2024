filepath_data = "input_data.txt"
filepath_rules = "input_rules.txt"
lines =[]
valid_data = []
rules = []
total = 0

def islinevalid(data,rules):
    for [p1,p2] in rules:
        try:
            p1_index = data.index(p1)
            p2_index = data.index(p2)
        except:
            continue
        if p1_index > p2_index:
            #print("returning False",p1_index,p2_index)
            return False  
    #print(data)
    return True         
        


with open(filepath_data) as f:
    content_data = f.readlines()

with open(filepath_rules) as f:
    content_rules = f.readlines()

for line in content_rules:
    rule =  line.strip().split("|")
    rules.append(rule)

for line in content_data:
    data =  line.strip().split(",")
    if islinevalid(data,rules):
        total = total + int(data[int((len(data)/2))])

print(total)
