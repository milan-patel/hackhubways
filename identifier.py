# Identifier

# Program combs through the raw data files to group together trips potentially taken by 
# a single individual

# build a function that groups together trips taken by an 'individual'  


import csv
from zipCodeConverter import *
from datetime import datetime
from datetime import timedelta

# search through all time stamps for 35-54yo females biking between two stations
# on weekdays, leaving between 7-10AM and departing 6-10 hours after their arrival
# over the last 3 months

header = ['tripduration', 'starttime', 'stoptime', 'start station id', 'start station name', 'start station latitude', 'start station longitude', 'end station id', 'end station name', 'end station latitude', 'end station longitude','bikeid', 'usertype', 'birth year', 'gender'] 

csv_files = ["rawdata/201807-bluebikes-tripdata.csv","rawdata/201808-bluebikes-tripdata.csv","rawdata/201809-bluebikes-tripdata.csv"]

# 8 possible stations within the South Boston Waterfront Area
stations = stationsByZipCode("02210")

def findTrips(demo, startID, csv_file_names):
           # demo is of the form List(Int, Int, Int)
           # where the first int is the max birthyear, 
           # the second is the min birthyear, 
           # and the third is the gender expressed as either 1 or 2
           
           #startID is the stationID you want to look at
    
           # csv_file_name is list of strings of the hubway data files being analyzed
    
           # function returns a list of all possible round trips taken by an individual
    departures = []
    arrivals = []
    output = [departures, arrivals]
    for csv_file_name in csv_file_names: 
        with open(csv_file_name, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader) # skips the header 
            for row in csv_reader:
                if(demo[0] > int(row[13]) and int(row[13]) < demo[1] and int(row[14]) == demo[2] and \
                   startID == row[3]):
                    row[1] = datetime.strptime(row[1], "%Y-%m-%d %H:%M:%S.%f")
                    row[2] = datetime.strptime(row[2], "%Y-%m-%d %H:%M:%S.%f")
                    departures.append(row)
                elif(demo[0] > int(row[13]) and int(row[13]) < demo[1] and int(row[14]) == demo[2] and \
                     startID == row[7]):
                    row[1] = datetime.strptime(row[1], "%Y-%m-%d %H:%M:%S.%f")
                    row[2] = datetime.strptime(row[2], "%Y-%m-%d %H:%M:%S.%f")
                    arrivals.append(row)
    return output


def groupTrips(lst):
    uppertime = timedelta(hours =10)
    lowertime = timedelta(hours=6)
    
    # takes in the output of findTrips, produces a dictionary of individuals
    # taking trips to and from particular locations frequently
    departures = lst[0]
    arrivals = lst[1] 
    destinations = {}
    i = 0 
    
    for departure in departures:
        i+=1
        end = departure[7]
        for arrival in arrivals:
            if(end == arrival[3] and departure[13] == arrival[13] and departure[1].date() == arrival[1].date()):
                destinations[i] = [departure,arrival]
                break
    return destinations

with open("SampleIndData.csv", 'w') as out:
    csv_writer = csv.writer(out)
    csv_writer.writerow(header)
    for k in range(0,8):
        for value in (groupTrips(findTrips([1983, 1964,2], stations[k], csv_files)).items()):
            csv_writer.writerow(value[1][0])
            csv_writer.writerow(value[1][1])


