import csv
import sys
import os

accept_count = 0
reject_count = 0
spec_hit = 0
outcsv = open('out.csv', 'w')
outcsv.write("duration,month,day,starttime,startstation,endstation,year,gender\n");
for filename in os.listdir('./rawdata/'):
    if filename.endswith(".csv"):
        with open("./rawdata/" + filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                if(row[13]=='1969' or row[14]=='0' or row[0]=='tripduration' or row[12]=='Customer'):
                    reject_count+=1
                else:
                    if(len(sys.argv)>2 and row[3]==sys.argv[1] and row[7]==sys.argv[2] and row[14]=='2'):
                        spec_hit+=1
                        print(row[1] + " " + row[2] + " "+ row[7] + " " + row[13] + " " + row[14])
                    accept_count+=1
                    dt = row[1].split(" ")
                    outcsv.write(row[0]+","+dt[0].split('-')[1]+","+dt[0].split('-')[2]+","+dt[1]+","+row[3]+","+row[7]+","+row[13]+","+row[14]+"\n")

print(f'Pass {accept_count}\nFail {reject_count}\nSpec {spec_hit}')
