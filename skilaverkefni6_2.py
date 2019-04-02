# Matthías Ólafur
import csv

with open("triangle.txt","r") as file:
    csv = csv.reader(file, delimiter=' ')
    data = []
    for x in csv:
        data.append(list(map(int, x)))
print("len",len(data))

def triangle(data,row=0,column=0):
    if row == len(data):
        return 0
    d = data[row]
    if row == 0:
        print("0",d[column])
        return triangle(data,row+1) + d[column]
    if d[column] >= d[column+1]:
        print("2",row,d[column])
        return triangle(data,row+1,column) + d[column]
    else:
        print("4",row,d[column+1])
        return triangle(data,row+1,column+1) + d[column+1]

print(triangle(data))