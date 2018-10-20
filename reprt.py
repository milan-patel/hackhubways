import csv
import os

multicol = {}
hit=0
with open("rt.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        sig = row[3]+","+row[4]+","+row[5]+","+row[6]
        if(sig in multicol):
            multicol[sig]+=1
            hit+=1
        else:
            multicol[sig]=1
for k in list(multicol.keys()):
    if(multicol[k]<50):
        del multicol[k];

print(multicol)
print(len(multicol))
