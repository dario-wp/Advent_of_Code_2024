import numpy
import pandas

loop = int(10)
distancetemp = 0
distance = 0
number = 0
file = 'input.txt'
inputs = pandas.read_csv(file, header=None, sep=r'\s+', names=['col1', 'col2'])
col1 = inputs['col1'].values
col2 = inputs['col2'].values

col1.sort()
col2.sort()


for index,x in enumerate(col1):
    distance += abs(x-col2[index])

print("Total distance: "+str(distance))


