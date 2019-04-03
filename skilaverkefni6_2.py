# Matthías Ólafur
import csv

with open("triangle67.txt","r") as file:
    csv = csv.reader(file, delimiter=' ')
    data = []
    for x in csv:
        data.append(list(map(int, x)))

def triangle_v2(data,row=0,column=0,memo={}):
    d = data[row]
    if row == len(data)-1:
        return d[column]
    summa = 0
    if (str(row+1) + "," + str(column)) in memo:
        summa1 = memo[str(row+1) + "," + str(column)]
    else:
        summa1 = triangle_v2(data,row+1,column,memo)
    if (str(row + 1) + "," + str(column+1)) in memo:
        summa2 = memo[str(row + 1) + "," + str(column+1)]
    else:
        summa2 = triangle_v2(data,row+1,column+1,memo)
    if summa1 >= summa2:
        summa += summa1
    else:
        summa += summa2
    summa += d[column]
    memo[str(row) + "," + str(column)] = summa
    return summa

print(triangle_v2(data))
