# Identifier

# Program combs through the raw data files to group together trips potentially taken by 
# a single individual

# build a function that groups together trips taken by an 'individual'  


import csv
from zipCodeConverter import *
from datetime import datetime
from datetime import timedelta

def convertStrToDateTime(s):
    s = datetime.strptime(s, "%Y-%m-%d %H:%M:%S.%f")
    return s
    

# search through all time stamps for [AN AGE GROUP] of [A GENDER (ONE OF MALE OR FEMALE)] biking 
# between two stations, leaving their home and returning roughly 6-10 hours after their departure

header = ['tripduration', 'starttime', 'stoptime', 'start station id', 'start station name', 'start station latitude', 'start station longitude', 'end station id', 'end station name', 'end station latitude', 'end station longitude','bikeid', 'usertype', 'birth year', 'gender'] 

csv_files = ["rawdata/201807-bluebikes-tripdata.csv","rawdata/201808-bluebikes-tripdata.csv","rawdata/201809-bluebikes-tripdata.csv"]

# Possible stations within the South Boston Waterfront Area Zip code
zipCode = "02134"
demo = [1983,1964,2] # 

def findTrips(demo, zipCode, csv_file_names):
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
    stations = stationsByZipCode(zipCode)
    for csv_file_name in csv_file_names: 
        with open(csv_file_name, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader) # skips the header 
            for row in csv_reader:
                if(row[3] in stations or row[7] in stations):
                    if(row[3] in stations and demo[0] > int(row[13]) and int(row[13]) > demo[1] and int(row[14]) == demo[2]):
                        row[1] = convertStrToDateTime(row[1])
                        row[2] = convertStrToDateTime(row[2])
                        departures.append(row)
                    elif(demo[0] > int(row[13]) and int(row[13]) > demo[1] and int(row[14]) == demo[2]):
                        row[1] = convertStrToDateTime(row[1])
                        row[2] = convertStrToDateTime(row[2])
                        arrivals.append(row)
    return output


def groupTrips(lst):
    uppertime = timedelta(hours=10)
    lowertime = timedelta(hours=6)
    
    # takes in the output of findTrips, produces a dictionary of individuals
    # taking trips to and from particular locations frequently
    departures = lst[0]
    arrivals = lst[1] 
    destinations = []
    for departure in departures:
        end = departure[7]
        start = departure[3]
        for arrival in arrivals:
            if(departure[1].date() == arrival[1].date() and end == arrival[3] and departure[13] == arrival[13] and \
               start == arrival[7] and departure[1] + lowertime < arrival[1] and departure[1] + uppertime > arrival[1] ):
                destinations.append(departure)
                destinations.append(arrival)
                break
    return destinations

def writeIndDataToCSV(demo,zipCode,csv_files):
    title = "Biking Commute Data for "
    if(demo[2] == 2):
        title += "Females "
    else:
        title += "Males "
    title+= "Aged "
    title+= str(2018-demo[0])+" to "+str(2018-demo[1])+" in "+zipCode+".csv"
    entries = groupTrips(findTrips(demo,zipCode,csv_files))
    with open(title, 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(header)
        for row in entries:
            writer.writerow(row)
    return title 


