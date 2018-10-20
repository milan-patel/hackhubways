import csv
import sys

with open(sys.argv[1]) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    date = sys.argv[1].split('-')
    accept_count = 0
    reject_count = 0
    spec_hit = 0
    outcsv = open(date[0]+'_out.csv', 'w')
    for row in csv_reader:
        if(row[13]=='1969' or row[14]=='0' or row[0]=='tripduration'):
            reject_count+=1
        else:
            if(len(sys.argv)>3 and row[3]==sys.argv[2] and row[7]==sys.argv[3]):
                spec_hit+=1
                print(row[1] + " " + row[2] + " "+ row[7])
            accept_count+=1
            dt = row[1].split(" ")
            outcsv.write(row[0]+","+dt[0]+","+dt[1]+","+row[3]+","+row[7]+","+row[12]+","+row[13]+","+row[14]+"\n")

print(f'Pass {accept_count}\nFail {reject_count}\nSpec {spec_hit}')
