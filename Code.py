import csv 
import math
with open("data.csv", newline="")as f:
    reader= csv.reader(f)
    fileData = list(reader)

data = fileData[0]

def mean(data):

    n = len(data)
    sum = 0

    for x in data:
        sum += int(x)
    mean = sum / n

    return mean

squared=[]

for num in data:
    sub= int(num)-mean(data)
    subt= sub**2
    squared.append(subt)

Add=0

for i in squared:
    Add += i

result = (Add / (len(data)-1))

standardDeviation = math.sqrt(result)

print(standardDeviation)