#Find rountrips from processed CSV
import csv
import os

with open("out.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    outcsv = open('rt.csv', 'w')
    day = '01'
    daytrips ={}
    rt=0
    for row in csv_reader:
        if(row[2]!=day):
            daytrips ={}
            day=row[2]
        key = row[4]+row[5]+row[6]+row[7]
        oppkey =row[5]+row[4]+row[6]+row[7]
        if(oppkey in daytrips and daytrips[oppkey]!=0):
            outcsv.write(row[0]+","+row[1]+","+row[2]+","+row[4]+","+row[5]+","+row[6]+","+row[7]+"\n");
            daytrips[oppkey]-=1
            rt+=1
        else:
            if(key in daytrips):
                daytrips[key]+=1
            else:
                daytrips[key]=1
print("Total rt: " + str(rt))
