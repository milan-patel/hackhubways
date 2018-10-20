# Converts Start ID and End ID into zip codes 
import requests
import json
import config
import csv



def findLatLng(station_ID):
    # the Station_ID has to be a string. I couldn't get it to work as just a number
    # Example:
    # findLatLng("67") -> {'lat': 42.3581, 'lng': -71.093198} 
    # findLatLng(67) -> {} 
    d = {}
    with open("rawdata/201809-bluebikes-tripdata.csv",'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if (row[3] == station_ID):
                d['lat'] = float(row[5])
                d['lng'] = float(row[6])
                break
    return d


def findZipCode(lat, lng):
    # Make a get request to get the zipcode based on lat and lng from the Google Maps Reverse Geocoding api.
    response = requests.get("https://maps.googleapis.com/maps/api/geocode/json?latlng="+str(lat)+","+str(lng)+"&key="+config.API_KEY)

    # Print the zip code of the response.
    parsed_json = json.loads(response.content)
    return(parsed_json["results"][0]["address_components"][-1]['short_name'])

def stationIDindex():
    d1 ={}
    firstline = True
    outcsv = open("stationIDzipcodes.csv",'w')
    outcsv.write("Station ID, Zip Code\n")
    with open("rawdata/201809-bluebikes-tripdata.csv",'r') as csv_file:
        # opens the Sept. 2018 data
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if(firstline):
                firstline = False
                continue
            if(row[3] in d1):
                # checks if the stationID has been indexed already
                continue
            else:
                d1[row[3]] = True
                d = findLatLng(row[3]) 
                # writes the StationID and Zip Code to the output CSV
                outcsv.write(row[3]+','+findZipCode(d['lat'],d['lng'])+'\n')
    return
                



