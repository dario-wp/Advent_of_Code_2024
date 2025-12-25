import numpy
import pandas

safe_value = 0
filepath = 'sample_input.txt'


def values_increasing(values_array):
    if values_array[0] < values_array[1]:
            temp_unsafe = False
            for x in range(len(values_array)-1):
                the_diff = values_array[x+1] - values_array[x]
                if 0< the_diff < 4:
                    continue
                else:
                    temp_unsafe= True
                    values_array.pop(x+1)
            if not temp_unsafe:
                safe_value= safe_value + 1


def values_decreasing(values_array):                
    if values_array[0] > values_array[1]:
        temp_unsafe = False
        for x in range(len(values_array)-1):
            the_diff = values_array[x] - values_array[x+1]
            if 0< the_diff < 4:
                continue
            else:
                temp_unsafe= True
            if not temp_unsafe:
                safe_value= safe_value + 1


def values_equal(values_array):
    if values_array[0] == values_array[1]:
        temp_unsafe = True


with open(filepath) as f:
    lines = f.readlines()
    for number_of_row, number_on_line in enumerate(lines):
        values_array=[int(val) for val in number_on_line.split()]
        #print(f"line {index+1}: {str(values)}")
        if len(values_array) == 1:
            safe_value= safe_value + 1
            continue
        values_increasing(values_array,)
        values_decreasing(values_array)
        values_equal(values_array)
        
        
                
        
        


print(safe_value)
        

        #for position in values_array:
         #   print(position[)
          #  print(position)
        #for x in values:
          #  if 
           #     largest_number 
           # print(x)
        #while test = True:
         #   if values[index]
