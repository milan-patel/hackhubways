import csv
import sys

with open(sys.argv[1]) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    date = sys.argv[1].split('-')
    accept_count = 0
    reject_count = 0
    outcsv = open(date[0]+'_out.csv', 'w')
    for row in csv_reader:
        if(row[13]=='1969' or row[14]=='0'):
            reject_count+=1
        else:
            accept_count+=1
            outcsv.write(row[0]+","+row[1]+","+row[3]+","+row[7]+","+row[12]+","+row[13]+","+row[14]+"\n")
        '''if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            line_count += 1'''
print(f'Pass {accept_count}\nFail {reject_count}')
